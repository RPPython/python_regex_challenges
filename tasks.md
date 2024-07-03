## Python Homework Assignment: Regular Expression Challenges

### Tasks
You are provided with a series of strings. Your task is to write Python functions using regular expressions to transform these strings as specified.

1. **Email Anonymizer:**
    - **Function Name:** `email_anonymizer`
    - **Input:** A string containing email addresses.
    - **Output:** The same string but with email addresses replaced by `"[email]"`.
    - **Example Input:** `"Contact us at support@example.com"`
    - **Example Output:** `"Contact us at [email]"`

2. **Date Formatter:**
    - **Function Name:** `date_formatter`
    - **Input:** A string containing dates in various formats (e.g., `DD-MM-YYYY`, `MM/DD/YYYY`, `YYYY.MM.DD`).
    - **Output:** The same string but with all dates converted to `YYYY-MM-DD` format.
    - **Example Input:** `"Event date: 12/05/2023 or 05.12.2023"`
    - **Example Output:** `"Event date: 2023-05-12 or 2023-05-12"`

3. **Phone Number Standardizer:**
    - **Function Name:** `standardize_phone`
    - **Input:** A string containing phone numbers in various formats.
    - **Output:** The string with phone numbers standardized to `(XXX) XXX-XXXX` format.
    - **Example Input:** `"Call +359-88-7123-456 for assistance"`
    - **Example Output:** `"Call +359 88 7123 456 for assistance"`

4. **Whitespace Normalizer:**
    - **Function Name:** `normalize_whitespace`
    - **Input:** A string with irregular spacing (extra spaces, tabs, newlines).
    - **Output:** The same string with all whitespace sequences replaced by a single space.
    - **Example Input:** `"This  text   contains irregular    spacing."`
    - **Example Output:** `"This text contains irregular spacing."`

5. **HTML Tag Remover:**
    - **Function Name:** `remove_html_tags`
    - **Input:** A string containing HTML tags.
    - **Output:** The string with all HTML tags removed.
    - **Example Input:** `"<p>This is a <b>bold</b> move!</p>"`
    - **Example Output:** `"This is a bold move!"`
