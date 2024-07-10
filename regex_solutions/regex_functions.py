# regex_functions.py

### YOUR CODE HERE

import re

# 1. Email Anonymizer
def anonymize_emails(text):
    """Replaces email addresses with '[email]'."""
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.sub(email_pattern, '[email]', text)

# 2. Date Formatter
def format_date(text):
    """Converts dates to 'YYYY-MM-DD' format."""
    # Patterns for different date formats
    date_patterns = [
        (r'\b(\d{2})-(\d{2})-(\d{4})\b', r'\3-\2-\1'),  # DD-MM-YYYY to YYYY-MM-DD
        (r'\b(\d{2})/(\d{2})/(\d{4})\b', r'\3-\1-\2'),  # MM/DD/YYYY to YYYY-MM-DD
        (r'\b(\d{4})\.(\d{2})\.(\d{2})\b', r'\1-\2-\3'), # YYYY.MM.DD to YYYY-MM-DD
    ]
    
    for pattern, replacement in date_patterns:
        text = re.sub(pattern, replacement, text)
        
    return text

# 3. Phone Number Standardizer
def standardize_phone(text):
    """Standardizes phone numbers to '(XXX) XXX-XXXX' format."""
    phone_pattern = r'\+?(\d{3})[-. ]?(\d{2})[-. ]?(\d{4})[-. ]?(\d{3})'
    return re.sub(phone_pattern, r'(\1) \2-\3-\4', text)

# 4. Whitespace Normalizer
def normalize_whitespace(text):
    """Replaces all whitespace sequences with a single space."""
    return re.sub(r'\s+', ' ', text).strip()

# 5. HTML Tag Remover
def remove_html_tags(text):
    """Removes all HTML tags."""
    html_tag_pattern = r'<.*?>'
    return re.sub(html_tag_pattern, '', text)


