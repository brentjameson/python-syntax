def print_upper_words(words,letters):
    ''' Accepts a set of words and a set of letters. Prints a set of the capitalized words that start with one of the letters passed in. '''
    for letter in letters:
        cap_letters = letter.upper()
        for word in words:
            upper_word = word.upper()
            if (upper_word[0]) == cap_letters:
                print(upper_word)

print_upper_words(['hello', 'hey', 'goodbye', 'yo', 'yes'], ['h', 'y'])