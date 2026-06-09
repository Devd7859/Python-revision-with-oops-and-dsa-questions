import random

def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    print(f"Your score: {score}")
    with open("Hi-score.txt") as f:
        # .strip() removes any hidden spaces or newlines
        hiscore_content = f.read().strip()
        
        # If the file is not empty, convert to int
        if hiscore_content != "":
            hiscore = int(hiscore_content)
        else:
            hiscore = 0
    if (score > hiscore or hiscore == " "):
        with open("Hi-score.txt","w") as f:
            f.write(str(score))
    return score


game()
