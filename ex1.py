# Find cost per day and per month of cloud hosting

cost_per_hr = float(input("Cost per hour: "))
server_unit = int(input("Amount of servers: "))
cost_per_day = cost_per_hr * 24 * server_unit
cost_per_month = (cost_per_hr * 672 * server_unit)

print("\nStandard Price: ")
print('Cost per day:\t {0:10.2f} ฿ \nCost per month:\t {1:10.2f} ฿'.format((cost_per_day/server_unit), (cost_per_month/server_unit)) )
print("===================================================================")
print("\nTotal: ")
print('Cost per day:\t{:10.2f} ฿'.format(cost_per_day))
print('Cost per month:\t{:10.2f} ฿'.format(cost_per_month))

print("\n=================================================================")
print('{0:5}{1:11}{2:11}'.format('', 'Unit Cost', 'Grand Total'))
print('{0:5}{1:11.2f} ฿ {2:11.2f} ฿'.format('Day', (cost_per_day/server_unit), cost_per_day))
