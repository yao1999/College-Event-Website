from datetime import datetime, date, time

year = "2022"
month = "10"
day = "01"
start_time = "10:20"
exam_date = datetime.strptime(year + "-" + month + "-" + day + " " + start_time,'%Y-%m-%d %H:%M')
today = datetime.now()

print(today)
print(exam_date)

if today < exam_date:
    print("before")
else:
    print("after")

<class 'django.db.models.query.QuerySet'>
<class 'Events.models.Event'>



