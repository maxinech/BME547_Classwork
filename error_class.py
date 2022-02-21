def calc_square_root(n):

    try:
        from my_math_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt
        print("My_calculator module not available. Using default.")
    from warnings import warn
    warn("Your are running a not so good function.")
    try:
        x = 5
        answer = sqrt(n)
        z = 10
    except TypeError:
        print("Enter something different")
    except ValueError:
        print("Do not enter a negative number")
    # except Exception:
    #     print("Exception")
    # else:
        # return answer
    print(x, z)


def main():
    print(calc_square_root(-4))


if __name__ == "__main__":
    main()
