def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer= ''
    if (a < b and c > b) or (a>b and b>c):
        answer= b
    if (a >b and c > a) or (a<b and a>c):
        answer= a
    if c > a and c< b:
        answer = c
        


    return answer
print(main(5,44,31))

