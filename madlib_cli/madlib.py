from parse import *

#define functions
def read_template(str):
    file = open(str, "r")
    read = file.read()
    file.close()
    return read.strip()

def parse_template(str):

    return

def merge(str, tup):
    return str.format(*tup)

#create program
print("""
*************************************
**      Welcome to Mad Lib         **
**  *****************************  **
**  You will be prompted to enter  **
**  different parts of speech.     **
**  Your answers will be used to   **
**  complete sentences and then    **
**  display them once they are     **
**  complete. This will usually    **
**  create some silly results.     **
**  *****************************  **
**           Have fun!             **
*************************************
""")