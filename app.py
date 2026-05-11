import os
from flask import Flask

app = Flask(__name__)

@app.py.route('/')
def home():
    return "Hello from Secure DevSecOps Project"

if __name__ == "__main__":
    # Fetch settings from environment variables for security
    # Defaults to safe values if variables aren't set
    host = os.environ.get("APP_HOST", "127.0.0.1")
    port = int(os.environ.get("APP_PORT", 5000))
    
    # Debug is strictly False to prevent information leakage
    app.run(host=host, port=port, debug=False)
