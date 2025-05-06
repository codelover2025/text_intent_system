import re
import string

def clean_text(text: str) -> str:
    """
    Cleans the input text by:
    1. Lowercasing the text.
    2. Removing punctuation.
    3. Removing digits.
    4. Removing extra spaces.
    5. Stripping leading/trailing spaces.

    Args:
        text (str): The input text to be cleaned.

    Returns:
        str: The cleaned text.
    """
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Remove digits (optional)
    text = re.sub(r'\d+', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text
