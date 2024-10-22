import datetime

time = datetime.datetime(year=1970, month=1, day=1)
time_difference = datetime.datetime.now() - time
seconds = time_difference.total_seconds()
print(
    f"Seconds since {time.strftime('%B %-d, %Y')}: {seconds} or {seconds:.2E} in scientific notation"
)
