import random
def scramble_word(word):
    
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)
def task3():
    array=["apple","orange","lemon"]
    choice_word=random.choice(array)
    scrambled_word = scramble_word(choice_word)
    
    Attempts=5
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    print(f"You have {Attempts} attempts")
    while Attempts>0:
        word=input("Enter your Guess: ")
        if word==choice_word :
            print("Congratulations")
            break
        Attempts-=1
        print(f"Incorrect! Try again. You have {Attempts} attempts left.")
    if Attempts==0:
        print(f"You’re out of attempts! The correct word was: {choice_word}")
task3()

