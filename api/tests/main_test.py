from main import get_request


def test_valid_message():
    """Tests that a valid message input returns a valid response"""
    response = get_request("Hello")
    assert response == "Hi there!"
