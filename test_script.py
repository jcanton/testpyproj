"""
This script demonstrates a simple addition operation in a main function.
"""

def main() -> None:
    """
    The main function that runs the script. It performs a simple addition
    of two integers and prints the result.
    """
    print("Running main")
    a: int = 2
    b: int = 3
    c = a + b
    print(f"c = a + b = {c}")
    pass

if __name__ == "__main__":
    main()

