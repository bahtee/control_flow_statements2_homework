def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    answer = ''
    if a<b:
        if b<c:
            answer=c
        else:
            answer=b
    else:
        answer = a            
    return answer

print(main(7,5,6))