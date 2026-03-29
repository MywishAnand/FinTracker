import pandas as pd

class OptimizerIntelligence:
    def __init__(self):
        pass

    def generate_roadmap(self, df: pd.DataFrame) -> dict:
        total_spend = df['transaction_amount'].sum()
        if total_spend == 0:
            return {"Leakage Score": 0, "Total Spend": 0, "Leakage Amount": 0, "Recommendations": []}
            
        category_spend = df.groupby('category')['transaction_amount'].sum()
        shadow_spend = category_spend.get("Redundant/Shadow IT", 0)
        anomaly_spend = df[df['is_anomaly'] == True]['transaction_amount'].sum()
        
        # Calculate algorithmic leakage (100% of shadow, 50% risk weight from anomalies)
        leakage_amount = shadow_spend + (anomaly_spend * 0.5)
        raw_score = (leakage_amount / total_spend) * 100 * 3
        leakage_score = int(min(max(raw_score, 0), 100))
        
        recommendations = []
        if shadow_spend > 0:
            recommendations.append(f"🟢 High Impact / Low Effort: Terminate redundant tools contributing ${shadow_spend:,.2f} to Shadow IT spend.")
        
        if anomaly_spend > 0:
            recommendations.append(f"🟡 High Impact / Med Effort: Conduct forensic audit on ${anomaly_spend:,.2f} of anomalous transactions (duplicates / vendor creep).")
            
        unclassified = category_spend.get("Uncategorized", 0)
        if unclassified > total_spend * 0.1:
            recommendations.append(f"🔵 Med Impact / Low Effort: Taxonomize ${unclassified:,.2f} in uncategorized spend to improve pipeline visibility.")

        if not recommendations:
            recommendations.append("📉 Baseline achieved. Recommend monitoring fixed operations for incremental savings.")

        return {
            "Leakage Score": leakage_score,
            "Total Spend": total_spend,
            "Leakage Amount": leakage_amount,
            "Recommendations": recommendations
        }
