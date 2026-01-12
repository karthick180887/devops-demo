from flask import Flask, jsonify
import os


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello from Flask on Azure DevOps!", 200

    @app.route("/health")
    def health():
        return jsonify(status="ok"), 200

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
