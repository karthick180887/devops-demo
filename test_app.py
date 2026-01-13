import platform

from app import create_app


def test_index():
    app = create_app()
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello from Flask on Azure DevOps!" in resp.data


def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
    assert isinstance(data["uptime_seconds"], int)
    assert data["uptime_seconds"] >= 0
    assert isinstance(data["version"], str)


def test_info(monkeypatch):
    monkeypatch.delenv("APP_NAME", raising=False)
    monkeypatch.delenv("APP_VERSION", raising=False)
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("BUILD_BUILDNUMBER", raising=False)
    monkeypatch.delenv("BUILD_SOURCEVERSION", raising=False)

    app = create_app()
    client = app.test_client()
    resp = client.get("/info")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["name"] == "flask-azure-devops"
    assert data["version"] == "dev"
    assert data["environment"] == "local"
    assert data["python"] == platform.python_version()
    assert data["build_number"] == "unknown"
    assert data["commit_sha"] == "unknown"


def test_info_overrides(monkeypatch):
    monkeypatch.setenv("APP_NAME", "demo")
    monkeypatch.setenv("APP_VERSION", "1.2.3")
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("BUILD_BUILDNUMBER", "42")
    monkeypatch.setenv("BUILD_SOURCEVERSION", "abcdef")

    app = create_app()
    client = app.test_client()
    resp = client.get("/info")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["name"] == "demo"
    assert data["version"] == "1.2.3"
    assert data["environment"] == "test"
    assert data["build_number"] == "42"
    assert data["commit_sha"] == "abcdef"
