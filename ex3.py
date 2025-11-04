def calculate_final_price(amount, has_discount_card, is_holiday):
    base_discount = 0
    
    if has_discount_card:
        base_discount += 5
    
    if is_holiday:
        base_discount += 3
    
    amount_discount = 0
    if amount >= 30000:
        amount_discount = 10
    elif amount >= 20000:
        amount_discount = 7
    elif amount >= 15000:
        amount_discount = 5
    elif amount >= 5000:
        amount_discount = 3
    
    total_discount = base_discount + amount_discount
    
    if total_discount > 15:
        total_discount = 15
    
    final_price = amount - (amount * total_discount / 100)
    
    return round(final_price, 2)
