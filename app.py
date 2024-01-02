from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! My name is Anmol Kumar Singh and my USN is 1BM20IS196."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
