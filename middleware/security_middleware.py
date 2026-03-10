from middleware.detector import ThreatDetector
from middleware.sanitizer import InputSanitizer
from middleware.validator import OutputValidator
from middleware.logger import SecurityLogger
from middleware.policy import SecurityPolicy


class SecurityMiddleware:

    def __init__(self, policy_level="balanced"):

        self.detector = ThreatDetector()
        self.sanitizer = InputSanitizer()
        self.validator = OutputValidator()
        self.logger = SecurityLogger()
        self.policy = SecurityPolicy(level=policy_level)

    def process_input(self, prompt):

        # Step 1: Sanitize the prompt
        cleaned_prompt = self.sanitizer.clean_prompt(prompt)

        # Step 2: Detect threats
        threat = self.detector.analyze(cleaned_prompt)

        # Step 3: Evaluate security policy
        action = self.policy.evaluate_threat(threat)

        # Step 4: Log security event if needed
        if threat:
            self.logger.log_event(prompt, threat, action)

        return cleaned_prompt, threat, action

    def process_output(self, response):

        # Step 5: Validate output
        if not self.validator.validate_response(response):

            self.logger.log_event(response, "SENSITIVE_OUTPUT", "BLOCK")

            return False

        return True