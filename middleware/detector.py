import re


class ThreatDetector:

    def __init__(self):

        # Prompt injection patterns
        self.prompt_injection_patterns = [
            r"ignore .* instructions",
            r"ignore previous instructions",
            r"ignore earlier instructions",
            r"disregard .* instructions",
            r"forget .* instructions",
            r"override .* rules",
            r"bypass .* safety",
            r"disable .* safety",
            r"ignore safeguards",
            r"do anything now",
        ]

        # Jailbreak / roleplay attacks
        self.jailbreak_patterns = [
            r"act as .*",
            r"pretend to be .*",
            r"you are now .*",
            r"roleplay .*",
            r"simulate .*",
            r"unrestricted .* assistant",
            r"evil assistant",
            r"malicious ai",
        ]

        # Prompt leakage attempts
        self.prompt_leak_patterns = [
            r"system prompt",
            r"hidden instructions",
            r"internal instructions",
            r"internal prompt",
            r"show .* prompt",
            r"print .* prompt",
            r"secret system prompt",
            r"system message",
        ]

    def detect_prompt_injection(self, prompt):

        for pattern in self.prompt_injection_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                return "PROMPT_INJECTION"

        return None

    def detect_jailbreak(self, prompt):

        for pattern in self.jailbreak_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                return "JAILBREAK_ATTACK"

        return None

    def detect_prompt_leak(self, prompt):

        for pattern in self.prompt_leak_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                return "PROMPT_LEAK_ATTEMPT"

        return None

    def analyze(self, prompt):

        threat = self.detect_prompt_injection(prompt)

        if threat:
            return threat

        threat = self.detect_jailbreak(prompt)

        if threat:
            return threat

        threat = self.detect_prompt_leak(prompt)

        if threat:
            return threat

        return None