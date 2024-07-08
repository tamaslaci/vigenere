# Vigenére
# Enc -> c(i+jt) = m(i+jt) + k(i) mod 26 : i=1..t, j=0..
# Dec -> m(i+jt) = c(i+jt) - k(i) mod 26 : i=1..t, j=0..

import random

message = "egynagyontitkosuzenetegynagyontikosfeladotolegynagyontitkosfogadonak"

def Gen(l = random.randint(10, 20)):
    key = "".join([chr(random.randint(0, 25) + ord("a")) for n in range(l)])
    return key

key = Gen()

def Enc(message, key):
    key_text = ""
    while len(key_text) < len(message):
        key_text += key
    full_key_text = key_text[:(len(message))]
    message_nums = [(ord(m) - ord("a")) for m in message]
    key_nums = [(ord(k) - ord("a")) for k in full_key_text]
    chipertext = ""
    for (m, k) in zip(message_nums, key_nums):
        chipertext += str(chr((m + k) % 26 + ord("a")))
    return chipertext


def Dec(chipertext, key):
    key_text = ""
    while len(key_text) < len(chipertext):
        key_text += key
    full_key_text = key_text[:(len(chipertext))]
    key_nums = [(ord(k) - ord("a")) for k in full_key_text]
    decoded_message = ""
    chipertext_nums = [(ord(c) - ord("a")) for c in chipertext]
    for (c, k) in zip(chipertext_nums, key_nums):
        decoded_message += str(chr((c - k) % 26 + ord("a")))
    return decoded_message

def Print_vigenere():
    print("\n'vigenere.py'\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("secret message:\t\t" + message)
    print("random key:\t\t" + key)
    print("------------------------------------------------------------")
    print("encoded message:\t" + Enc(message, key))
    print("decoded message:\t" + Dec(Enc(message, key), key) +"\n")

Print_vigenere()