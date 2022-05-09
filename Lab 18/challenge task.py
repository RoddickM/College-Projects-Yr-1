import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

height = [[159], [164], [169], [173], [179]]  # height of person in centimetres

weight = [[59], [66], [72.2], [75], [80]]  # corresponding  weight of person

# below are the titles and labels of the graph
plt.title("Height and Weight Correlation")
plt.xlabel("Height in Centimetres")
plt.ylabel("Weight in Kilograms")

# creates and fits/trains the model
model = LinearRegression()
model.fit(X=height, y=weight)

# plots the points to chart
plt.plot(height, weight, "k.")

# plots the regression line showing the correlation
plt.plot(height, model.predict(height), color="r")

# adds axis range for x (height) and y (shoe size)
plt.axes([150, 200, 50, 100])

# the code below applies a grid to the chart and displays it
plt.grid(True)
plt.show()
