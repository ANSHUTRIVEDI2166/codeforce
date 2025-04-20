def max_gifts(n):
    full_pairs = n // 3
    remainder = n % 3
    return full_pairs * 2 + (1 if remainder > 0 else 0)
