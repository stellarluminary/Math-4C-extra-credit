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
    raw_messages.append(msg.list_of_vectors)
    print("raw_messages in create_new", raw_messages)
    return msg

def select_message_list():
    selecting = True
    chosen_list = []
    while selecting == True:
        print("USER MESSAGES ENTER 1")
        print("ENCRYPTED MESSAGES ENTER 2")
        choice = input("1 or 2? ")
        if choice == "1":
            chosen = raw_messages
            selecting = False
        elif choice == "2":
            chosen = encrypted_messages
            selecting = False
        else:
            print("SORRY, PLEASE ENTER 1 OR 2")
    return chosen_list

def select_message_from_list(lst):
    print("LIST OF MESSAGES:")
    for i in range(len(lst)):
        print(i, lst[i])
    chosen_message_from_list = input("WHICH MESSAGE? ENTER INDEX ")
    return chosen_message_from_list

# def select():
#     chosen = select_message_list()
#     msg = select_message_from_list(chosen)
#     return msg

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
    chosen_list = select_message_list()
    for i in range(len(chosen_list)):
        print(i)

# def quit_program():
#     active = False
#     print("QUIT")
#     return 

def main():
    active = True
    print("WELCOME TO THE HILL CIPHER CRYPTOGRAPHY TERMINAL")
    print()
    while active:
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
            create_new(user_message)

        elif user_choice == "ENCRYPT":
            msg = select_message_from_list(raw_messages)
            encrypt(msg)
        
        elif user_choice == "DECRYPT":
            msg = select_message_from_list(encrypted_messages) 
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