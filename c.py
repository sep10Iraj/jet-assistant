for i in range(10):
    w=input('>>')
    n=input('>')
    m=input('>>')
    plus='+'
    x='*'
    d='-'
    new_w=int(w)
    new_m=int(m)

    if  plus in n:
        print(new_w + new_m)
        print('________________________')

    elif x in n:
        print(new_w*new_m)
        print('________________________')

    elif d in n:
        print(new_w - new_m)
        print('________________________')

    else:
        print('ERROR')