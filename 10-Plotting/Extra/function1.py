import numpy as np
import matplotlib.pyplot as plt

def excs_1():
    x = np.linspace(-8, 8, 1000)
    # Function
    a = np.add(x, 4)
    b = np.add(x, 2)
    c = np.add(x, -3)
    ab = np.multiply(a, b)
    abc = np.multiply(ab, c)
    y = np.multiply(abc, 0.25)

    axis_y = np.linspace(np.amin(y), np.amax(y), 1000)

    roots = np.array([-4, -2, 3])

    plt.plot(x, y, color="blue", label="Function y=0.25(x+4)(x+2)(x-3)")
    plt.plot(np.zeros(axis_y.shape), axis_y, dashes=[6, 2], color="green", label="Axis")
    plt.plot(x, np.zeros(x.shape), dashes=[6, 2], color="green")
    plt.axis([-8, 8, -20, 30])
    plt.plot(roots, np.zeros(roots.shape), 'r*', label="Roots")

    for i in range(len(roots)):
        name = "Root " + str(i + 1)
        plt.annotate(name, xy=(roots[i], 0), xytext=(roots[i], 10), arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xticks(np.arange(-5, 5, step=1))
    plt.yticks(np.arange(-20, 30, step=10))
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.show()

def excs_2():
    n_subplots = 0
    while True:
        try:
            n_subplots = int(input("Enter an even number (0, infinity): "))
            if n_subplots % 2 == 0:
                break
            elif n_subplots <= 0:
                print("The value must be over 0")
            else:
                print("Please enter an even number, following the specifications")
        except ValueError:
            print("Please enter a number")

    n_rows = n_subplots // 2
    plt.figure(1)

    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    fig.show()

excs_2()
