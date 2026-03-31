import numpy

encryption_matrix = [
    [2,5,5],
    [-1,-1,0],
    [2,4,3]
]

decryption_matrix = [
    [3,-5,-5],
    [-3,4,5],
    [2,-2,-3]
]

key = {" ":0, "A":1, "B":2,"C":3, "D":4, "E":5, "F": 6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15,\
       'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

# msg = "EXPERIENCE"

# for k,v in key.items():
#     if v == 24:
#         print(k)
#     else:
#         print("Not X")

def encrypt_message():
    # print("message in encrypt message function:", msg)
    msg = input("TYPE YOUR MESSAGE IN ALL CAPS: ")
    # print("Message:", msg)

    encrypted_msg = []

    for letter in msg:
        for k,v in key.items():
            if letter == k:
               encrypted_msg.append(v)
                # print(v)
    # print("encrypted message:", encrypted_msg)
    return encrypted_msg

def vectorize_encrypted_msg(encrypted_msg):
    print("Turn encrypted message into a list of 3x1 vectors.")
    list_of_vectors = []
    # length_of_encrypted_msg = len(encrypted_msg)

    # for i in range(0, length_of_encrypted_msg, 3):
    while len(encrypted_msg) > 0:
        # Steps through every three numbers in encrypted_msg
        # print(encrypted_msg[i])
        vector = []
        vector.append(encrypted_msg.pop(0))
        if len(encrypted_msg) == 0:
            vector.append(0)
            vector.append(0)
            print("vector (1st if)", vector)
            
        elif len(encrypted_msg) == 1:
            vector.append(encrypted_msg.pop(0))
            vector.append(0)
            print("vector (2nd if)", vector)
            
        else:
            vector.append(encrypted_msg.pop(0))
            vector.append(encrypted_msg.pop(0))
        list_of_vectors.append(vector)

        
    print("empty encrypted_msg", encrypted_msg)
    print("final list of vectors", list_of_vectors)


    # while len(encrypted_msg) > 0:
    #     vector = []
    #     if len(encrypted_msg) % 3 == 1:
    #         vector.append(encrypted_msg.pop(0))
    #         vector.append(0)
    #         vector.append(0)
    #         list_of_vectors.append(vector)
    #     elif len(encrypted_msg) % 3 == 2:
    #         vector.append(encrypted_msg.pop(0))
    #         vector.append(encrypted_msg.pop(0))
    #         vector.append(0)
    #         list_of_vectors.append(vector)
    #     elif len(encrypted_msg) % 3 == 0:
    #         vector.append(encrypted_msg.pop(0))
    #         vector.append(encrypted_msg.pop(0))
    #         vector.append(encrypted_msg.pop(0))
    #         list_of_vectors.append(vector)
    # print("encrypted_msg", encrypted_msg)
    # print("list of vectors", list_of_vectors)




def decrypt_message():
    print("Decrypting message . . .")

encrypted_msg = encrypt_message()
vectorize_encrypted_msg(encrypted_msg)