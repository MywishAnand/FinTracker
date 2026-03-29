import re
import pandas as pd

class PIIRedactor:
    def __init__(self):
        self.patterns = {
            "ssn": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
            "credit_card": re.compile(r'\b(?:\d[ -]*?){13,16}\b'),
            "email": re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        }
        
    def redact_text(self, text: str) -> str:
        if not isinstance(text, str):
            return text
        for key, pattern in self.patterns.items():
            text = pattern.sub(f"[REDACTED_{key.upper()}]", text)
        return text

    def redact_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Scans all string-based columns and executes the redaction pipelines.
        """
        df_redacted = df.copy()
        for col in df_redacted.columns:
            if df_redacted[col].dtype == 'object':
                df_redacted[col] = df_redacted[col].apply(self.redact_text)
        return df_redacted
