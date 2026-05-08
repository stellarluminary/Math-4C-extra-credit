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
msg_objects = []
# raw_messages = []
# cipher_messages = []
encrypted_messages = []


def create_new(inp):
    msg = Message(inp)
    msg.numerize_message()
    msg.vectorize_numerized_msg()
    msg_objects.append(msg)
    # raw_messages.append(msg.msg)
    # cipher_messages.append(msg.list_of_vectors)
    # print("raw_messages in create_new", raw_messages)
    # print("cipher messages in create_new", cipher_messages)
    return msg

def select_message_list_to_view():
    selecting = True
    chosen_list = []
    while selecting == True:
        print("USER MESSAGES ENTER 0")
        print("NUMERIZED MESSAGES ENTER 1")
        print("ENCRYPTED MESSAGES ENTER 2")
        print()
        choice = input("0, 1, OR 2? ")
        if choice == "0":
            chosen_list = [ m.msg for m in msg_objects ]
            selecting = False
        elif choice == "1":
            # chosen_list = cipher_messages
            chosen_list = [ m.list_of_vectors for m in msg_objects ]
            selecting = False
        elif choice == "2":
            # chosen_list = encrypted_messages
            chosen_list = [ m.encrypted_list_of_vectors for m in msg_objects ]
            selecting = False
        else:
            print("SORRY, PLEASE ENTER 0, 1, OR 2")
    # print("Your chosen list: ", chosen_list)
    return chosen_list

def select_message_for_processing(choice):
    print("LIST OF MESSAGES:")
    print()
    if choice == 1:
        # If the user chooses to encrypt
        for i in range(len(msg_objects)):
            print(i, msg_objects[i].msg)
        print()
    else:
        # If the user chooses to decrypt
        for i in range(len(msg_objects)):
            print(i, msg_objects[i].encrypted_list_of_vectors)
        print()        
    msg_obj_idx = int(input("WHICH MESSAGE? ENTER INDEX "))
    return msg_obj_idx


def encrypt(msg_obj_idx):
    # print("encrypt function: msg_objects[msg_obj_idx]", msg_objects[msg_obj_idx])
    msg = msg_objects[msg_obj_idx].encrypt_message()
    print("MESSAGE ENCRYPTED:", msg_objects[msg_obj_idx].encrypted_list_of_vectors)
    encrypted_messages.append(msg)
    return msg

def decrypt(msg_obj_idx):
    msg_objects[msg_obj_idx].decrypt_message()
    msg = msg_objects[msg_obj_idx].translate_decrypted_message()
    return msg


def view():
    chosen_list = select_message_list_to_view()
    for i in range(len(chosen_list)):
        print()
        print(chosen_list[i])


def main():
    active = True
    print("WELCOME TO THE HILL CIPHER CRYPTOGRAPHY TERMINAL")
    print()
    while active:
        print("OPTIONS:")
        print()
        print("CREATE NEW")
        print("ENCRYPT")
        print("DECRYPT")
        print("VIEW")
        print("QUIT")
        print()
        user_choice = input("TYPE CHOICE IN ALL CAPS ")
        print()
        if user_choice == "CREATE NEW":
            user_message = input("ENTER MESSAGE IN ALL CAPS AND NO PUNCTUATION: ")
            create_new(user_message)
            print()

        elif user_choice == "ENCRYPT":
            msg_obj_idx = select_message_for_processing(1)
            encrypt(msg_obj_idx)
            print()
        
        elif user_choice == "DECRYPT":
            msg_obj_idx = select_message_for_processing(2) 
            decrypt(msg_obj_idx)
            print()

        elif user_choice == "VIEW":
            view()
            print()

        elif user_choice == "QUIT":
            print("THANK YOU FOR USING THE HILL CIPHER CRYPTOGRAPHY TERMINAL")
            print()
            active = False


if __name__ == "__main__":
    main()
