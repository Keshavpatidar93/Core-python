import datetime
for i in range(1,13):
    month_name = datetime.date(2026,i,10).strftime("%B")
    print(f"month {i} : {month_name}")