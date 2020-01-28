import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import pandas as pd

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


    plt.figure(1)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    for i in range(1, n_subplots + 1):
        plt.subplot(2,2,i)
        y = np.sin(i * x)
        plt.plot(x, y)

    plt.show()

def excs_3():
    x = np.linspace(0, 2 * np.pi, 500)
    y = np.linspace(0, 2 * np.pi, 500)

    xx, yy = np.meshgrid(x, y, sparse=True)

    z = np.sin(xx) + np.cos(yy)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(xx, yy, z, cmap='viridis')
    plt.show()

def excs_4():
    x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
    x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
    y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

    fig, axs = plt.subplots(2,2,figsize=(10,10))
    plt.setp(axs, xticks=np.arange(2.5, 20, step=2.5))
    
    axs[0,0].scatter(x, y1, color='black', marker='s')
    axs[0,1].scatter(x, y2, color='black', marker='s')
    axs[1,0].scatter(x, y3, color='black', marker='s')
    axs[1,1].scatter(x4,y4, color='black', marker='s')


    romans = ["I", "II", "III", "IV"]
    roman_counter = 0
    for i in range(2):
        for j in range(2):
            props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
            # place a text box in upper left in axes coords
            axs[i,j].text(0.85, 0.95, romans[roman_counter], transform=axs[i,j].transAxes, fontsize=14,
                verticalalignment='top', bbox=props)

            roman_counter += 1
    
    plt.show()

    # Lab 10.5
    print()
    print("Statistics")
    print()
    print()


    mean_1 = np.mean(y1)
    mean_2 = np.mean(y2)
    mean_3 = np.mean(y3)
    mean_4 = np.mean(y4)

    print("Mean")
    print(mean_1, mean_2, mean_3, mean_4)
    print()

    std_1 = np.std(y1)
    std_2 = np.std(y2)
    std_3 = np.std(y3)
    std_4 = np.std(y4)

    print("Standard Deviation")
    print(std_1, std_2, std_3, std_4)
    print()

    corr_1 = np.corrcoef(x, y1)[0][1]
    corr_2 = np.corrcoef(x, y2)[0][1]
    corr_3 = np.corrcoef(x, y3)[0][1]
    corr_4 = np.corrcoef(x4, y4)[0][1]

    print("Correlation coefficient")
    print(corr_1, corr_2, corr_3, corr_4)
    print()


def excs_5():
    bicimad = pd.read_csv('bicimad.csv', delimiter=';')

    age_range = bicimad["ageRange"]

    age_ranges = ["0 y 16", "17 y 18", "19 y 16", "27 y 40", "41 y 65", "66-100"]
    age_legend = []
    for item in age_ranges:
        legend_patch = Patch(color='blue', label="El usuario tiene entre " + item + " años")
        plt.legend(handles=[legend_patch], bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.hist(age_range, )
    plt.show()

excs_5()
