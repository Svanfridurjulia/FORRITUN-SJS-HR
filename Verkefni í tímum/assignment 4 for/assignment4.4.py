max_days = int(input("Input max number of days: "))
target = int(input("Input dollar target: "))
days_when_amount_acquired = 0
money_counter = 0
dollars = 1

for i in range(1,max_days+1):
    money_counter = money_counter + dollars
    if target <= money_counter:
        days_when_amount_acquired = i
        break
    dollars = dollars * 2

print('Days needed:',days_when_amount_acquired)

