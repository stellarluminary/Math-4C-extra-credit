import pytest
from message import Message

# @pytest.fixture
# msg = Message("EXPERIENCE")


def test_numerize_message():
    msg = Message("EXPERIENCE")
    assert msg.numerize_message() == [5, 24, 16, 5, 18, 9, 5, 14, 3, 5]

# def test_get_message(monkeypatch):
#     monkeypatch.setattr("main.get_message", lambda _: "HOUSE")
#     m = get_message()
#     assert m == "HOUSE"

# def test_numerize_message():
#     assert numerize_message()
