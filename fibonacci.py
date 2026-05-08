"""
Fibonacci Series Generator
Generates the Fibonacci sequence for N terms.
"""


def fibonacci(n: int) -> list[int]:
    """Generate Fibonacci series for N terms.
    
    Args:
        n: Number of terms to generate.
        
    Returns:
        List containing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


def main():
    N = 10
    result = fibonacci(N)
    print(f"Fibonacci series for N={N}:")
    print(result)


if __name__ == "__main__":
    main()
