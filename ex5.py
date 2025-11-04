def calcul_value():
    num = int(input())
    match num:
        case 5 | 10:
            print(num)
        case 25:
            print(28)
        case 50:
            print(58)
        case 100:
            print(120)
        case _:
            print("error")
