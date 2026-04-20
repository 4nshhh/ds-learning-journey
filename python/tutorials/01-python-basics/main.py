expenses = [1200,1300,1500,1700]
total_expense = 0
# for expense in expenses:
#     total_expense += expense
#
# print(total_expense)

for i,expense in enumerate(expenses):
    print(f"Month {i+1}, expense : {expense}")
    total_expense += expense
print(f"Total : {total_expense}")





