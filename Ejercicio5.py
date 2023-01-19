def hollow_triangle(n):
    width = n * 2 - 1
    row = '{{:_^{}}}'.format(width).format
    