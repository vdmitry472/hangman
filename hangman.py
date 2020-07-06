# Write your code here
import random

print("H A N G M A N")
words = ["python", "java", "kotlin", "javascript"]
alphabet = list("qwertyuiopasdfghjklzxcvbnm")
game_flag = 1
def play_hangman(command):
    global words
    global alphabet
    global game_flag
    if command == "play":
        word = random.choice(words)
        test_word = list(word)
        res = list(word)
        check = list()
        count = 0
        for char in res:
            if count >= 0:
                res.pop(count)
                res.insert(count, "-")
            count += 1
        count = 8
        while count > 0:
            loop = 1
            flag = 0
            while loop > 0:
                print("")
                print("".join(res))
                letter = input("Input a letter: ")
                if (len(letter) == 1) and letter in alphabet:
                    loop = 0
                elif len(letter) != 1:
                    print("You should input a single letter")
                elif letter not in alphabet:
                    print("It is not an ASCII lowercase letter")
            if letter not in test_word and letter not in check:
                print("No such letter in the word")
                flag = 1
            elif letter in res or letter in check:
                print("You already typed this letter")
            else:
                i = 0
                for char in test_word:
                    if letter == char:
                        res.pop(i)
                        res.insert(i, char)
                    i += 1
            if "-" not in res:
                print("You guessed the word {}!".format(word))
                print("You survived!")
                break
            check.append(letter)
            if flag == 1:
                count -= 1
        if count == 0:
            print("You are hanged!")
    else:
        game_flag = 0
while game_flag > 0:
    command = input('Type "play" to play the game, "exit" to quit: ')
    play_hangman(command)
