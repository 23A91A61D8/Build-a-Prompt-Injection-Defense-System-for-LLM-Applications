import re


class InputSanitizer:

    def __init__(self):

        # patterns that should be removed from user input
        self.dangerous_patterns = [
            r"ignore (all )?previous instructions",
            r"disregard previous instructions",
            r"forget your instructions",
            r"override rules",
            r"bypass safety",
            r"disable safety",
        ]

    def clean_prompt(self, prompt):

        # Remove leading and trailing spaces
        prompt = prompt.strip()

        # Remove dangerous patterns
        for pattern in self.dangerous_patterns:
            prompt = re.sub(pattern, "", prompt, flags=re.IGNORECASE)

        # Remove suspicious symbols
        prompt = re.sub(r"[<>]", "", prompt)

        # Normalize multiple spaces
        prompt = re.sub(r"\s+", " ", prompt)

        return prompt