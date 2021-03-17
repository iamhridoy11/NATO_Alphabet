import pandas

file = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_comprehension = {row.letter: row.code for (index, row) in file.iterrows()}


# List comprehension and exception handling

def generate_result():
    word = input("Enter a word: ").upper()
    try:
        list_comprehension = [dict_comprehension[items] for items in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_result()
    else:
        print(list_comprehension)


generate_result()
