import textwrap

# def wrap(string, max_width):
#     for i in range(0, len(string), max_width):
#         print(string[i:i + max_width])

def wrap(string, max_width):
    return(textwrap.fill(string, max_width))


# input >>  ABCDEFGHIJKLIMNOQRSTUVWXYZ 4
# output >> ABCD
#           EFGH
#           IJKL
#           IMNO
#           QRST
#           UVWX
#           YZ
