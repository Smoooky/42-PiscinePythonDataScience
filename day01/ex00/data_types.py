#!/usr/bin/python3

def data_types():
    variables = (
        1,                          # int
        'some text',                # str
        4.2,                        # float
        True,                       # bool
        [1, 2, 3, '100'],           # list
        {'first': 1, 'second': 2},  # map
        (1, 'asd', True),           # tuple
        {1, 5, 3, 4, 6}             # set
    )
    output = '['
    for var in variables:
        output += type(var).__name__ + ', '
    output = output[:-2] + ']'
    print(output)


if __name__ == '__main__':
    data_types()
