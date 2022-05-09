import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

height = [[143], [158], [159], [164], [166], [180], [190]]  # height of people in centimetres

shoe_size = [[3.5], [4], [5], [6.5], [7], [9], [10]]  # shoe size corresponding to height

# below are the titles and labels of the graph
plt.title("Height and Shoe Size Correlation")
plt.xlabel("Height in Centimetres")
plt.ylabel("Shoe Size")

# creates and fits/trains the model
model = LinearRegression()
model.fit(X=height, y=shoe_size)

# predicts the shoe size based on the training dataset we used
size_predict = model.predict([[179]])[0][0]

# plots the points to chart
plt.plot(height, shoe_size, "k.")

# plots the regression line showing the correlation
plt.plot(height, model.predict(height), color="r")

# adds axis range for x (height) and y (shoe size)
plt.axis([100, 200, 0, 15])

# the code below applies a grid to the chart and displays it
plt.grid(True)
plt.show()

# prints the prediction of the shoe size
print(round(size_predict, 1))
