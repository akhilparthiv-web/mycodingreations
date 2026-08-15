#the menu
def option():
    print("\n 1. Encrypt \n"
          "\n 2. Decrypt with key \n"
          "\n 3. Decrypt with brute force \n"
          "\n 4. Quit \n"
          )
    while True:
        upick = input('')
        if upick.isnumeric():   
            if (int(upick) <= 4) and (int(upick) >= 1):
                break
            else:
                upick = 'please enter valid option'
        else:
            upick = 'please enter valid option'
    return upick
    
    
    



#option 1 encryption
def encrypt():
    umess = input('what is you message? ')
    encrypted = ""
    ukey = input('what is the key?(1-25)  ')
    if ukey.isnumeric():
        ukey = int(ukey)
        for letter in umess:
            if letter.islower() is True: #lower separation
                aletter = ord(letter)
                if aletter + ukey > 122: #overboard protection
                    aletter = ((aletter - 26) + ukey)
                    eletter = chr(aletter)
                else:
                    eletter = chr(aletter + ukey) #normal lowercase letter
            elif letter.isupper() is True: #upper separtion\
                aletter = ord(letter)
                if aletter + ukey > 90: 
                    aletter = (aletter - 26) + ukey
                    eletter = chr(aletter)
                else:
                    aletter = aletter + ukey
                    eletter = chr(aletter)
                
            else:
                eletter = letter
            encrypted += eletter
    else:
        print('please enter valid key')
    return encrypted


def decrypt():
    de = ""
    emess = input('what is the message? ')
    key = input('what is the key? ')
    if key.isnumeric():
            key = int(key)
    else:
        return('enter good key')
    for letter in emess:
        if letter.islower():
            shifted = ord(letter) - 97
            new_shifted = (shifted - key) % 26
            dletter = chr(new_shifted + 97)
            de = de + dletter
        elif letter.isupper():
            shifted = ord(letter) - 65
            new_shifted = (shifted - key) % 26
            dletter = chr(new_shifted + 65)
            de = de + dletter
        else:
            de = de + letter
    return de
            
def decrypt_brute():
    emess = input('what is the message? ')
    for key in range(1, 26):
        de = ""
        for letter in emess:
            if letter.islower():
                shifted = ord(letter) - 97
                new_shifted = (shifted - key) % 26
                dletter = chr(new_shifted + 97)
                de = de + dletter
            
            elif letter.isupper():
                shifted = ord(letter) - 65
                new_shifted = (shifted - key) % 26
                dletter = chr(new_shifted + 65)
                
                de = de + dletter
            else:
                de = de + letter
        return f"key {key}: {de}"
    
while True:
    user_choice = int(option())

    if user_choice == 1:
        print(encrypt())
    elif user_choice == 2:
        print(decrypt())
    elif user_choice == 3:
        print(decrypt_brute())
    elif user_choice == 4:
        print("BYE")
        break

    else:
        print('not now coming soon')
