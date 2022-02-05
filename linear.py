def input_parameter():
    print("Enter (x, y) coordinates by comma, example:  3, 2")
    point1_input = input("Enter the first coordinate: ")
    point1 = tuple(int(x) for x in point1_input.split(","))
    point2_input = input("Enter the second coordinate: ")
    point2 = tuple(int(x) for x in point2_input.split(","))
    point3_x_input = input("Enter x value of the third coordinate: ")
    point3_x = int(point3_x_input)
    return point1, point2, point3_x


def calculate_y(point1, point2, point3_x):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    slope = (y1 - y2) / (x1 - x2)
    point3_y = slope * (point3_x - x1) + y1
    return point3_y


def output_y(point3_y):
    print("y value of the third coordinate is {}".format(point3_y))


if __name__ == "__main__":
    point1, point2, point3_x = input_parameter()
    point3_y = calculate_y(point1, point2, point3_x)
    output_y(point3_y)
