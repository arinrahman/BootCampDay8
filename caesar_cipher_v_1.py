
def encode(message, shift_num):

    l= list(message)
    for i in range(len(message)):
        conv=ord(l[i])+ shift_num
        l[i]= chr(conv)
    return ''.join(l)

def decode(message, shift_num):

    l= list(message)
    for i in range(len(message)):
        conv=ord(l[i])- shift_num
        l[i]= chr(conv)
    return ''.join(l)
def check_alpha(a):

    for value in a:
        if not ((65 <= ord(value) <= 90) or (97 <= ord(value) <= 122)):  # Check A-Z or a-z
            return 1  # Found a non-alphabet character
    return 0  # All characters are alphabetic



resp="E"
while resp=="E":

    m= input("Write the word you want to encode.\n")
    c=check_alpha(m)
    if c==1:
        print("Warning: Invalid input. Type alphabetic inputs only.")
        continue
    n= int(input("Write the shift number you want to use.\n"))
    s= encode(m,n)
    print(f"Encoded message: {s}")

    resp_2= input("Type D to decode. Typing anything else will remove you from the system.\n")
    if resp_2=="D":
        j = decode(s, n)
        print(f"Decoded message: {j}")
    resp = input("Type E to continue encoding. Typing anything else will remove you from the system.\n")



