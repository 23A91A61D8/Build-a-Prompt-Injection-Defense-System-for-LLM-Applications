import logging
import os
from datetime import datetime


class SecurityLogger:

    def __init__(self):

        log_directory = "logs"
        log_file = os.path.join(log_directory, "security.log")

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
        )

    def log_event(self, prompt, threat_type, action):

        message = f"PROMPT: {prompt} | THREAT: {threat_type} | ACTION: {action}"

        logging.info(message)