def is_valid_date(month, day, year):
    if month < 1 or month > 12:
        return False, "Invalid format"
    
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month-1]:
        return False, "Invalid format"
    
    if year < 1000 or year > 9999:
        return False, "Invalid format"
    
    return True, "Invalid format"

def is_valid_time(hour, minute, second):
    if hour < 0 or hour > 23:
        return False, "Invalid format"
    
    if minute < 0 or minute > 59:
        return False, "Invalid format"
    
    if second < 0 or second > 59:
        return False, "Invalid format"
    
    return True, ""

def convert_to_12_hour_format(hour, minute, second):
    if hour == 0:
        period = "AM"
        hour_12 = 12
    elif hour < 12:
        period = "AM"
        hour_12 = hour
    elif hour == 12:
        period = "PM"
        hour_12 = 12
    else:
        period = "PM"
        hour_12 = hour - 12
    
    return f"{hour_12}:{minute:02d}:{second:02d} {period}"

def format_date_time(date_time_str):
    
    parts = date_time_str.split()
    if len(parts) != 2:
        print("Invalid format")
        return
    
    date_part, time_part = parts
    
    date_parts = date_part.split('/')
    if len(date_parts) != 3:
        print("Invalid format")
        return
    
    month_str, day_str, year_str = date_parts
    
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        print("Invalid format")
        return
    
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    
    is_date_valid, date_error = is_valid_date(month, day, year)
    if not is_date_valid:
        print(date_error)
        return
    
    time_parts = time_part.split(':')
    if len(time_parts) != 3:
        print("Invalid format")
        return
    
    hour_str, minute_str, second_str = time_parts
    
    if not (hour_str.isdigit() and minute_str.isdigit() and second_str.isdigit()):
        print("Invalid format")
        return
    
    hour = int(hour_str)
    minute = int(minute_str)
    second = int(second_str)
    
    is_time_valid, time_error = is_valid_time(hour, minute, second)
    if not is_time_valid:
        print(time_error)
        return
    
    formatted_date = f"{day:02d}.{month:02d}.{str(year)[-2:]}"
    
    formatted_time = convert_to_12_hour_format(hour, minute, second)
    
    print(f"{formatted_date} {formatted_time}")
