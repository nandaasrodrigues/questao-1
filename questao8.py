def multiplication_table(n):
    header_fmt = '{{:>{}}}'.format(4)
    
    print(header_fmt.format(''), end = '')
    print(header_fmt.format(''), end = '')
    for k in range(1, n+1):
        print(header_fmt.format(k), end = '')
    print('\n')
    print(header_fmt.format(':'), end = '')
    print('-'*((n+1)*4), end = '')
    print('\n')
    for i in range (1, n+1):
        print(header_fmt.format(str(i)+':'), end = '')
        print(header_fmt.format(''), end = '')
        for j in range(1, n+1):
            print(header_fmt.format(i*j), end = '')
        print('\n')

multiplication_table(12)