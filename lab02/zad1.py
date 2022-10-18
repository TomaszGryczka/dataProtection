import sys, re
from collections import Counter
from string import ascii_letters

table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "nopqrstuvwxyzabcdefghijklm")

error = 0.05

def predict_offset(text, most_freq_letter, most_freq_letter_prob):
    lowercase_text = text.lower()
    letters_freq = count_letters(text).most_common()
    sum_of_letters = 0
    for i in range(len(letters_freq)):
        sum_of_letters += letters_freq[i][1]
    letter_prob = letters_freq[0][1] / sum_of_letters
    letter = letters_freq[0][0]
    if(most_freq_letter_prob + error > letter_prob and letter_prob > most_freq_letter_prob - error):
        return ord(letter) - ord(most_freq_letter)
    else:
        print("Cannot find offset")
        return 0




def count_letters(text):
    filtered = [c for c in text.lower() if c in ascii_letters]
    return Counter(filtered)

with open('spanish.txt', 'r') as spanish, open("english.txt", "r") as english, open("polish.txt", "r") as polish:
    print("Predicted offset: ", predict_offset(str.translate(spanish.read(), table), "e", 0.125))
    print("Predicted offset: ", predict_offset(str.translate(english.read(), table), "e", 0.138))
    print("Predicted offset: ", predict_offset(str.translate(polish.read(), table), "a", 0.088))