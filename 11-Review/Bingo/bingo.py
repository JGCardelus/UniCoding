import random
import sys
import time
import platform
import matplotlib.pyplot as plt

system = platform.system()

maximum = None
size = None
card = None

ld_mode = False


class sysc:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def poss_num(num):
    # sys.stdout.write(sysc.OKBLUE)
    sys.stdout.write(num)
    # sys.stdout.write(sysc.ENDC)


def final_num(num):
    # sys.stdout.write(sysc.BOLD)
    # sys.stdout.write(sysc.OKBLUE)
    sys.stdout.write(num)
    # sys.stdout.write(sysc.ENDC)


def generate_random(list, maximum):
    n = 0
    while True:
        n = random.randint(0, maximum)
        if n not in list:
            break

    return n


def generate_card(size, maximum):
    card = []
    for i in range(size ** 2):
        n = generate_random(card, maximum)
        card.append(n)

    return card


def print_card(card, numbers):
    row_len = len(card) ** (1 / 2)  # 4 * 4 = 16, row_len = 4 = sqrt(16)
    for i in range(row_len):
        for j in range(row_len):
            # Check wether the number has been selected or not
            number = card[i + j]
            if number in numbers:
                number = 'X'
            else:
                number = str(number)

            # Print number box
            print("|{2:s}".format(number), end='')

        print('|')


def simulate_drum(numbers, maximum):
    global ld_mode

    if ld_mode == False:
        sys.stdout.write('And the next number is....')
        sys.stdout.write('\n')

        for i in range(10):
            p = random.randint(0, maximum)
            poss_num(str(p) + '\r')
            time.sleep(0.3)

    number = generate_random(numbers, maximum)

    if ld_mode == False:
        final_num(str(number))

    return number


def is_done(card, numbers):
    done = False
    correct_numbers = 0

    for number in card:
        if number in numbers:
            correct_numbers += 1

    if correct_numbers == len(card):
        done = True

    return done


def play_game(size, maximum):
    numbers = []
    balls = 0
    # Generate card and print it
    card = generate_card(size, maximum)
    printcard(card, numbers_from_the_drum)

    # Play while the player has not won
    while not is_done(card, numbers):
        ball_n = simulate_drum(numbers, maximum)
        balls += 1
        numbers.append(ball_n)
        print("Updated Play Card: ")
        print_card(card, numbers)

    return balls


def play_headless(size, maximum):
    numbers = []
    balls = 0
    # Generate card and print it
    card = generate_card(size, maximum)

    # Play while the player has not won
    while not is_done(card, numbers):
        ball_n = simulate_drum(numbers, maximum)
        balls += 1
        numbers.append(ball_n)

    return balls


def luduocris_mode():
    global ld_mode

    ld_mode = True

    stats = []
    tries = {}
    for i in range(1, 10):
        avg_sum = 0
        tries[i] = []
        for j in range(10):
            required_balls = play_headless(i, 100)
            avg_sum += required_balls

            tries[i].append(required_balls)

        avg_sum /= 10
        stats.append(avg_sum)

    plt.plot(list(range(1, 10)), stats)

    for i in tries.keys():
        balls = tries[i]
        for ball in balls:
            plt.scatter(i, ball, c='g', alpha=0.5)

    plt.xlabel("Card size")
    plt.ylabel("Avg number of balls required")
    plt.legend()
    plt.show()


luduocris_mode()
