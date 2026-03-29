import pandas as pd
import numpy as np
from scipy import stats

class AnomalyDetector:
    def __init__(self, z_thresh=2.5):
        self.z_thresh = z_thresh

    def detect_statistical_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        anomalies = []
        for category, group in df.groupby('category'):
            if len(group) > 2:
                # Bypass division by zero / nan issues on identical arrays
                z_scores = np.abs(stats.zscore(group['transaction_amount'], nan_policy='omit'))
                z_scores = np.nan_to_num(z_scores)
                
                outlier_indices = group.index[z_scores > self.z_thresh]
                
                for idx in outlier_indices:
                    anomalies.append({
                        'index': idx,
                        'reason': f"Z-SCORE FLAG: High velocity outlier ({group.loc[idx, 'transaction_amount']}) in {category}."
                    })
        return pd.DataFrame(anomalies)

    def detect_contextual_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        anomalies = []
        
        # Identical transaction vectors
        duplicates = df[df.duplicated(subset=['merchant', 'transaction_amount', 'transaction_date'], keep=False)]
        for idx in duplicates.index:
            anomalies.append({
                'index': idx,
                'reason': "CONTEXT FLAG: Exact duplicate charge within matching chronology."
            })
            
        if 'transaction_date' in df.columns:
            weekend_mask = df['transaction_date'].dt.dayofweek >= 5
            high_value_weekend = df[weekend_mask & (df['transaction_amount'] > 500)]
            for idx in high_value_weekend.index:
                anomalies.append({
                    'index': idx,
                    'reason': "CONTEXT FLAG: Abnormal weekend billing cycle behavior > $500."
                })
                
        return pd.DataFrame(anomalies)

    def flag_anomalies(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        stat_anomalies = self.detect_statistical_anomalies(df)
        cont_anomalies = self.detect_contextual_anomalies(df)
        
        if stat_anomalies.empty and cont_anomalies.empty:
            df['is_anomaly'] = False
            df['anomaly_reason'] = ""
            return df

        all_anomalies = pd.concat([stat_anomalies, cont_anomalies]).drop_duplicates(subset=['index'])
        if not all_anomalies.empty:
            all_anomalies.set_index('index', inplace=True)
            df['is_anomaly'] = False
            df['anomaly_reason'] = ""
            df.loc[all_anomalies.index, 'is_anomaly'] = True
            
            # Group anomaly strings if multiple apply
            grouped_reasons = all_anomalies.groupby(all_anomalies.index)['reason'].apply(lambda x: ' | '.join(x))
            df.loc[grouped_reasons.index, 'anomaly_reason'] = grouped_reasons
        else:
            df['is_anomaly'] = False
            df['anomaly_reason'] = ""
            
        return df
