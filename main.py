import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
sn.set()

DISCRETE_OUTLIERS = np.array([0, 1, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3])
OUTLIERS = np.linspace(0, 4.3, 1000)
LIM = (-0.1, 4.4)

def calculate_cgpa(cgpa, chours, gpa, passed, outlier):
    total = cgpa * chours + 3 * gpa * passed + outlier * 3
    return total / ((chours + 3 * passed + 3))

def simulate(cgpa, chours, gpa, passed):
    if passed:
        title = "cGPA vs. outliers if you did not PASS"
    else:
        title = "cGPA vs. outliers if you PASSed"
    plot(
        calculate_cgpa(cgpa, chours, gpa, passed, DISCRETE_OUTLIERS),
        calculate_cgpa(cgpa, chours, gpa, passed, OUTLIERS),
        title,
    )

def plot(discrete_cgpa, cgpa, title):
    plt.scatter(DISCRETE_OUTLIERS, discrete_cgpa)
    plt.plot(OUTLIERS, cgpa)
    plt.xlim(LIM)
    plt.ylim(LIM)
    plt.xlabel("The grade you get in the future.")
    plt.ylabel("Your new cGPA.")
    plt.title(title)

cgpa = float(input("cGPA: "))
chours = float(input("Number of credit hours: "))
gpa = float(input("Numerical grade you're thinking of PASSing: "))

plt.figure(0)
simulate(cgpa, chours, gpa, 0)
plt.figure(1)
simulate(cgpa, chours, gpa, 1)
plt.show()
