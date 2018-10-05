print("printed !")
plaintext = input('write text')
alphabet = "abcdefghijklmnoprstuvyz" 
key = 1
key = int(input("write key"))

cipher = " "

for c in plaintext:
    if c in alphabet: 
        cipher += alphabet[(alphabet.index(c)+key)%len(alphabet)]
print ('merhaba:'+cipher)



