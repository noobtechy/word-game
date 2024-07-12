import random
name = input("Give me your name : ")
print("all the best ", name)
words = ['hello','hi','yekkow','olo','tata','noobytech']
word = random.choice(words)
guesses = ''
turns = 7
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end = "")
            failed +=1
    print()
    if failed == 0:
        print("You win ")

        print("The word is : ", word)
        break
    
    guess = input(" guess a character: ")
    guesses += guess
    if guess not in word:
        turns -= 1 
        print("wrong")
        print("you have ", turns,"more gusses ")
        if turns == 0:
            print("you lost! thanks for trying ")       
                

