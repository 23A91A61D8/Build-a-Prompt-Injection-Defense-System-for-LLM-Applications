from flask import Flask, request, jsonify

from middleware.security_middleware import SecurityMiddleware

app = Flask(__name__)

# Initialize security middleware
security = SecurityMiddleware(policy_level="balanced")


# Fake LLM function (for demonstration)
def call_llm(prompt):

    # In real systems this would call an actual LLM
    return f"LLM Response: {prompt}"


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    if not data or "prompt" not in data:
        return jsonify({"error": "Prompt is required"}), 400

    user_prompt = data["prompt"]

    # Pass prompt through security middleware
    cleaned_prompt, threat, action = security.process_input(user_prompt)

    if action == "BLOCK":

        return jsonify({
            "status": "blocked",
            "reason": threat
        })

    # Call LLM with sanitized prompt
    llm_response = call_llm(cleaned_prompt)

    # Validate LLM output
    output_safe = security.process_output(llm_response)

    if not output_safe:

        return jsonify({
            "status": "blocked",
            "reason": "Sensitive information detected"
        })

    return jsonify({
        "status": "success",
        "response": llm_response
    })


if __name__ == "__main__":
    app.run(debug=True)