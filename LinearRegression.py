import pandas as pd
import matplotlib.pyplot as plt

def csvFile(file):
    csvFile = pd.read_csv(file)
    return csvFile

data = csvFile()

def Extract_X(independent):
    data[independent] = pd.to_numeric(data()[independent], errors='coerce')
    x = data[independent]
    return x

def Extract_Y(dependent):
    data[dependent] = pd.to_numeric(data()[dependent], errors='coerce')
    y = data[dependent]
    return y
    
x = Extract_X()
y = Extract_Y()

# Calculate the coefficients for the linear regression
mean_x = x.mean()
mean_y = y.mean()
xy = (x*y).mean()
x_squared = (x**2).mean()

m = (xy - mean_x * mean_y) / (x_squared - mean_x ** 2)
b = mean_y - m * mean_x
# Equation for linear regression
equation = f'y = {m:.2f}x + {b:.2f}'
# Predicted values based on the regression line
y_pred = m*x+b

def plot():
    # PLot Scatter Plot of the Data Points
    plt.scatter(x,y,label="Data Points")
    # Plot the Regression Line
    plt.plot(x, y_pred, color="red", Label="Regression Line")

    plt.xlabel('Independent Variable')
    plt.ylabel('Dependent Variable')
    plt.title('Linear Regression')

    plt.text(0.1,0.9, equation, transform=plt.gca().transAxed, fontsize=12)
    #Show the plot
    plt.show()