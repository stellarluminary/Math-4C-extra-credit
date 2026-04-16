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

    def test_encrypt_message(self):
        m = Message("LINEAR ALGEBRA IS AWESOME")
        m.numerize_message()
        m.vectorize_numerized_msg()
        em = m.encrypt_message()
        assert em == [
            [43, 107, 102], 
            [45, 96, 79], 
            [23, 47, 36], 
            [13, 38, 41], 
            [35, 89, 90], 
            [-1, 26, 45], 
            [-11, 2, 20], 
            [49, 132, 134], 
            [10, 25, 25]] 

    def test_decrypt_message(self):
        m = Message("LINEAR ALGEBRA IS AWESOME")
        m.numerize_message()
        m.vectorize_numerized_msg()
        m.encrypt_message()
        dm = m.decrypt_message()
        assert dm == [
            [12, 9, 14], 
            [5, 1, 18], 
            [0, 1, 12], 
            [7, 5, 2], 
            [18, 1, 0], 
            [9, 19, 0], 
            [1, 23, 5], 
            [19, 15, 13], 
            [5, 0, 0]
        ]        