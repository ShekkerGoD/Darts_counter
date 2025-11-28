# global variables

start_score:        int = 501 # standard game of x01 with 501 points
darts_thrown:       int = 0
darts_to_finish:    int = 0
main_input:         str = "" # score of visit (3 darts) or exit, quit

# functions

def greeting() -> str:
    print("\nDarts counter v0.2\n\nTo end program: type exit or quit\n\n----------\n")


def avg_score(start_score: int = 501, darts_thrown: int = 0) -> float:
    return round(start_score / darts_thrown * 3, 1)

# main part

greeting()

def main():

    global start_score, main_input, darts_thrown, darts_to_finish

    while True:

        # check-score logic for each iteration

        if start_score == 0 and darts_thrown == 9:
            print("\n----- 9 DARTER! -----\n")
            break
        if start_score == 0 and darts_thrown > 9:
            try:
                darts_to_finish = int(input("\nDarts needed to finish: "))
                if darts_to_finish > 3:
                    raise Exception
                else:
                    print(f"\n----- GAME SHOT -----\n\nYou've finished leg with {darts_thrown - 3 + darts_to_finish} darts!\n\nYour average for 3 darts is {avg_score(501, darts_thrown)}\n")
                    break
            except Exception:
                print("\n----- Not valid input ----- \n\nEnter a valid number of darts finished\n\n----------")
                continue
        if start_score < 0 or start_score == 1: # score 1 is also bust, due its disability to checkout
            print(f"\n----- Darts thrown: {darts_thrown} -----\n\n----- BUSTED -----\n\nYou've busted score!\n")
            start_score += int(main_input)
            continue
        if start_score > 170 and start_score != 0:
            try:
                main_input = input("Enter score: ")
                if main_input in {"quit", "Quit", "exit", "Exit", "QUIT", "EXIT"}:
                    break
                if int(main_input) in {163, 166, 169, 172, 173, 175, 176, 178, 179} or int(main_input) > 180:
                    print(f"\n----- Not valid input -----\n\nEnter a valid score\n\n----------\n")
                    continue
                else:
                    start_score -= int(main_input)
                    darts_thrown += 3
                    print(f"\n----- Darts thrown: {darts_thrown} -----\n\nYou've scored: {int(main_input)}\n\nPoints left: {start_score}\n\n----------\n")
                    continue
            except ValueError:
                print("\n----- Not valid input -----\n\nEnter a score (or darts finished) or type valid exit\n\n----------\n")
                continue
        if start_score <= 170 and start_score > 0:
            if start_score in {159, 162, 163, 165, 166, 168, 169}:
                try:
                    main_input = input("Enter score: ")
                    if main_input in {"quit", "Quit", "exit", "Exit", "QUIT", "EXIT"}:
                        break
                    if int(main_input) in {163, 166, 169, 172, 173, 175, 176, 178, 179} or int(main_input) > 180:
                        print(f"\n----- Not valid input -----\n\nEnter a valid score\n\n----------\n")
                        continue
                    else:
                        start_score -= int(main_input)
                        darts_thrown += 3
                        print(f"\n----- Darts thrown: {darts_thrown} -----\n\nYou've scored: {int(main_input)}\n\nPoints left: {start_score}\n\n----------\n")
                        continue
                except ValueError:
                    print("\n----- Not valid input -----\n\nEnter a score (or darts finished) or type valid exit\n\n----------\n")
                    continue
            try:
                print(f"----- CHECKOUT -----\n\nYou required {start_score}\n\n----------\n")
                main_input = input("Enter score: ")
                if main_input in {"quit", "Quit", "exit", "Exit", "QUIT", "EXIT"}:
                    break
                if int(main_input) in {159, 162, 163, 166, 169, 172, 173, 175, 176, 178, 179} or int(main_input) > 180:
                    print(f"\n\n----- Not valid input -----\n\nEnter a valid score\n\n----------\n")
                    continue
                else:
                    start_score -= int(main_input)
                    darts_thrown += 3
            except ValueError:
                print("\n\n----- Not valid input -----\n\nEnter a score (or darts finished) or type valid exit\n\n----------\n")
            continue


if __name__ == "__main__":
    main()
