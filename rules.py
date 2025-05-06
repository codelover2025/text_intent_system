import re

KEYWORDS = {
    "PHPLead": ["php", "laravel", "symfony"],
    "VendorLead": ["vendor", "supplier", "partner"],
    "NoLead": ["unsubscribe", "spam", "remove"]
}

def rule_based_intent(text: str):
    # Clean the text (this can be more advanced depending on your needs)
    text = text.lower()

    # Check for each intent and its associated keywords
    for intent, keywords in KEYWORDS.items():
        # Create a regex pattern to match whole words only
        pattern = r'\b(?:' + '|'.join(map(re.escape, keywords)) + r')\b'
        
        if re.search(pattern, text):  # Search for whole word matches only
            return intent

    return None
