from flask import Flask
import socket
import os

app = Flask(__name__)

def find_free_port(default_port=5000):
    """Find a free port automatically."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()
    return port

@app.route("/")
def home():
    return """
        <h2>🚀 AutoDeploy Test Successful!</h2>
        <p>Hello from Vinitha’s Flask App 👋</p>
        <p>✅ Flask is running successfully with automatic port detection.</p>
    """

if __name__ == "__main__":
    port = find_free_port()
    print(f"\n✅ Starting Flask app on port {port} ...")
    print(f"🌍 Access via ngrok: http://localhost:{port}\n")
    app.run(host="0.0.0.0", port=port)
