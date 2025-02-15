import re

# Sample string containing various data types
sample_string = """
Email addresses: c.mushipe@alustudent.com, clive.mushipe@virtualyours.co.rw
URLs: https://www.virtualyours.com, http://fabric.virtualyours.org/page
Phone numbers: (254) 112-2801, 078-768-4130, 011.286.9870
Credit card numbers: 1234 5678 9012 3456, 1234-5678-9012-3456
Time: 14:30, 2:30 PM
HTML tags: <h1>Title</h1>, <a href="https://www.virtualyours.com">Link</a>
Hashtags: #virtualyours, #ThisIsAHashtag
Currency amounts: $19.99, $1,234.56
"""

# Regex patterns for extraction
regex_patterns = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "url": r"https?://(?:www\.)?\S+\.\S+",
    "phone": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "credit_card": r"\b(?:\d{4}[- ]?){3}\d{4}\b",
}

# Function to extract data using regex
def extract_data(text, pattern_name):
    pattern = regex_patterns[pattern_name]
    matches = re.findall(pattern, text)
    return matches

# Extract and display results
print("Email addresses:", extract_data(sample_string, "email"))
print("URLs:", extract_data(sample_string, "url"))
print("Phone numbers:", extract_data(sample_string, "phone"))
print("Credit card numbers:", extract_data(sample_string, "credit_card"))