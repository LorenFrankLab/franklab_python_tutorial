"""We can use the module docstring to describe the module"""
import os

N_CATS = 3


def my_first_function():
    """Prints Success"""
    print("Success")


def my_second_function():
    """Prints number of cats"""
    print(N_CATS)


def get_abs_path_of_cur_dir():
    print(os.path.abspath(os.path.curdir))
