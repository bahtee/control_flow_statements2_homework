def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer=''
    if a<b and a<c:
        answer= a
    if b < a and b<c:
        answer= b
    if c<a and c<b :
        answer= c      
    return answer
print(main(5,3,1))    