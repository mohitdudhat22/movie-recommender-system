import subprocess
import os

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Streamlit app is running."

@app.route("/streamlit")
def run_streamlit():
    subprocess.Popen(["streamlit", "run", "app.py", "--server.port", "8501", "--server.headless", "true"])
    return "Streamlit started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
