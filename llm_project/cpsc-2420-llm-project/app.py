"""This will house the backend of the application"""

from flask import Flask, request, Response
from inference import run_inference
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
"""This route will act as an api endpoint for the login page"""

@app.route("/api/prompt-response")
def api_login():
    prompt = request.args.get("prompt")
    response = run_inference(prompt)
    return {"Response" : response}

