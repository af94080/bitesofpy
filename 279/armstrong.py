def is_armstrong(n: int) -> bool:
    n = str(n)
    pwr = len(n)
    tot = 0
    for char in n:
        tot += int(char) ** pwr
    return n == str(tot)
