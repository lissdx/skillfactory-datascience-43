import sys
from core import guess_index, read_user_input

MAX_NUM = 100
MIN_NUM = 0


def main():
    """
    The game based on binary-search algorithm
    https://en.wikipedia.org/wiki/Binary_search_algorithm
    :return:
    """
    ind = None
    is_answer_found = False

    # Sorted list of values
    search_list = list(range(MIN_NUM, MAX_NUM + 1))
    start_play_txt = f"Hi, my friend! Could you choose a number between {MIN_NUM} and {MAX_NUM} and remember it?" + \
                     "\nI'll try to guess it ASAP!\nJust answer to flowing question...\nPress ENTER to continue"

    guess_answer = "*****\nYour number is {}.\nPress\nY - if I'm right\nB - your number bigger" + \
                   "\nS - your number smaller" + \
                   "\nE - exit"

    input(start_play_txt)

    while not is_answer_found:
        ind: int = guess_index(search_list)
        print(guess_answer.format(search_list[ind]))
        answer = read_user_input()

        if answer == 'E':
            print('Bye, Bye!')
            sys.exit()

        if answer == 'Y':
            is_answer_found = True
            continue

        # If bigger get the higher part of array
        if answer == 'B' and search_list[ind] != search_list[-1]:
            search_list = search_list[ind + 1:]
        # If smaller get the lower part of array
        elif answer == 'S' and search_list[ind] != search_list[0]:
            search_list = search_list[:ind]
        # User doesn't remember number
        else:
            print(f'Something is goinng wrong')
            print(f'See you!')
            sys.exit()

    print(f'Your number is: {search_list[ind]}')
    print(f'See you!')


if __name__ == '__main__':
    main()
