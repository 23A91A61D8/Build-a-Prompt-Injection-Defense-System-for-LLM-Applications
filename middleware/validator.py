import re


class OutputValidator:

    def __init__(self):

        # Patterns that indicate sensitive information
        self.sensitive_patterns = [

            # API keys
            r"api[_-]?key",

            # Password mentions
            r"password",

            # Secret tokens
            r"secret",

            # Email addresses
            r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",

            # Phone numbers (10 digits)
            r"\b\d{10}\b",

            # Long token strings
            r"[A-Za-z0-9]{32,}",

        ]

    def contains_sensitive_data(self, response):

        for pattern in self.sensitive_patterns:
            if re.search(pattern, response, re.IGNORECASE):
                return True

        return False

    def validate_response(self, response):

        if self.contains_sensitive_data(response):
            return False

        return True