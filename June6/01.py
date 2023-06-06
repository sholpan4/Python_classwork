def get_seconds (hours, minutes, seconds):
    sec_in_min = minutes * 60  #minutes *= 60
    sec_in_hours = hours * 60 * 60 
    return sec_in_hours + sec_in_min + seconds

total = get_seconds (2, 30, 5)
print(total)
