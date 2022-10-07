def main(a):
    """check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    x=pow(a,1/2)
    return int(x)**2 == a

print(main(16))