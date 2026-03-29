import pandas as pd

class SemanticCategorizer:
    def __init__(self):
        # NLP keyword-based categorization lexicon
        self.knowledge_base = {
            "aws": "Essential Operations",
            "amazon web services": "Essential Operations",
            "gcp": "Essential Operations",
            "azure": "Essential Operations",
            "github": "Essential Operations",
            "slack": "Essential Operations",
            "zoom": "Essential Operations",
            "hubspot": "Variable Growth",
            "salesforce": "Variable Growth",
            "linkedin": "Variable Growth",
            "google ads": "Variable Growth",
            "mailchimp": "Variable Growth",
            "wework": "Essential Operations",
            "uber": "Variable Growth",
            "doordash": "Redundant/Shadow IT",
            "starbucks": "Redundant/Shadow IT",
            "netflix": "Redundant/Shadow IT",
            "spotify": "Redundant/Shadow IT",
            "personal": "Redundant/Shadow IT"
        }
        
    def categorize(self, df: pd.DataFrame) -> pd.DataFrame:
        if 'merchant' not in df.columns:
            df['category'] = 'Uncategorized'
            return df
            
        def get_category(merchant_name):
            if not isinstance(merchant_name, str):
                return 'Uncategorized'
            name_lower = merchant_name.lower()
            for key, cat in self.knowledge_base.items():
                if key in name_lower:
                    return cat
            return 'Uncategorized'
            
        df['category'] = df['merchant'].apply(get_category)
        return df
