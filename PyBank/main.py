import os
import csv

file_location = '../../../nu-chi-data-pt-03-2020-u-c/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv'

total_months = 0
profit_loss = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

with open(file_location, "r") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    row = next(csvreader)

    previous_row = int(row[1])
    total_months += 1
    profit_loss += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    for row in csvreader:
        
        total_months += 1
        profit_loss += int(row[1])
        
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
        
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
    
    average_change = sum(monthly_change) / len(monthly_change)
    
    high = max(monthly_change)
    low = min(monthly_change)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${high})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${low})")

output_file_location = "PyBank"

with open(output_file_location, "w",) as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${low})\n")