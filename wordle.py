# Program will help me win in wordle!

#===============================================================================

import os

# fill the position score dictionaries
def fill_pos_score(all, pos, index):
    for word in all:
        pos[word[index]] += 1
    return pos

# copy one dictionary into another
def copy_dict(src, dest):
    for i in src:
        dest[i] = src[i]
    return dest

# remove words with given letter in given index from the given dictionary
def remove_word(letter, index, p_words):
    ret = {}
    ret = copy_dict(p_words, ret)
    for word in p_words:
        if word[index] == letter:
            del ret[word]
    return ret

# remove words that dont have the letter in the given index
def remove_word_2(letter, index, p_words):
    ret = {}
    ret = copy_dict(p_words, ret)
    for word in p_words:
        if not(word[index]) == letter:
            del ret[word]
    return ret

# remove all words with given letter
def remove_all(letter, p_words):
    ret = {}
    ret = copy_dict(p_words, ret)
    for word in p_words:
        for ch in word:
            if ch == letter:
                del ret[word]
                break
    return ret

# returns whether or not given character is a number
def is_num(ch):
    nums = {"9", "8", "0", "1", "2", "3", "4"}
    for n in nums:
        if ch == n:
            return True
    return False

# return the word with the greatest score from the given dictionary
def guess_word(dict):
    largest_score = 0 # will store the largest score in given dict
    word = ""         # word to be returned
    for w in dict:
        if dict[w] > largest_score:
            largest_score = dict[w]
            word = w
    return word

# print the remaining words
def print_remaining(dict):
    for word in dict:
        print(word)

#===============================================================================

# initialize dict to store count of each char at each index
pos_score_1    = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
pos_score_2    = pos_score_3 = pos_score_4 = pos_score_5 = pos_score_1
all_words      = {} # dict that stores all words from 'words.txt'
word_score     = {} # dict that stores all words with their associated score
possible_words = {} # dict that will store current possible words while running the program
# load in the words file
try:
    file = open("words.txt", "rt")
except:
    print("Could not open 'words.txt', make sure it is in working directory!")

for w in file:
    all_words[w[0:5]] = 0 # no need for different numbers in this dict

# close the file when done using it
file.close()

# iterate over the words, creating a score for each letter
pos_score_1 = fill_pos_score(all_words, pos_score_1, 0)
pos_score_2 = fill_pos_score(all_words, pos_score_2, 1)
pos_score_3 = fill_pos_score(all_words, pos_score_3, 2)
pos_score_4 = fill_pos_score(all_words, pos_score_4, 3)
pos_score_5 = fill_pos_score(all_words, pos_score_5, 4)

# give each word a score based upon previously found occurrence for each letter in each index
for word in all_words:
    word_score[word] = pos_score_1[word[0]] + pos_score_2[word[1]] + pos_score_3[word[2]] + pos_score_4[word[3]] + pos_score_5[word[4]]

# Now try to guess the word of the day based on first two guesses as well as input string
print("*******************************************************************************")
print("*  Try words as you please, the two given are 'statistically' your            *")
print("*  best option. If you know the location of a letter, type it with            *")
print("*  its preceding index number (0,1,2,3, or 4). If you don't know a            *")
print("*  letter's location, simply include the letter with a space infront          *")
print("*  of it. If a letter is known to NOT be in the string, precede the letter    *")
print("*  with a 9. Hit enter after your input string. If you would like to          *")
print("*  print all possible strings, input an 8. IF you would like to terminate     *")
print("*  the program, simply press 'ctrl c', or type a 0 and press enter. Goodluck  *")
print("*******************************************************************************")

possible_words = word_score # initialize to
inp = input("input: ")
while inp != "0":
    str = ""
    count = 0
    while count < len(inp):
        if is_num(inp[count]):
            index = inp[count]
            if index == "9":
                possible_words = remove_all(inp[count+1], possible_words)
                count += 3
            elif index == "8":
                print_remaining(possible_words)
                count += 2
            else:
                possible_words = remove_word(inp[count+1], int(index), possible_words)
                count += 3
        else:
            index = inp[count+1]
            possible_words = remove_word_2(inp[count], int(index), possible_words)
            count += 3
    print(guess_word(possible_words))
    inp = input("input: ")

os.system("pause")
