import pandas as pd
import pdfplumber

class DocumentParser:
    def __init__(self):
        # Universal schema mapper to ingest distinct documents into a unified structure
        self.column_mapping = {
            'charge': 'transaction_amount',
            'billed': 'transaction_amount',
            'amount': 'transaction_amount',
            'cost': 'transaction_amount',
            'vendor': 'merchant',
            'merchant': 'merchant',
            'date': 'transaction_date',
            'timestamp': 'transaction_date'
        }

    def _normalize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        # Standardize to lowercase and strip whitespace
        df.columns = [str(c).lower().strip() for c in df.columns]
        
        # Deduplicate results if multiple columns standardized to the same name (e.g., 'Amount' and 'AMOUNT')
        df = df.loc[:, ~df.columns.duplicated()].copy()
        
        # Map columns using the universal schema mapper
        new_columns = [self.column_mapping.get(c, c) for c in df.columns]
        df.columns = new_columns
        
        # Deduplicate again in case multiple source columns mapped to the same target (e.g., 'Charge' and 'Billed')
        df = df.loc[:, ~df.columns.duplicated()].copy()
        
        # Hydrate missing structure with defaults
        if 'transaction_amount' not in df.columns:
            df['transaction_amount'] = 0.0
        if 'merchant' not in df.columns:
            df['merchant'] = 'Unknown'
        if 'transaction_date' not in df.columns:
            df['transaction_date'] = pd.NaT

        # Purge localized artifacts in financial numerics
        if df['transaction_amount'].dtype == 'object':
            df['transaction_amount'] = (
                df['transaction_amount']
                .astype(str)
                .str.replace('$', '', regex=False)
                .str.replace(',', '', regex=False)
            )
        df['transaction_amount'] = pd.to_numeric(df['transaction_amount'], errors='coerce').fillna(0.0)
        df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
        return df

    def parse_csv(self, file_buffer) -> pd.DataFrame:
        df = pd.read_csv(file_buffer)
        return self._normalize_columns(df)

    def parse_xlsx(self, file_buffer) -> pd.DataFrame:
        df = pd.read_excel(file_buffer)
        return self._normalize_columns(df)

    def parse_pdf(self, file_buffer) -> pd.DataFrame:
        """
        VLM contextual extraction proxy. Uses table extraction heuristic mappings.
        """
        all_tables = []
        with pdfplumber.open(file_buffer) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    if len(table) > 1:
                        df_table = pd.DataFrame(table[1:], columns=table[0])
                        all_tables.append(df_table)
        
        if not all_tables:
            return pd.DataFrame(columns=['transaction_date', 'merchant', 'transaction_amount'])

        combined = pd.concat(all_tables, ignore_index=True)
        return self._normalize_columns(combined)

    def parse(self, file_buffer, file_type: str) -> pd.DataFrame:
        if file_type == 'csv':
            return self.parse_csv(file_buffer)
        elif file_type in ['xlsx', 'xls']:
            return self.parse_xlsx(file_buffer)
        elif file_type == 'pdf':
            return self.parse_pdf(file_buffer)
        else:
            raise ValueError(f"Unsupported document topology: {file_type}")
