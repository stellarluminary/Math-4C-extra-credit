# Math-4C-extra-credit
My extra credit project for Mission College's Math 4C (Linear Algebra) class. This repo also contains a refacotored version of the program for Mission College's EGR 10 Honors project. 

The extra credit project for Math 4C is housed in `main.py`. This program is an implementation of the Hill Cipher. It takes a user-inputted string and encodes and decodes it using a square matrix and its inverse.

To run this program, clone this project to your local machine.

Run the following command:

`python main.py`

The program will prompt you to enter a text string in all capital letters and no punctuation.

The Honors project version of this program is more interactive and allows the user to CREATE NEW, ENCRYPT, DECRYPT, AND VIEW messages. A user can also choose to exit the program if they enter QUIT.

To run this program, run the following command:

`python terminal.py`

This version of the program does have flaws. Current issues to be resolved are:

- program does not accept lowercase letters or punctuation
- numerized and encrypted messages in `terminal.py` are decoupled from their Message instance 
- program does not have unit tests
