from datetime import datetime, timezone, timedelta

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M'))  # string format time


user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)