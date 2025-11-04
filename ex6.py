def process_message(message):
    if len(message) > 160:
        return message[:160]
    else:
        return message
