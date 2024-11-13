from art import logo, vs
from game_data import data
from random import choice
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


print(logo)

##pick two random items and
#make a function using random.choice
def pick_data(data_list):
    item = choice(data_list)
    return item

def print_data(item1, item2):
    print(
        f"Compare A: {item1['name']}, a {item1['description']}, from {item1['country']}."
    )
    print(vs)
    print(
        f"Againts B: {item2['name']}, a {item2['description']}, from {item2['country']}."
    )

## Check the answer
def compare_followers(item1, item2):
    if item1['follower_count'] > item2['follower_count']:
        return True
    else:
        return False

##repeat this game until the player guesses wrong. show the score.
def show_final_score(score):
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

##if the player guessed right, take the second one in the first place and and take another random item for the second one. incremenet by 1 the score.

score = 0
itemA = pick_data(data)
itemB = pick_data(data)
answer_check = True

while answer_check:
    # make sure they are not the same
    while itemA == itemB:
        itemB = pick_data(data)

    print_data(itemA, itemB)
    answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()
    if answer == 'A':
        answer_check = compare_followers(itemA, itemB)
    else:
        answer_check = compare_followers(itemB, itemA)

    score += 1
    itemA = itemB
    itemB = pick_data(data)
    if answer_check:
        print(f"you are right! your score: {score}")

show_final_score(score)
