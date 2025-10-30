from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>🚀 AutoDeploy Test Successful!</h2><p>Hello from Vinitha’s Flask App 👋</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
