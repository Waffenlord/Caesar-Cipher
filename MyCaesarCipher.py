
ALL_SIGNS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789!¡%&+-*/'
MAX_KEY_NUM = len(ALL_SIGNS) - 1

def get_mode():
    print('Welcome to Caesar Cipher do you want to encrypt, decrypt or brute-force a message?')
    while True:      
        mode = input().lower()
        if mode in ['decrypt', 'd', 'encrypt', 'e' ,'brute', 'b']:
            return mode
        else:
            print('Please selecte decrypt, encrypt or brute')
            continue

def get_key():
    key = 0
    print(f'Please select the key you want to use to encrypt or decrypt (1 - {MAX_KEY_NUM})')
    while True:
        try:
            key = int(input())
        except:
            print('Please type a number')
            continue
        if key >= 1 and key <= MAX_KEY_NUM:
            return key
        else:
            print('Type a number within the range')
            continue

def get_message():
    print('Please type your message: ')
    return input()

def get_translated_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for sign in message:
        signIndex = ALL_SIGNS.find(sign)
        if signIndex == -1:
            translated += sign
        else:
            signIndex += key
    
            if signIndex >= MAX_KEY_NUM:
                signIndex -= len(ALL_SIGNS)
            elif signIndex < 0:
                signIndex += len(ALL_SIGNS)
           
            translated += ALL_SIGNS[signIndex]
        
    return translated

def restart():
    print('Do you want to perform another action? (yes or no)')
    r = input().lower()
    if r.startswith('y'):
        return True
    else:
        print('Thank you for using my cipher!')
        return False


running = True
while running:
    mode = get_mode()
    message = get_message()
    if mode[0] != 'b':
        key = get_key()
        print('Your translate message is: ')
        print(get_translated_message(mode, message, key))
        running = restart()
    else:
        for key in range(1 , MAX_KEY_NUM + 1):
            print(get_translated_message('decrypt', message, key))
        running = restart()
        