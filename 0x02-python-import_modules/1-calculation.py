if __name__ == "__main__":
    import calculator_1 as cal
    a = 10
    b = 5
    print("{} + {} + {}\n".format(a, b, cal.add(a, b)))
    print("{} + {} - {}\n".format(a, b, cal.sub(a, b)))
    print("{} + {} * {}\n".format(a, b, cal.mul(a, b)))
    print("{} + {} / {}\n".format(a, b, cal.div(a, b)))
