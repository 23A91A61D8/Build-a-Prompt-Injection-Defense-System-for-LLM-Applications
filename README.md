# Build-a-Prompt-Injection-Defense-System-for-LLM-Applications

## Overview

Large Language Models (LLMs) are widely used in modern applications but are vulnerable to adversarial attacks such as prompt injection, jailbreak attempts, and prompt leakage. These attacks can manipulate the model’s behavior and potentially expose sensitive information.

This project implements a **Prompt Injection Defense System** designed as a reusable **security middleware** that protects LLM-powered applications from malicious prompts. The system analyzes and sanitizes user inputs, detects attack patterns, validates model outputs, and logs security events.

The system follows a **Defense-in-Depth architecture**, where multiple security layers work together to ensure robust protection against adversarial attacks.

---

## Key Features

- Prompt Injection Detection
- Jailbreak Attack Detection
- Prompt Leakage Protection
- Input Sanitization Pipeline
- Output Validation for Sensitive Data
- Configurable Security Policies (Strict / Balanced)
- Structured Security Logging
- Automated Attack Test Suite
- Example Flask Application Demonstrating Integration

---

## System Architecture

The system uses a layered security architecture:

User Prompt  
↓  
Input Sanitization  
↓  
Threat Detection Engine  
↓  
Security Policy Evaluation  
↓  
Security Logging  
↓  
LLM Processing  
↓  
Output Validation  
↓  
Safe Response to User  

This layered approach ensures malicious prompts are detected and blocked before they reach the LLM.

---

## Project Structure
Prompt-Injection-Defense-System-for-LLM-Applications
│
├── middleware
│ ├── detector.py
│ ├── sanitizer.py
│ ├── validator.py
│ ├── logger.py
│ ├── policy.py
│ └── security_middleware.py
│
├── app
│ └── example_app.py
│
├── tests
│ ├── malicious_prompts.txt
│ ├── benign_prompts.txt
│ └── test_runner.py
│
├── logs
│
├── requirements.txt
├── README.md
└── EVALUATION.md


---

## Security Components

### Threat Detection

The threat detection module identifies malicious patterns including:

- Prompt injection attacks  
- Jailbreak attempts  
- Role-playing attacks  
- System prompt leakage requests  

Implemented in:


middleware/detector.py


---

### Input Sanitization

The input sanitizer cleans user prompts before they are sent to the LLM.

Functions include:

- Removing malicious instructions  
- Normalizing input text  
- Filtering dangerous patterns  

Implemented in:


middleware/sanitizer.py


---

### Output Validation

The output validator prevents sensitive information from leaking through LLM responses.

Detects:

- API keys  
- Passwords  
- Secret tokens  
- Email addresses  
- Phone numbers  

Implemented in:


middleware/validator.py


---

### Security Policy Engine

The system supports configurable security levels.

Available modes:

**Strict Mode**
- Blocks all suspicious prompts

**Balanced Mode**
- Allows legitimate prompts while blocking malicious prompts

Implemented in:


middleware/policy.py


---

### Security Logging

All security events are logged with:

- Timestamp  
- Original prompt  
- Threat type  
- Action taken  

Logs are stored in:


logs/security.log


---

## Installation

Clone the repository:


git clone <repository-url>
cd Prompt-Injection-Defense-System-for-LLM-Applications


Create a virtual environment:


python -m venv venv


Activate the virtual environment.

For Windows PowerShell:


venv\Scripts\Activate.ps1


Install dependencies:


pip install -r requirements.txt


---

## Running the Example Application

Start the Flask API server:


python -m app.example_app


The server will run at:


http://127.0.0.1:5000


Example API endpoint:


POST /chat


Example request body:


{
"prompt": "Explain machine learning"
}


---

## Running the Test Suite

The project includes an automated test suite for evaluating attack detection performance.

Run the test suite:


python -m tests.test_runner


The test runner evaluates:

- Attack detection rate
- False positive rate

---

## Example Evaluation Results

Example output from the test suite:

Malicious Prompt Test

Total Attacks: 20
Detected Attacks: 18
Detection Rate: 90.00%

Benign Prompt Test

Total Prompts: 10
False Positives: 0
False Positive Rate: 0.00%


These results demonstrate that the system effectively detects malicious prompts while allowing legitimate user queries.

---

## Technologies Used

- Python
- Flask
- Regular Expressions
- AI Security Concepts
- Modular Middleware Architecture

---

## Future Improvements

Potential enhancements include:

- Integration with real LLM APIs
- Machine learning-based attack detection
- Semantic analysis for advanced prompt injection detection
- Integration with enterprise AI security monitoring systems

---

## Conclusion

This project demonstrates a modular and practical approach to securing LLM-powered applications against prompt injection and adversarial manipulation. By combining threat detection, input sanitization, output validation, configurable security policies, and logging, the system provides a robust defense layer that can be integrated into real-world AI systems.
