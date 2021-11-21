##Project21: Caeser CipherImproved  version

### Project 21: Caeser Cipher program
##What is Caeser Cipher program??
##It is an ancient type of encription.
#Here the letter in the message will be shifted by certain predetermined amount to get encripted or decripted message

print("Welcome to CAESER CIPHER Game")
import string
alphabets=[letter for letter in string.ascii_lowercase]
print(alphabets)

def encription(user_text,shift, user_input):
    if user_input=='encode':
        encode=[]
        for i in range(0,len(user_text)):
            for j in range(0,len(alphabets)):
                 if user_text[i]==alphabets[j]:
                    #encode.append(alphabets[j+shift])
                    req_shift=j+shift
                    #print('RS:',req_shift)
                    if req_shift>25:
                        req_shift = req_shift-26
                        encode.append(alphabets[req_shift])
                    else:
                        encode.append(alphabets[req_shift])


        encoded_word=""
        for i in encode:
            encoded_word += i
        print("Encoded word:",encoded_word) 

    elif user_input=='decode':
        decode=[]
        for i in range(0,len(user_text)):
            for j in range(0,len(alphabets)):
                if user_text[i]==alphabets[j]:
                    decode.append(alphabets[j-shift])
               

        decoded_word=""
        for i in decode:
            decoded_word += i
        print("Decoded word:",decoded_word) 
    else:
        print("Please enter either encode or decode")



condition_to_run="True"
while condition_to_run=="True":
    user_input=str.lower(input("Type 'encode' for encryption and type 'decode' for decryption:"))
    user_text=str.lower(input("Enter the word for encryption:"))
    shift=int(input("Type the shift number:"))
    #def encode(shift):
    encription(user_text,shift, user_input)
    choice=input("Do you want to re-run the code: Y for YES and N for NO: ")
    
    if choice=='N':
        condition_to_run="False"
print("GOOD BYE")