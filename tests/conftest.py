import pytest
from algotradingtier0.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instance of main flask app"""
    return create_app()