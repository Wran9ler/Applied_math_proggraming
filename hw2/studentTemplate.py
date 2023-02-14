hourlyWage, total_work_hour = map(int, input().split())

if total_work_hour > 40:
    total_pay = int(1.4 * hourlyWage * (total_work_hour - 40) + (40 * hourlyWage))
else:
    total_pay = total_work_hour * hourlyWage

print(total_pay)
