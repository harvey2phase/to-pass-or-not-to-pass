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
        legend = "if you did not PASS"
        color = "b"
    else:
        legend = "if you PASSed"
        color = "g"
    plot(
        calculate_cgpa(cgpa, chours, gpa, passed, DISCRETE_OUTLIERS),
        calculate_cgpa(cgpa, chours, gpa, passed, OUTLIERS),
        color, legend,
    )

def plot(discrete_cgpa, cgpa, color, legend):
    plt.scatter(DISCRETE_OUTLIERS, discrete_cgpa, c = color, label = legend)
    plt.plot(OUTLIERS, cgpa, c = color)

cgpa = float(input("cGPA: "))
chours = float(input("Number of credit hours: "))
gpa = float(input("Numerical grade you're thinking of PASSing: "))

simulate(cgpa, chours, gpa, 0)
simulate(cgpa, chours, gpa, 1)

plt.xlim(LIM)
plt.ylim(LIM)
plt.xlabel("The grade you get in the future.")
plt.ylabel("Your new cGPA.")
plt.legend()
plt.show()
