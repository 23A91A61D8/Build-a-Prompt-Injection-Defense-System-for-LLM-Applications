class SecurityPolicy:

    def __init__(self, level="balanced"):

        # Security level can be: strict or balanced
        self.level = level

    def evaluate_threat(self, threat_type):

        if threat_type is None:
            return "ALLOW"

        if self.level == "strict":

            # In strict mode everything suspicious is blocked
            return "BLOCK"

        elif self.level == "balanced":

            if threat_type in ["PROMPT_INJECTION", "JAILBREAK_ATTACK"]:
                return "BLOCK"

            if threat_type == "PROMPT_LEAK_ATTEMPT":
                return "WARN"

        return "ALLOW"