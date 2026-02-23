# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

def series_sum(n: int) -> int:
    total = 0
    term = 0
    for i in range(n):
        term = term * 10 + 2
        total += term
    return total
print(series_sum(5))