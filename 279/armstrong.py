def is_armstrong(n: int) -> bool:
    n = str(n)
    pwr = len(n)
    tot = 0
    for char in n:
        tot += int(char) ** pwr
    return n == str(tot)

def is_armstrong_dominic(n: int) -> bool:
	'''1) Calling str(n) twice (reuse snum to compute size)
		2) I don't think the list() conversion is necessary

		Here's mine, 
		similiar to <a href="#Martin">@Martin</a> 
		but with a generator expression 
		instead of a list:
	'''
    snum = str(n)
    size = len(snum)
    return sum(int(digit)**size for digit in snum) == n

def is_armstrong_david_colton(n: int) -> bool:
    return sum([int(num)**len(str(n)) for num in str(n)]) == n

def is_armstrong_alex(n: int) -> bool:
    return sum([pow(int(x), len(str(n))) for x in str(n)]) == n

def is_armstrong_geoff(n: int) -> bool:
    potential = str(n)
    power = len(potential)
    return n == sum(pow(int(num), power) for num in potential)


#### their solution: by daniel

def is_armstrong_official_solution_corrected(n: int) -> bool:
    summed_n = 0
    for i in str(n):
        summed_n += int(i)**len(str(n))
    return True if summed_n == n else False    


def is_armstrong_official_solution(n: int) -> bool:

    snum = str(n)
    size  = len(snum)

    total = sum(
        map(lambda x: x**size, map(int, snum))
    )

    return n == total

    # or as a one-liner
    # return n == sum(map(powered, map(int, snum)))