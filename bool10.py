from math import sqrt
def main(a):
    """
    check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return sqrt(a)==int(sqrt(a))
print(main(4))