from datetime import datetime, timedelta

INITIAL_DATE = datetime(year=2016, month=12, day=19)
year_interval = timedelta(days=365)
hundred_day_interval = timedelta(days=100)


def gen_special_pybites_dates(start=INITIAL_DATE):
	next_100 = start
	next_year = start + year_interval
	while True:

		if next_100 < next_year: 
			yield next_100  
			next_100 += hundred_day_interval
		else:
			yield next_year
			next_year += year_interval
		

