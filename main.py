# In this game you need to guess which of the names is richer
# For example 'Richard Branson' vs 'Ilon Musk' ---> type 'higher' if you think the second is richer, or 'lower' if
# you think the second is poorer
import random

the_compare_names_values = [
    ('ELON MUSK', 219),
    ('JEFF BEZOS', 171),
    ('BERNARD ARNAULT', 158),
    ('BILL GATES', 128),
    ('WARREN BUFFETT', 118),
    ('LARRY PAGE', 111),
    ('SERGEY BRIN', 107),
    ('LARRY ELLISON', 106),
    ('STEVE BALLMER', 91.4),
    ('MUKESH AMBANI', 90.7),
    ('GAUTAM ADANI', 90),
    ('MICHAEL BLOOMBERG', 82),
    ('CARLOS SLIM HELU', 81.2),
    ('Francoise Bettencourt Meyers', 74.8),
    ('MARK ZUCKERBERG', 67.3),
    ('Jim Walton', 66.2),
    ('Zhong Shanshan', 65.7),
    ('MICHAEL DELL', 55.1),
    ('IOVANNI FERRERO', 36.2),
    ('Jacqueline Mars', 31.7),
    ('Susanne Klatten', 24.3),
    ('Jack Ma', 22.8),
    ('Leonard Lauder', 23.1),
    ('Steve Cohen ', 17.4),
    ('Pavel Durov', 15.1),
]


def generate_index():
    """Generate a random number, which we will use for our person choose"""
    return random.randint(0, 24)


def choose_person_to_compare(array):
    """Choose a person in list of tuples"""
    index = generate_index()
    person = array[index]
    return person


def compare_the_riches_of_persons(person_one, person_two, your_suggestion):
    riches_person_one = person_one[1]
    riches_person_two = person_two[1]

    if riches_person_one > riches_person_two and your_suggestion == 'lower':
        return True
    elif riches_person_one > riches_person_two and your_suggestion == 'higher':
        return False
    elif riches_person_one < riches_person_two and your_suggestion == 'lower':
        return False
    elif riches_person_one < riches_person_two and your_suggestion == 'higher':
        return True


def the_win_statement(array, person_one, person_two, couple_of_compares):
    couple_of_compares = [person_one[0], person_two[0]]
    next_person_to_compare = choose_person_to_compare(array)

    couple_of_compares.pop(0)
    couple_of_compares.append(next_person_to_compare[0])
    return couple_of_compares

numbers_of_correct_answers = 0

list_of_two = []
first_compare_person = choose_person_to_compare(the_compare_names_values)
second_compare_person = choose_person_to_compare(the_compare_names_values)
the_win_statement(the_compare_names_values, first_compare_person, second_compare_person, list_of_two)


lose_the_game = False
make_suggestion = input(
    f"If you think that {first_compare_person[0].title()} have more wealth, type 'higher', if not, type 'lower': ")

while not lose_the_game:

    if compare_the_riches_of_persons(first_compare_person, second_compare_person, make_suggestion) is True:
        print("You win!")
        the_win_statement(the_compare_names_values, first_compare_person, second_compare_person, list_of_two)
        current_person = the_win_statement(the_compare_names_values, first_compare_person, second_compare_person, list_of_two)
        numbers_of_correct_answers += 1
        make_suggestion = input(
            f"If you think that {current_person[0].title()} have more wealth than {current_person[1].title()}, type 'higher', if not, type 'lower': ")
    else:
        print("You lose, sorry!")
        lose_the_game = True
        break



