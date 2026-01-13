import platform
import os
import time
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)
    app.config["START_TIME"] = time.monotonic()
    app.config["APP_NAME"] = os.environ.get("APP_NAME", "flask-azure-devops")
    app.config["APP_VERSION"] = os.environ.get("APP_VERSION", "dev")
    app.config["ENVIRONMENT"] = os.environ.get("APP_ENV", "local")
    app.config["BUILD_NUMBER"] = os.environ.get("BUILD_BUILDNUMBER", "unknown")
    app.config["COMMIT_SHA"] = os.environ.get("BUILD_SOURCEVERSION", "unknown")

    @app.route("/")
    def index():
        return "Hello from Flask on Azure DevOps!", 200

    @app.route("/health")
    def health():
        uptime_seconds = int(time.monotonic() - app.config["START_TIME"])
        return (
            jsonify(
                status="ok",
                uptime_seconds=uptime_seconds,
                version=app.config["APP_VERSION"],
            ),
            200,
        )

    @app.route("/info")
    def info():
        return (
            jsonify(
                name=app.config["APP_NAME"],
                version=app.config["APP_VERSION"],
                environment=app.config["ENVIRONMENT"],
                python=platform.python_version(),
                build_number=app.config["BUILD_NUMBER"],
                commit_sha=app.config["COMMIT_SHA"],
            ),
            200,
        )

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
