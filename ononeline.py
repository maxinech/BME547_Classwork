def input_parameter():
    print("Enter (x, y) coordinates by comma, example:  3, 2")
    point1_input = input("Enter the first coordinate: ")
    point1 = tuple(int(x) for x in point1_input.split(","))
    point2_input = input("Enter the second coordinate: ")
    point2 = tuple(int(x) for x in point2_input.split(","))
    point3_input = input("Enter the third coordinate: ")
    point3 = tuple(int(x) for x in point3_input.split(","))
    return point1, point2, point3


def judge_ononeline(point1, point2, point3):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    x3 = point3[0]
    y3 = point3[1]
    slope = (y1 - y2) / (x1 - x2)
    if y3 - y1 == slope * (x3 - x1):
        return True
    else:
        return False


if __name__ == "__main__":
    point1, point2, point3 = input_parameter()
    result = judge_ononeline(point1, point2, point3)
    print(result)
