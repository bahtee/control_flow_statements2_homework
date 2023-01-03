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
    if a<b:
        if a<c:
            answer= a
        else:
            answer= c
    else:
        answer= b        
    return answer
print(main(7,8,5))    