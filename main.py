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


def current_person_one_name(array):
    return array[0][0]


def current_person_two_name(array):
    return array[1][0]


def current_person_one_wealth(array):
    return array[0][1]


def current_person_two_wealth(array):
    return array[1][1]


numbers_of_correct_answers = 0

lose_the_game = False

first_compare_person = choose_person_to_compare(the_compare_names_values)

list_of_two = [first_compare_person, ]

last_person = ''
wealth_of_last_person = 0

while not lose_the_game:
    second_compare_person = choose_person_to_compare(the_compare_names_values)
    list_of_two.append(second_compare_person)
    current_person_one = list_of_two[0]
    current_person_two = list_of_two[1]
    make_suggestion = input(
        f"Compare {current_person_one_name(list_of_two).title()} with ${current_person_one_wealth(list_of_two)}B and {current_person_two_name(list_of_two).title()} wealth!\nType 'higher' or 'lower' for second name: ")

    if compare_the_riches_of_persons(current_person_one, current_person_two, make_suggestion) is True:
        print("You made a correct guess! You move on 😉")
        list_of_two.pop(0)

        numbers_of_correct_answers += 1
    else:
        lose_the_game = True
        last_person = current_person_two_name(list_of_two).title()
        wealth_of_last_person = current_person_two_wealth(list_of_two)
        break

if lose_the_game:
    print("You lose, sorry! 😣")
    print(f"The numbers of your correct answers are: {numbers_of_correct_answers}!")
    print(f"You can guess correct that {last_person} have a wealth of ${wealth_of_last_person}B")
