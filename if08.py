def main(number):
    """
    Return the days of the week, return the days of the week according to the numbers 1 to 7.
    Use the elif statments.
    1: "Monday"
    2: "Tuesday"
    3: "Wednesday"
    4: "Thursday"
    5: "Friday"
    6: "Saturday"
    7: "Sunday"
    Args:
        number: Number of the day.
    Returns:
        str: return answer.
    """
    answer='1 dan 7 gacha bolgan son kiriting'
    if number==1:
        answer='Monday'
    if number==2:
        answer='Tuesday'
    if number == 3:
        answer = 'Wednesday'
    if number == 4:
        answer='Thursday'
    if number == 5 :
        answer='Friyday'
    if number == 6:
        answer='Saturday' 
    if number == 7:
        answer='Sunday'   
    return answer
print(main(99))