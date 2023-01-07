numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def count_digits(string: str) -> int:
    """
    Count the number of digits in a string of fixed length.
    args:
        string: string of fixed length
    returns:
        number of digits in the string
    """

    # Your code goes here
    sum = 0
    for n in string:
        if n in numbers:
            sum += 1
        else:
            sum += 0
    return sum


print(count_digits('3 4 5 7 9 , 4'))
