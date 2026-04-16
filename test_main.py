import pytest
from message import Message

# @pytest.fixture
# msg = Message("EXPERIENCE")

class TestMessage:

    def test_numerize_message(self):
        m = Message("EXPERIENCE")
        nm = m.numerize_message()
        assert nm == [5, 24, 16, 5, 18, 9, 5, 14, 3, 5]

    def test_vectorize_numerized_msg(self):
        m = Message("LINEAR ALGEBRA")
        m.numerize_message()
        vm = m.vectorize_numerized_msg()
        assert vm ==  [[12, 9, 14], [5, 1, 18], [0, 1, 12], [7, 5, 2], [18, 1, 0]]


