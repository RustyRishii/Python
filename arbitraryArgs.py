# *args    = allows you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#           * unpacking operator


def add_nums(*args):
    print(args)
    print(sum(args))


add_nums(2, 4, 5)
