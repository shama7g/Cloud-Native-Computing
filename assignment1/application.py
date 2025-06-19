from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# Add "greetings" route
# Read "GREETING" environment variable and return its value
@app.route("/greetings")
def greetings():
    greeting = os.environ.get("GREETING", "No greeting set.")
    return greeting

# Add "listcontents" route
# Read contents of "hostfolder" and return the contents
@app.route("/listcontents")
def list_contents():
    folder_path = "/hostfolder"
    try:
        files = os.listdir(folder_path)
        return jsonify(files)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001) # Change port to 5001
