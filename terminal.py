from message import Message

# class Terminal:
# '''
#     Terminal class that serves as the interface/screen that houses the message class.
#     Displays options to encrypt, decrypt, store, and delete messages.

#     Methods:

# '''

#     def __init__(self):
#         print("Welcome to the matrix cryptography terminal. Select from the following options:")
    
#     def create_message(self):
#         Message.get_message()

# def encrypt_message():
#     Message.get_message()


def main():
    print("Welcome to the matrix cryptography terminal. Select from the following options:")
    print()
    print("1 View messages")
    print("2 Enter message to encrypt:")
    print("3 Decrypt message")
    print("Delete message from messages")
    print("Press X to quit")
    print()

    msg = Message("LINEAR ALGEBRA IS SO USEFUL")
    msg.numerize_message()
    msg.vectorize_numerized_msg()
    msg.encrypt_message()
    msg.decrypt_message()
    msg.translate_decrypted_message()
    msg.convert_matrix_to_str()

if __name__ == "__main__":
    main()