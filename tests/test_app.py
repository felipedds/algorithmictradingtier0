def test_app_is_created(app):
    assert app.name == "algotradingtier0.app"

def test_config_is_loaded(config):
    assert config["DEBUG"] is False

def test_request_returns_404(client):
    assert client.get("/url_dont_exists").status_code == 404