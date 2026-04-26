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

raw_messages = []
encrypted_messages = []


def create_new(inp):
    msg = Message(inp)
    msg.numerize_message()
    msg.vectorize_numerized_msg()
    raw_messages.append(msg)
    return msg

# def select_message_list():
#     selecting = True
#     while selecting == True:
#         print("User messages enter 1")
#         print("Encrypted messages enter 2")
#         choice = input("1 or 2?")
#         if choice == 1:
#             selecting = False
#             return raw_messages
#         elif choice == 2:
#             selecting = False
#             return encrypted_messages
#         else:
#             print("SORRY, PLEASE ENTER 1 OR 2")

def encrypt(msg):
    msg = msg.encrypt_message()
    return msg

def decrypt(msg):
    msg = msg.decrypt_message()
    msg.translate_decrypted_message()
    return msg

# def save(msg):
#     raw_messages.append(msg)
#     print("SAVED TO MESSAGES")

def view():
    print("SAVED MESSAGES")
    print(raw_messages)

# def quit_program():
#     active = False
#     print("QUIT")
#     return 

def main():
    active = True
    while active:
        print("WELCOME TO THE HILL CIPHER CRYPTOGRAPHY TERMINAL")
        print()
        print("COMMANDS:")
        print()
        print("CREATE NEW")
        print("ENCRYPT")
        print("DECRYPT")
        print("VIEW")
        print("QUIT")
        print()
        user_choice = input("TYPE CHOICE IN ALL CAPS ")
        if user_choice == "CREATE NEW":
            user_message = input("ENTER MESSAGE:")
            msg = create_new(user_message)

        elif user_choice == "ENCRYPT":
            encrypt(msg)
        
        elif user_choice == "DECRYPT":
            decrypt(msg)

        elif user_choice == "VIEW":
            view()

        elif user_choice == "QUIT":
            # quit_program()
            print("THANK YOU FOR USING THE HILL CIPHER CRYPTOGRAPHY TERMINAL")
            active = False

        # msg = Message("LINEAR ALGEBRA IS AWESOME")
        # msg.numerize_message()
        # msg.vectorize_numerized_msg()
        # msg.encrypt_message()
        # msg.decrypt_message()
        # msg.translate_decrypted_message()
        # msg.convert_matrix_to_str()

        # print()
        # print("------------------------")
        # print()
        # m = Message("MAKE SURE TO KNOW THE DEFINITIONS")
        # m.numerize_message()
        # m.vectorize_numerized_msg()
        # m.encrypt_message()
        # m.decrypt_message()
        # m.translate_decrypted_message()
        # m.convert_matrix_to_str()    


if __name__ == "__main__":
    main()