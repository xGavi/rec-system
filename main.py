from game import Game
from dataBase import DataBase
import csv

def q0():
    q = input("What do you want to play?\n")
    matches: list = db.searchT(q)
    if len(matches) == 0:
        print("No matches found")
        tryAgain()
    elif len(matches) > 1:
        q1(matches)
    else:
        print(matches[0])
        c1(matches[0])

def q1(tagMatches: list):
    print(tagMatches)
    q = input("These are the tag matches from our database. Out of those, what do you want to play?\n")
    matches: list = db.searchT(q, tagMatches)
    if len(matches) == 0:
        print("No matches found")
        tryAgain()
    elif len(matches) > 1:
        q1(matches)
    else:
        print(matches[0])
        c1(matches[0])

def q2(tagMatch: str, gameMatches=None):
    print("Following games with that tag:")
    matches: list = db.searchG([tagMatch])
    for match in matches:
        print(match)
    q = input("What game do you want to play?\n")
    matches = db.searchG([q], matches)
    if len(matches) == 0:
        print("No matches found")
        tryAgain()
    elif len(matches) > 1:
        q2(tagMatch, matches)
    else:
        print(matches[0])
        c2(matches[0])

def tryAgain():
    q = input("Do you wish to try again? (y/n)\n")
    if q.lower() == "y":
        q0()
    elif q.lower() == "n":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input")
        tryAgain()

def c1(match: str):
    q = input(f"{match}: is this what you want to play? (y/n)\n")
    if q.lower() == "y":
        q2(match)
    elif q.lower() == "n":
        tryAgain()
    else:
        print("Invalid input")
        c1(match)

def c2(match: Game):
    q = input(f"{match.name}: is this what you want to play? (y/n)\n")
    if q.lower() == "y":
        print("Enjoy!")
        exit()
    elif q.lower() == "n":
        tryAgain()
    else:
        print("Invalid input")
        c2(match)

if True:
    db = DataBase("db")
    with open('gameList.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            game = Game(db, row['Name'], row['Developer'], row['Year of Launch'], *row['Tags'].split(";"))

    print("welcome")
    q0()



