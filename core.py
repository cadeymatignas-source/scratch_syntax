import sys
from random import randint
from time import sleep

_scratch_data = {"answer": ""}


def say(text):
    print(text)


def say_for_seconds(texty, secs):
    print(texty)
    sleep(secs)


def ask(question):
    _scratch_data["answer"] = input(question)
    return _scratch_data["answer"]


def answer():
    return _scratch_data["answer"]


def wait(seconds):
    sleep(seconds)


def pick_random_number_from(a, b):
    return randint(a, b)


def stop_all():
    sys.exit(0)


def add_to_list(listname, item):
    listname.append(item)


def insert_in_list(listname, index, item):
    listname.insert(index, item)


def delete_from_list(listname, index):
    listname.pop(index)


def delete_all_from_list(listname):
    listname.clear()


def replace_in_list(listname, index, item):
    listname[index] = item


# For anyone reading the code, I skipped the forever and repeat functions not because I wanted to but because it doesnt work: Cade
