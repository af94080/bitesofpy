from collections import Counter

def freq_digit(num: int) -> int:
	cnt = Counter(str(num))
	top = int(cnt.most_common(1)[0][0])
	return top

def freq_digit_2(num: int) -> int:
    return int(Counter(str(num)).most_common()[0][0])	