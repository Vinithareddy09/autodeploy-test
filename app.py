from flask import Flask
import sys
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>🚀 AutoDeploy Test Successful!</h2><p>Hello from Vinitha’s Flask App 👋</p>"

if __name__ == "__main__":
    # Default port
    port = 5000

    # 1️⃣ Check if user passed --port argument (e.g. python app.py --port 5050 or --port=5050)
    for arg in sys.argv:
        if arg.startswith("--port"):
            try:
                if "=" in arg:
                    port = int(arg.split("=")[1])
                else:
                    port = int(sys.argv[sys.argv.index(arg) + 1])
            except (IndexError, ValueError):
                print("⚠️ Invalid port argument, using default 5000")

    # 2️⃣ If no --port given, check environment variable (useful for Render/Ngrok/etc.)
    port = int(os.environ.get("PORT", port))

    print(f"✅ Starting Flask app on port {port} ...")
    app.run(host="0.0.0.0", port=port)
