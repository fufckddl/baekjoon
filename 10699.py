from datetime import datetime, timedelta, timezone

tz = timezone(timedelta(hours=0))
now = datetime.now()
formatted_time = now.strftime("%Y-%m-%d")
print(formatted_time)