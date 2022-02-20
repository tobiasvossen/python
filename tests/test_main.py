from main import welcome


def test_welcome():
    assert "Hello" in welcome()
    assert "!" in welcome()
