from datetime import datetime, timedelta

# Task 1: Subtract five days from current date
current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Five days ago was:", five_days_ago)

# Task 2: Print yesterday, today, and tomorrow
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)
print("Yesterday was:", yesterday)
print("Today is:", current_date)
print("Tomorrow will be:", tomorrow)

# Task 3: Drop microseconds from datetime
current_date_without_microseconds = current_date.replace(microsecond=0)
print("Current date without microseconds:", current_date_without_microseconds)

# Task 4: Calculate difference between two dates in seconds
date1 = datetime(2023, 1, 1, 0, 0, 0)
date2 = datetime(2023, 1, 2, 12, 0, 0)
difference_in_seconds = (date2 - date1).total_seconds()
print("Difference between date1 and date2 in seconds:", difference_in_seconds)
