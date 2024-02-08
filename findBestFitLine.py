import matplotlib.pyplot as plt

def inputPoints(numPoints):
    points = []
    for n in range(1, numPoints + 1):
        x = float(input(f"Enter the x value for point number {n}: "))
        y = float(input(f"Enter the y value for point number {n}: "))
        point = [x, y]
        points.append(point)
        print(f"The point ({x}, {y}) was added.")
    return points

def calculateMeanOfXAndY(points):
    sumOfX = sum(point[0] for point in points)
    sumOfY = sum(point[1] for point in points)
    meanOfX = sumOfX / len(points)
    meanOfY = sumOfY / len(points)
    return meanOfX, meanOfY

def calculateSlope(meanOfX, meanOfY, points):
    numerator = sum((x - meanOfX) * (y - meanOfY) for x, y in points)
    denominator = sum((x - meanOfX) ** 2 for x, _ in points)
    return numerator / denominator

def findB(meanOfX, meanOfY, slope):
    return meanOfY - slope * meanOfX

def findYForX(slope, b, x):
    return slope * x + b

def plotLineOfBestFit(points, slope, b):
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    plt.scatter(x_values, y_values, label='Data Points')
    
    # Generate y values for the line of best fit
    x_values = [min(x_values), max(x_values)]
    y_values = [slope * x + b for x in x_values]
    plt.plot(x_values, y_values, color='red', label='Line of Best Fit')
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Line of Best Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    numberOfPoints = int(input("Enter the number of points you wish to enter: "))
    points = inputPoints(numberOfPoints)
    meanOfX, meanOfY = calculateMeanOfXAndY(points)
    slope = calculateSlope(meanOfX, meanOfY, points)
    b = findB(meanOfX, meanOfY, slope)
    print(f"Slope = {slope:.2f}")
    print(f"Y-intercept = {b:.2f}")
    print(f"Equation of the line: y = {slope:.2f}x + {b:.2f}")
    x = float(input("Enter x u wish to use to get y: "))
    y = findYForX(slope, b, x)
    print(f"The resulting point is: ({x}, {y:.2f})")
    plotLineOfBestFit(points, slope, b)

main()
