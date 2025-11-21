# global variables

start_score:    int = 501 # standard game of x01 with 501 points
darts_thrown:   int = 0
main_input:     str = "" # score of visit (3 darts) or exit, quit

# functions

def greeting() -> str:
    print("\nDarts counter v0.2\n\nTo end program: type exit or quit\n\n----------\n")

# main part

greeting()

while True:

    try:
        main_input = input("Enter score: ")
        if main_input in {"quit", "Quit", "exit", "Exit", "QUIT", "EXIT"}:
            break
        if int(main_input) in {163, 166, 169, 172, 173, 175, 176, 178, 179} or int(main_input) > 180:
            print(f"\n\n----- Not valid input -----\n\nEnter a valid score\n\n----------\n")
            continue
        else:
            start_score -= int(main_input)
            darts_thrown += 3
    except ValueError:
        darts_thrown -= 3
        print("\n\n----- Not valid input -----\n\nEnter a score or type valid exit\n\n----------\n")
        continue
    
    if start_score < 0 or start_score == 1: # score 1 is also bust, due its disability to checkout
        print(f"\n----- Darts thrown: {darts_thrown} -----\n\n----- BUSTED -----\n\nYou've busted score!\n")
        start_score += int(main_input)
        print(f"----- CHECKOUT -----\n\nYou required {start_score}\n\n----------\n")
        continue
    if start_score > 170:
        print(f"\n----- Darts thrown: {darts_thrown} -----\n\nYou've scored: {int(main_input)}\n\nPoints left: {start_score}\n\n----------\n")
    if start_score <= 170 and start_score > 0:
        print(f"\n----- Darts thrown: {darts_thrown} -----\n\n----- CHECKOUT -----\n\nYou required {start_score}\n\n----------\n")
    if start_score == 0: 
        print(f"\n----- GAME SHOT -----\n\nYou've finished leg with {darts_thrown} darts!\n")
        break
