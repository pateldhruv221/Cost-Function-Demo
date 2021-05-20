import numpy as np

# NOTE: Program assumes no data validation required

# FUNCTIONS
def h(coefficients, x): # hypothesis function
    output = 0

    for i in range(len(coefficients)):
        output += coefficients[i]*(x**i)

    return output

def J(m, h, coefficients, data_set): # cost function
    cost = 0

    for i in range(m):
        cost += (h(coefficients, data_set[i,0]) - data_set[i, 1])**2

    cost = cost/(2*m)

    return cost

# INTRO
print("\nDemonstration of the Squared Error Cost Function using 2D Regression")
print("--------------------------------------------------------------------\n")

# extracting data from text file
data_set = []

with open("data_set.txt", "r") as data_set_file:
    print("Parsing data provided in file...")

    for i, point in enumerate(data_set_file):
        if i > 2: # start reading at the 3rd line
            # processing line and adding the elements to the training set
            data_set.append(point.strip().split())

    print("...Parsing complete\n")

data_set = np.array(data_set, dtype="float")
print(f"Inputted data set:\n{data_set}\n")
m = data_set.shape[0]

# generating hypothesis function
degree = int(input("Enter the degree of your desired hypothesis function: "))

coefficients = np.zeros(degree+1, dtype="float")
for i in range(coefficients.size):
     coefficient = float(input(f"Enter coefficient t{i}: "))
     coefficients[i] = coefficient

# portraying selection of hypothesis function
print("\nHypothesis function: ",end="")
i = 0
while i <= degree:
    if i == degree:
        print(f"{coefficients[i]}x^{i}")
    else:
        print(f"{coefficients[i]}x^{i} + ",end="")

    i += 1

print(f"Cost = {J(m, h, coefficients, data_set):.4f} (to 4 decimal places)")
