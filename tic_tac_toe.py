"""
W02 Prove: Developer - Solo Code Submission
Author: Alex Ward
"""

def main():

    game_over = False
    turns = 0

    grid_list = [ "1", "2", "3", "4", "5", "6", "7", "8", "9" ]

    print_grid(grid_list)
    
    while not game_over:

        x_input = input("x's turn to choose a square (1-9): ")

        for num in grid_list:
            if x_input == num:
                grid_list[int(num) - 1] = "x"
                turns += 1

        print_grid(grid_list)

        game_over = check_game_status(grid_list, turns)

        if not game_over:
            o_input = input("o's turn to choose a square (1-9): ")

            for num in grid_list:
                if o_input == num:
                    grid_list[int(num) - 1] = "o"
                    turns += 1

            print_grid(grid_list)

            game_over = check_game_status(grid_list, turns)

def print_grid(grid_list):

    print(f"\n {grid_list[0]} | {grid_list[1]} | {grid_list[2]}")
    print("---+---+---")
    print(f" {grid_list[3]} | {grid_list[4]} | {grid_list[5]}")
    print("---+---+---")
    print(f" {grid_list[6]} | {grid_list[7]} | {grid_list[8]}\n")

def check_game_status(grid_list, turns):
    
    # I originally had this if statement written differently; it was much longer
    # and needlessly complicated. I implemented the if statement from the solution
    # program to improve mine. 

    if grid_list[0] == grid_list[1] == grid_list[2] \
    or grid_list[3] == grid_list[4] == grid_list[5] \
    or grid_list[6] == grid_list[7] == grid_list[8] \
    or grid_list[0] == grid_list[3] == grid_list[6] \
    or grid_list[1] == grid_list[4] == grid_list[7] \
    or grid_list[2] == grid_list[5] == grid_list[8] \
    or grid_list[0] == grid_list[4] == grid_list[8] \
    or grid_list[2] == grid_list[4] == grid_list[6]:
        print("Good game. Thanks for playing!")
        return True
    elif turns == 9:
        print("That's a draw. Thanks for playing!")
        return True
    else:
        return False

if __name__ == "__main__":
    main()