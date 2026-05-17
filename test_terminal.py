import pytest
import terminal
from message import Message

@pytest.fixture
def msg_1():
    return terminal.create_new("HAVE A GREAT SUMMER")

@pytest.fixture
def msg_2():
    return terminal.create_new("SEE YOU IN THE FALL")

# @pytest.mark.parametrize(
#         "input, vectorized, encrypted, decrypted",
#         [
#             ("HAVE A GREAT SUMMER", 
#              [8, 1, 22, 5, 0, 1, 0, 7, 18, 5, 1, 20, 0, 19, 21, 13, 13, 5, 18],
#              [[59, 127, 106], [12, 29, 28], [29, 65, 54], [49, 104, 85], [23, 65, 63], [23, 72, 80], [36, 90, 90]],
#               [['H', 'A', 'V'], ['E', ' ', 'A'], [' ', 'G', 'R'], ['E', 'A', 'T'], [' ', 'S', 'U'], ['M', 'M', 'E'], ['R', ' ', ' ']]
#              ),
#             ("GOOD LUCK WITH FINALS",
#              [7, 15, 15, 4, 0, 12, 21, 3, 11, 0, 23, 9, 20, 8, 0, 6, 9, 14, 1, 12, 19],
#              [[29, 80, 80], [32, 68, 56], [61, 146, 138], [-5, 13, 27], [32, 92, 100], [31, 77, 72], [28, 69, 62]],
#             [['G', 'O', 'O'], ['D', ' ', 'L'], ['U', 'C', 'K'], [' ', 'W', 'I'], ['T', 'H', ' '], ['F', 'I', 'N'], ['A', 'L', 'S']]
#              ),
#             ("LINEAR ALGEBRA IS SO USEFUL",
#              [12, 9, 14, 5, 1, 18, 0, 1, 12, 7, 5, 2, 18, 1, 0, 9, 19, 0, 19, 15, 0, 21, 19, 5, 6, 21, 12],
#              [[43, 107, 102], [45, 96, 79], [23, 47, 36], [13, 38, 41], [35, 89, 90], [-1, 26, 45], [23, 80, 95], [33, 106, 120], [15, 57, 66]],
#             [['L', 'I', 'N'], ['E', 'A', 'R'], [' ', 'A', 'L'], ['G', 'E', 'B'], ['R', 'A', ' '], ['I', 'S', ' '], ['S', 'O', ' '], ['U', 'S', 'E'], ['F', 'U', 'L']]
#              ),
#             ("SEE YOU IN THE FALL",
#              [19, 5, 5, 0, 25, 15, 21, 0, 9, 14, 0, 20, 8, 5, 0, 6, 1, 12, 12],
#              [[43, 110, 110], [5, 35, 45], [60, 141, 132], [68, 150, 130], [11, 35, 40], [35, 77, 66], [24, 60, 60]],
#              [['S', 'E', 'E'], [' ', 'Y', 'O'], ['U', ' ', 'I'], ['N', ' ', 'T'], ['H', 'E', ' '], ['F', 'A', 'L'], ['L', ' ', ' ']]
#              ),
#         ],
# )

def test_create_new(msg_1, msg_2):
    assert msg_1.msg == "HAVE A GREAT SUMMER"
    assert msg_2.msg == "SEE YOU IN THE FALL"

def test_encrypt(msg_1, msg_2):
    msg_1.encrypt_message()
    terminal.encrypt(0)
    msg_2.encrypt_message()
    terminal.encrypt(1)
    assert msg_1.encrypted_list_of_vectors == terminal.encrypted_messages[0]
    assert msg_2.encrypted_list_of_vectors == terminal.encrypted_messages[1]

def test_decrypt(msg_1,msg_2):
    msg_1.encrypt_message()
    msg_1.decrypt_message()
    msg_1.translate_decrypted_message()
    assert msg_1.translated_message == terminal.decrypt(0)

    msg_2.encrypt_message()
    msg_2.decrypt_message()
    msg_2.translate_decrypted_message() 
    assert msg_2.translated_message == terminal.decrypt(1)

# def test_create_new():
#     terminal.create_new("HAVE A GREAT SUMMER")
#     assert terminal.msg_objects[0].msg == "HAVE A GREAT SUMMER"
