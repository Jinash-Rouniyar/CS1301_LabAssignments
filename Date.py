from datetime import date

class Date:
	# Constructor
	def __init__(self, m, d, y):
		self.month = m
		self.day = d
		self.year = y

	def leap_year(self):
		return ((self.year%4 == 0) and not (self.year%100 == 0 and self.year%400 != 0))

	# To implement this class method, you can use Python's datetime package
	@classmethod
	def today(cls):
		d = str(date.today())
		temp=  d.split("-")
		return Date(int(temp[1]),int(temp[2]),int(temp[0]))

	# returns day of week as a String ("Sunday", "Monday", ...)
	def day_of_weekS(self):
		d = self.day_of_weekN()
		match d:
			case 0:
				return "Sunday"
			case 1:
				return "Monday"
			case 2:
				return "Tuesday"
			case 3:
				return "Wednesday"
			case 4:
				return "Thursday"
			case 5:
				return "Friday"
			case 6:
				return "Saturday"
	def month_string(self,m):
		my_dict = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
		return my_dict[m]
	#Source of code: https://artofmemory.com/blog/how-to-calculate-the-day-of-the-week/
	# returns day of week as a number (0 for "Sunday", 1 for "Monday", ...)
	def day_of_weekN(self):
		a = self.year
		m = self.month
		d = self.day

		d1 = (1+5*((a-1)%4) + 4*((a-1)%100) + 6*((a-1)%400))%7
		if ((a%4 == 0) and not (a%100 == 0 and a%400 != 0)):
			dmap = {1:0,2:3,3:4,4:0,5:2,6:5,7:0,8:3,9:6,10:1,11:1,12:6}
		else:
			dmap = {1:0,2:3,3:3,4:6,5:1,6:4,7:6,8:2,9:5,10:0,11:3,12:5}

		m1 = dmap[m]
		final = ((d1+m1+d)-1)%7
		return final
		
	# Returns the Date object one day after self
	def tomorrow(self):
		return self.add(1)

	# Returns the Date object obtained by adding ndays to self
	def add(self,ndays):
		day = self.day
		month = self.month
		year = self.year
		months_31 = [1,3,5,7,8,10,12]
		months_30 = [4,6,9,11]
		if self.leap_year():
					feb = 29
		else: feb = 28
		
		for _ in range(ndays):
			if day < feb:
					day += 1
			elif day == feb and month == 2:
					month += 1
					day = 1
			elif day == 30 and month in months_30:
					month += 1
					day = 1
			elif day == 31 and month in months_31:
					if month == 12:
							year += 1
							month = 1
							day = 1
							if (year%4 == 0) and not (year%100 == 0 and year%400 != 0):
								feb = 29
							else: feb = 28
					else:
							month += 1
							day = 1
			else:
					day += 1
		return Date(month,day,year)

	# Returns True if self is after d
	def after(self,d):
		if self.year > d.year:
			return True
		else:
			if self.month > d.month:
				return True
			else:
				if self.day > d.day:
					return True
				else: 	
					return False

	# Returns True if self is same as d
	def equals(self,d):
		if self.year == d.year and self.month == d.month and self.day == d.day:
			return True
		else:
			return False

	# Returns True if self is before d
	def before(self,d):
		if self.year < d.year:
			return True
		else:
			if self.month < d.month:
				return True
			else:
				if self.day < d.month:
					return True
				else:
					return False

	# Returns the number of days between self and d
	def days_between(self,d):
		if self.before(d):
			temp_year = self.year
			temp_month = self.month
			temp_day = self.day
			counter = 0

			while True:
				if temp_year == d.year and temp_month == d.month and temp_day == d.day:
					return counter
				counter += 1
				months_31 = [1,3,5,7,8,10,12]
				months_30 = [4,6,9,11]
				if (temp_year%4 == 0) and not (temp_year%100 == 0 and temp_year%400 != 0):
							feb = 29
				else: feb = 28

				if temp_day < feb:
					temp_day += 1
				elif temp_day == feb and temp_month == 2:
						temp_month += 1
						temp_day = 1
				elif temp_day == 30 and temp_month in months_30:
						temp_month += 1
						temp_day = 1

				elif temp_day == 31 and temp_month in months_31:
						if temp_month == 12:
								temp_year += 1
								temp_month = 1
								temp_day = 1
								if (temp_year%4 == 0) and not (temp_year%100 == 0 and temp_year%400 != 0):
									feb = 29
								else: feb = 28
						else:
								temp_month += 1
								temp_day = 1
				else:
						temp_day += 1
		elif self.equals(d):
			return 0
		else:
			return -1
		
	def __str__(self):
		return str(f"{self.day} {self.month_string(self.month)}, {self.year}")
