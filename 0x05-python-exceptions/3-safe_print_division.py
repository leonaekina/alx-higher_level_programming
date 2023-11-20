afe_print_division(a, b):
    try:
        division = a / b
    except (ZeroDivisionError, TypeError):
        division = None
    finally:
        print("Inside result: {}".format(division))
    return (division)
