lives = 6
word = ""
letter = ""
updatedSpaces= []

def intialize ():
    global word
    global updatedSpaces
    word = "airport"
    updatedSpaces = "_ _ _ _ _ _ _"
    print("Try to guess the word in 6 tries")
    print(updatedSpaces)

def getLetter():
    global letter
    print("What is your first guess?")
    letter = raw_input()
    
#def check():
   
def won():
    if updatedSpaces == word:
        print("Hurray, you got the word!")
    else:
        getLetter()        
 
def main():
    intialize()
    getLetter()
    #check()
