import random

def draw_letters():
    allletters = []
    alphabet = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }
    #expanded dictionary per numbers of letters
    for letter, number in alphabet.items():
        for i in range(number):
            allletters.append(letter)
<<<<<<< HEAD

=======
    
    #picking 10 random letters from expanded dictionary
>>>>>>> 4ce1b22f209d98b0bd4915516b9c1b862c64ebe4
    gameletters = []
    for letter in range(10):
        number = random.randint(0, 27)
        random_letter = allletters[number]
        gameletters.append(random_letter)
        allletters.remove(random_letter)
        
    return gameletters



def uses_available_letters(word, letter_bank):
    letter_bank_copy = letter_bank[:]
    for letter in word:
        letter = letter.capitalize()
        if letter not in letter_bank_copy:
            return False
        else:
            letter_bank_copy.remove(letter)
    return True


    
        

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass