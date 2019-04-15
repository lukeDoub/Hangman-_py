from random import randint

'''
Takes in the word to be made a secret word.
makes hidden word by creating a new string and then looping through the
passed in string and adds a '_' to the new string for every char in the 
passed in string
'''
def makeHiddenWord(s):
    hiddenWord = ""
    for x in s:
        hiddenWord += "_"
    return hiddenWord
            
'''
Takes in the word, the guessed char, and the secret word as a list
and then compares the char to the chars in the word and if there is a match then 
the respective index of the secret word list is changed to the char
'''
def guessChar(s, c, sW):
    for val in range(len(s)):
        if c == s[val]:
            sW[val] = c

'''
chooses a word to be useda s the secret word from a specified list using randint
'''
def chooseWord():
    words = ["make", "java", "unix", "mac", "windows", "switch", "loops"]
    randInt = randint(0, len(words)-1)
    return words[randInt]
    
'''
ask for a name and a word to be used in the game, then makes the secret word and
while both the word is not guessed and the attempts are less than tries the player
can guess a char. if while in the loop the guessed word equals the original string
then it breaks and after the loop if the guessed word does not equal the word then
the player "lost", if they do equal then the player won
'''
def playGame():
    name = raw_input("Enter Name ")
    #randomly picks a word to use from the list in chooseWord()
    word = chooseWord()
    #makes a list from the word to be easily iterated over. 
    wordList = list(word)
    #makes the hidden word(_'s)
    sWord = makeHiddenWord(word)
    #makes the hidden word list. makes it easier to replace the '_' with 
    #the correctly guessed char than replacing in the actual string
    secretWordList = list(sWord)
    print(sWord)
    tries = 10
    attempts = 0
    #while attempts are less than tries the user can guess a char
    while attempts < tries:
        guess = raw_input("Enter a char to guess ")
        #if the guess is longer than one char the user has to continue guessing
        #until a guess of one char is given
        while len(guess) != 1:
            guess = raw_input("input must be a single char ")
        guessChar(wordList, guess, secretWordList)
        attempts += 1
        print"attempts remaining: ", tries-attempts
        #makes a string from the hidden word list
        listString = "".join(secretWordList)
        print(listString)
        #if the guessed string equals the word break from the loop
        if listString == word:
            break
    #win condition: guessed word equals word
    if listString != word:
        print("You lost")
    #lose condition: guessed word does not equal word
    if listString == word:
        print("Congratulations, you won!!!")

def main():
    playGame()
        
main()

                
