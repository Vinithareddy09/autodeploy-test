from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>🚀 AutoDeploy Test Successful!</h2><p>Hello from Vinitha’s Flask App 👋</p>"

def find_free_port(preferred_ports=[5000, 5050, 6000, 7000]):
    """Finds the first available port from the list."""
    for port in preferred_ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("0.0.0.0", port)) != 0:
                return port
    # if all are taken, pick a random available one
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 0))
    free_port = s.getsockname()[1]
    s.close()
    return free_port

if __name__ == "__main__":
    port = find_free_port()
    print(f"✅ Starting Flask app on port {port} ...")
    app.run(host="0.0.0.0", port=port)
