def freq_digit(num: int) -> int:
	from collections import defaultdict
	d = defaultdict(int)
	for e in str(num):
		d[e] += 1
	d = sorted(d, key=d.get, reverse=True)
	return int(d[0])
	