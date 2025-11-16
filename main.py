# global variables

start_score: int = 501 # standard game of x01 with 501 points
darts_thrown: int = 0
main_input: str = "" # score of visit (3 darts) or exit, quit

# functions

def greeting() -> str:
    print("\nDarts counter v0.1\n\nTo end program: type exit or quit\n\n----------\n")

# main part

greeting()

while True:

    try:
        main_input = input("Enter score: ")
        if main_input in ["quit", "Quit", "exit", "Exit", "QUIT", "EXIT"]:
            break
        start_score -= int(main_input)
        darts_thrown += 3
    except ValueError:
        darts_thrown -= 3
        print("\n\n----- Not valid input -----\nEnter a score or type valid exit\n\n----------\n")
    
    if start_score > 170:
        print(f"\n----- Darts thrown: {darts_thrown} -----\n\nYou've scored: {int(main_input)}\n\nPoints left: {start_score}\n\n----------\n")
    if start_score <= 170 and start_score > 0:
        print(f"\n----- Darts thrown: {darts_thrown} -----\n\n----- CHECKOUT -----\n\nYou required {start_score}\n\n----------\n")
    if start_score < 0:
        print(f"\n----- Darts thrown: {darts_thrown} -----\n\n----- BUSTED -----\n\nYou've busted score!\n")
        start_score += int(main_input)
        print(f"----- CHECKOUT -----\n\nYou required {start_score}\n\n----------\n")
    if start_score == 0: 
        print(f"\n----- GAME SHOT -----\n\nYou've finished leg with {darts_thrown} darts!\n")
        break