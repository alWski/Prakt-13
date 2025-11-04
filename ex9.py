def is_valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 1 or day > days_in_month[month-1]:
        return False
    
    if year < 1000 or year > 9999:
        return False
    
    return True

def is_valid_time(hour, minute, second):
    if hour < 0 or hour > 23:
        return False
    
    if minute < 0 or minute > 59:
        return False
    
    if second < 0 or second > 59:
        return False
    
    return True

def calculate_seconds_since_epoch(month, day, year, hour, minute, second):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    total_days = 0
    for i in range(month - 1):
        total_days += days_in_month[i]
    
    total_days += day - 1
    
    total_seconds = total_days * 24 * 3600
    total_seconds += hour * 3600
    total_seconds += minute * 60
    total_seconds += second
    
    return total_seconds

def format_date_time(date_time_str):
    parts = date_time_str.split()
    if len(parts) != 2:
        return "Invalid format"
    
    date_part, time_part = parts
    
    date_parts = date_part.split('/')
    if len(date_parts) != 3:
        return "Invalid format"
    
    month_str, day_str, year_str = date_parts
    
    if not (month_str.isdigit() and day_str.isdigit() and year_str.isdigit()):
        return "Invalid format"
    
    month = int(month_str)
    day = int(day_str)
    year = int(year_str)
    
    if not is_valid_date(month, day, year):
        return "Invalid format"
    
    time_parts = time_part.split(':')
    if len(time_parts) != 3:
        return "Invalid format"
    
    hour_str, minute_str, second_str = time_parts
    
    if not (hour_str.isdigit() and minute_str.isdigit() and second_str.isdigit()):
        return "Invalid format"
    
    hour = int(hour_str)
    minute = int(minute_str)
    second = int(second_str)
    
    if not is_valid_time(hour, minute, second):
        return "Invalid format"
    
    total_seconds = calculate_seconds_since_epoch(month, day, year, hour, minute, second)
    
    return total_seconds
