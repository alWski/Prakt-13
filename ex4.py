def make_payment(P):
    if not isinstance(P, (int, float)):
        print("Повторить попытку")
        return
    
    if 20 <= P <= 1000:
        print('Успех')
    else:
        print('Повторить попытку')
