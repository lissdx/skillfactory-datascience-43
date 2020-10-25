from typing import List
from exception import GuessValueError


def guess_index(num_list: List[int]) -> int:
    """
    Try find the index in the middle of list.
    :param num_list:
    :return: index in the middle of list
    """
    # Validate input list
    if num_list is None or len(num_list) <= 0:
        raise GuessValueError("Search list is empty")

    # Help normalize len to avoid .5 result
    normalizer = len(num_list) % 2

    return int((len(num_list) - normalizer) / 2)


def read_user_input() -> str:
    """
    Check and read user's input.
    Limit the input by 'Y', 'B', 'E', 'S' chars
    :return:
    """
    answer = input()
    while answer.upper() not in ['Y', 'B', 'E', 'S']:
        print("Please enter the right answer!")
        print("Press\nY - if I'm right\nB - your number bigger" +
              "\nS - your number smaller" +
              "\nE - exit")

        answer = input()

    return answer.upper()
