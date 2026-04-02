import numpy

def main():

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


    def get_message():
        msg = input("TYPE YOUR MESSAGE IN ALL CAPS WITH NO PUNCTUATION: ")
        return msg

    def numerize_message(msg):

        numerized_msg = []

        for letter in msg:
            for k,v in key.items():
                if letter == k:
                    numerized_msg.append(v)
        # print("numerized message:", numerized_msg)
        return numerized_msg


    def vectorize_numerized_msg(numerized_msg):
        # print("Turn numerized message into a list of 1x3 vectors.")
        list_of_vectors = []
        # length_of_numerized_msg = len(numerized_msg)

        # for i in range(0, length_of_numerized_msg, 3):
        while len(numerized_msg) > 0:
            # Steps through every three numbers in numerized_msg
            # print(numerized_msg[i])
            vector = []
            vector.append(numerized_msg.pop(0))
            if len(numerized_msg) == 0:
                vector.append(0)
                vector.append(0)
                # print("vector (1st if)", vector)
                
            elif len(numerized_msg) == 1:
                vector.append(numerized_msg.pop(0))
                vector.append(0)
                # print("vector (2nd if)", vector)
                
            else:
                vector.append(numerized_msg.pop(0))
                vector.append(numerized_msg.pop(0))
            list_of_vectors.append(vector)

            
        # print("empty numerized_msg", numerized_msg)
        # print("final list of vectors", list_of_vectors)
        return list_of_vectors


    def encrypt_message(list_of_vectors):
        '''
        Encrypt the numerized and vectorized input text using the encryption_matrix.
        '''
        encrypted_list_of_vectors = []
        for i in range(len(list_of_vectors)):
            vector = []
            # encrypted_list_of_vectors.append(numpy.dot(encryption_matrix, i))
            # print("i:", i)
            # print(list_of_vectors[i][0])
            # print(list_of_vectors[i][1])
            # print(list_of_vectors[i][2])

            for j in range(len(encryption_matrix)):
                # print("index j of encryption_matrix:", j)
                num = (list_of_vectors[i][0] * encryption_matrix[0][j]) + \
                    (list_of_vectors[i][1] * encryption_matrix[1][j]) + \
                    (list_of_vectors[i][2] * encryption_matrix[2][j])
                vector.append(num)

            encrypted_list_of_vectors.append(vector)

        print("encrypted_list_of_vectors", encrypted_list_of_vectors)
        return encrypted_list_of_vectors

    def decrypt_message(encrypted_list_of_vectors):
        # print("Decrypting message . . .")
        decrypted_list_of_vectors = []
    
        for i in range(len(encrypted_list_of_vectors)):
            vector = []
            # print("i:", i)
            # print(encrypted_list_of_vectors[i][0])
            # print(encrypted_list_of_vectors[i][1])
            # print(encrypted_list_of_vectors[i][2])

            for j in range(len(decryption_matrix)):
                # print("index j of decryption matrix:", j)
                num = (encrypted_list_of_vectors[i][0] * decryption_matrix[0][j]) + \
                    (encrypted_list_of_vectors[i][1] * decryption_matrix[1][j]) + \
                    (encrypted_list_of_vectors[i][2] * decryption_matrix[2][j])
                vector.append(num)

            decrypted_list_of_vectors.append(vector)

        # print("decrypted_list_of_vectors", decrypted_list_of_vectors)
        return decrypted_list_of_vectors
    
    def translate_decrypted_message(decrypted_list_of_vectors):
        translated_message = []
        for i in range(len(decrypted_list_of_vectors)):
            vector = []
            for j in range(len(decrypted_list_of_vectors[i])):
                for k,v in key.items():
                    if decrypted_list_of_vectors[i][j] == key[k]:
                        vector.append(k)
            translated_message.append(vector)
        # print("Decrypted message:", translated_message)
        return translated_message

    def convert_matrix_to_str(translated_message):
        text = ""
        for i in range(len(translated_message)):
            for j in range(len(translated_message[i])):
                text += translated_message[i][j]
        print("Decrypted message:", text)


    msg = get_message()
    numerized_msg = numerize_message(msg)
    list_of_vectors = vectorize_numerized_msg(numerized_msg)
    encrypted_list_of_vectors = encrypt_message(list_of_vectors)
    decrypted_list_of_vectors = decrypt_message(encrypted_list_of_vectors)
    translated_message = translate_decrypted_message(decrypted_list_of_vectors)
    text = convert_matrix_to_str(translated_message)

if __name__ == "__main__":
    main()