# Vigenére
# Enc -> c(i+jt) = m(i+jt) + k(i) mod 26 : i=1..t, j=0..
# Dec -> m(i+jt) = c(i+jt) - k(i) mod 26 : i=1..t, j=0..

from collections import Counter

import frequency
import text

chipertext = text.chipertext
key = text.random_key
length = len(key)

def make_ceasar_chipers(chipertext):
    array_of_ceasar_texts = []
    i = 0
    while i < length:
        array_of_ceasar_texts.append("")
        j = 0
        while (i + j * length) < len(chipertext):
            array_of_ceasar_texts[i] += chipertext[i + j * length]
            j = j + 1
        i = i + 1
    return array_of_ceasar_texts

def analyze_ceasar_texts(array_of_ceasar_texts):
    letters_frequencies = {}
    for txt in array_of_ceasar_texts:
        letters_frequency_in_txt = {}
        for c in txt:
            letters_frequency_in_txt[c] = round(txt.count(c) / len(txt) * 100, ndigits=2)
        letters_frequencies[txt] = letters_frequency_in_txt
    return letters_frequencies

def sort_ceasar_text(ceasar_text_frequencies):
    tuples_array = [items for items in ceasar_text_frequencies.items()]
    tuples_array.sort(reverse=True, key=(lambda i:i[1]))
    return "".join([x for (x, _) in tuples_array])

def calculate_offset(ceasar_text_frequencies):
    sorted_ceasar_text = sort_ceasar_text(ceasar_text_frequencies)
    offsets = {}
    for (c, f) in zip(sorted_ceasar_text, frequency.sorted_frequency_letters):
        offsets[c] = ((ord(c) - ord("a")) - (ord(f) - ord("a"))) % 26
    most_common_offset = Counter(offsets.values()).most_common(1)[0][0]
    return most_common_offset

def decode_ceasar_chipers(chipertext):
    decoded_ceasar_chipers = []
    hacked_key = ""
    for ceasar_text_tuples in analyze_ceasar_texts(make_ceasar_chipers(chipertext)).items():
        ceasar_key = calculate_offset(ceasar_text_tuples[1])
        hacked_key += chr(ceasar_key + ord("a"))
        decoded_ceasar_chiper = ""
        for c in ceasar_text_tuples[0]:
            decoded_ceasar_chiper += chr((((ord(c) - ord("a")) - ceasar_key) % 26) + ord("a"))
        decoded_ceasar_chipers.append(decoded_ceasar_chiper)
    return (decoded_ceasar_chipers, hacked_key)

def assemble_plaintext(chipertext):
    decoded_ceasar_chipers = decode_ceasar_chipers(chipertext)[0]
    hacked_key = decode_ceasar_chipers(chipertext)[1]
    hacked_message = ["o" for i in range(len(chipertext))]
    i, j = 0, 0
    for ceasar_chiper in decoded_ceasar_chipers:
        while j < len(ceasar_chiper):
            hacked_message[i + j * length] = ceasar_chiper[j]
            j = j + 1
        i = i + 1
        j = 0
    return ("".join(hacked_message), hacked_key)

def Print_vigenere_hack():
    print("'vigenere_hack.py'\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    hacked_message = assemble_plaintext(chipertext)[0]
    hacked_key = assemble_plaintext(chipertext)[1]
    print("hacked message:\t\t" + hacked_message[:100] + "\n\t\t\t..." + hacked_message[-100:])
    print("\t\t\t(" + str(len(hacked_message)) + " characters)")
    print("hacked key:\t\t" + hacked_key)
    print("------------------------------------------------------------")
    print("original message:\t" + text.plaintext[:100] + "\n\t\t\t..." + text.plaintext[-100:])
    print("\t\t\t(" + str(len(text.plaintext)) + " characters)")
    print("original key:\t\t" + key + "\n")

Print_vigenere_hack()