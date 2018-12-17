# Rain Calculator - Jon Peppinck

totalDays = 0
totalRain = 0

Day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# The user can enter the number of weeks they wish to record their data for rain collection
# The program will only accept positive integers (e.g. 2 weeks)
# The program will reject zero and negative numbers, TypeErrors, and ValueErrors 
# If the user enters an invalid entry (e.g. 1.67, [1, 2]) they will be prompted to Re-enter

while True:
	try:

		weeks = input("Enter the number of weeks for which rainfall should be calculated: ")
		x = int(weeks)		

		if x <= 0:
			print("Number of weeks must be at least 1")

		else:
			break

	except (ValueError, TypeError):
		print("Number of weeks must be an integer")		

# The following nested loop allows the user to enter their data for each day
# The days are repeated for the number of weeks the user enters
# If the user enters a negatie number, TypeError, or ValueError...
# They will be prompted to Re-enter (as before)


for currentWeek in range(1, x +1):
	
	for currentDay  in Day[0:7]:

		while True:
			try:
	
				dailyRainfall = input("Enter the amount of rain (in mm) for " + \
				currentDay + \
				" of week " + str(currentWeek) +": ")
				y = int(dailyRainfall)

				totalRain += y

				totalDays += 1

				if y < 0:
					print("Amount of rain must be non-negative")

					totalRain = totalRain - y

					totalDays = totalDays + y

				else:
					break
				
			except (ValueError, TypeError):
				print("Amount of rain must be an integer")

# The total rain is found by summing all of the rainfall for each day together
# The total days is found by counting the number of days data has been entered
# The if statement let's the program dismiss negative values accumulating for both totals
			
		avgRainwk = totalRain/x

		avgRain = totalRain/totalDays

# The user will see the total rainfall expressed as an integer
# The user will see the average weekly/daily rainfall rounded to two decimal places

print("\nTotal Rainfall: " + format(totalRain, "d") + " mm", \
"Average rainfall per week: " + format(avgRainwk, ".2f") + " mm", \
"Average rainfall per day: " +format(avgRain, ".2f") + " mm", sep="\n")
		
