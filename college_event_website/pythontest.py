from datetime import datetime

now = datetime.now()
today8am = now.replace(hour=13, minute=30, second=0, microsecond=0)

print(now)
if now < today8am:
    print("true")
else:
    print("false")