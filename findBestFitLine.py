def inputPoints(numPoin):
    points = []
    for n in range(1,numPoin + 1):
        x = "x"
        y = "y"
        x = int(input(f"Enter the x value for a point number {n}: "))
        y = int(input(f"Enter the y value for a point number {n}: "))
        point = [x, y]
        points.append(point)
        print(f"The point ({x}, {y}) was added.")
    return points

def calculateMeanOfXAndY(points):
    sumOfX = 0
    sumOfY = 0
    lenOfX = 0
    lenOfY = 0
    for i in range(0,len(points)):
        for j in range(0,len(points[i])):
            if j == 0:
                sumOfX += points[i][j]
                lenOfX += 1
            else:
                sumOfY += points[i][j]
                lenOfY += 1
    meanOfX = sumOfX / lenOfX
    meanOfY = sumOfY / lenOfY
    return meanOfX, meanOfY

def calculateSlope(meanOfX, meanOfY, points):
    numerator = []
    denominator = []
    sumOfNumerator = 0
    sumOfDenominator = 0
    for i in range(0,len(points)):
        for j in range(0,len(points[i]) - 1):
            xMinusMean = points[i][j] - meanOfX
            yMinusMean = points[i][j + 1] - meanOfY
            productOf = xMinusMean * yMinusMean
            numerator.append(productOf)
            xMinusMeanSquared = (xMinusMean) ** 2
            denominator.append(xMinusMeanSquared)
    for k in range(0,len(numerator)):
        sumOfNumerator += numerator[k]
    for l in range(0,len(denominator)):
        sumOfDenominator += denominator[l]
    return sumOfNumerator / sumOfDenominator

def findB(meanOfX, meanOfY, slope):
    b = meanOfY - slope * meanOfX
    return b

def main():
    numberOfPoints = int(input("Enter the number of points u wish to enter: "))
    points = inputPoints(numberOfPoints)
    means = calculateMeanOfXAndY(points)
    meanOfX, meanOfY = means
    slope = calculateSlope(meanOfX, meanOfY, points)
    b = findB(meanOfX, meanOfY, slope)
    print(f"slope = {slope}\n b = {b}")
    print(f"Equation of a line is (y = {slope:.2f}x + {b})")

main()
