# Flask Azure DevOps Sample

Simple Flask app with an Azure DevOps pipeline.

## Endpoints

- / returns a greeting
- /health returns status, uptime, and version
- /info returns app and build metadata

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000/, http://localhost:5000/health, or http://localhost:5000/info.

## Configuration

Set these environment variables to override defaults:

- APP_NAME (default: flask-azure-devops)
- APP_VERSION (default: dev)
- APP_ENV (default: local)
- BUILD_BUILDNUMBER (default: unknown)
- BUILD_SOURCEVERSION (default: unknown)
# devops-demo
