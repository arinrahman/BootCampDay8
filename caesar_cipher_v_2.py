
def encode(message, shift_num):

    l= list(message)
    for i in range(len(message)):

            if (65 <= ord(l[i]) <= 90) or (97 <= ord(l[i]) <= 122):
                conv = ord(l[i]) + shift_num
                l[i] = chr(conv)


    return ''.join(l)

def decode(message, shift_num):

    l= list(message)
    for i in range(len(message)):
        conv=ord(l[i])- shift_num
        l[i]= chr(conv)
    return ''.join(l)


resp="E"
while resp=="E":

    m= input("Write the word you want to encode.\n")
    n= int(input("Write the shift number you want to use.\n"))
    s= encode(m,n)
    print(f"Encoded message: {s}")

    resp_2= input("Type D to decode. Typing anything else will remove you from the system.\n")
    if resp_2=="D":
        j = decode(s, n)
        print(f"Decoded message: {j}")
    resp = input("Type E to continue encoding. Typing anything else will remove you from the system.\n")