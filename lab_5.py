"""
this program will translation sentences that the end user will input
file textese.txt will serve as a dictionary
a list of strings from each line in the text file will be created
then dictionary the list will be created
file will be close as soon as function is done running

the sentence will be stored and processed word for word


a loop will go through each word that the user inputed then finds the matching word and returns back the value tied to the word
in the dictionary

when each word is translated we then
print out the translated sentence to the user. 

"""

"""

main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    words = for each of the word in the sentence
    for each words, translate the word
    print translate sentence to user

create_dictionary():
    read in textese.txt
    create list = each line from file
    close the file
    create a dict off of the list
    return the dict

main()

"""

def  main():
    sentence = input("Enter a sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
    words = sentence.split()
    for word in words: 
        print(dictionary.get(word, word), " ", end="")

main()