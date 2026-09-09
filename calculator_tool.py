def calculate_percentage(obtained, total):
    if total == 0:
        return 0
    return round((obtained / total) * 100, 2)
