import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #Set Variables
    month_count = []
    total = 0
    prev_rev = 0
    rev_change_list = []
    rev_avg = 0
    profit_tracker = 0
    greatest_increase = 0
    rev_change_month = []
   
    

    #Finding how many months in data set
    for row in csvreader:
        #Calculating total months in dataset
        month_count.append(csvreader)

        #Calculation net total amount of "Profit/Losses" over entire period
        total += int(row[1])

        #Calculation of change in "Profit/Losses" over the entire period
        
        rev_change = int(row[1]) - prev_rev
        prev_rev = int(row[1])
        rev_change_list += [rev_change]
        rev_change_month += [row[0]]
        
        #Find greatest/least profits and date
        maxChange = max(rev_change_list)
        maxChangeMonth = rev_change_month[rev_change_list.index(max(rev_change_list))]
        minChange = min(rev_change_list)
        minChangeMonth = rev_change_month[rev_change_list.index(min(rev_change_list))]
        
        

    #Actual Caculation of change in profit/losses - average minus the first row   
    rev_change_list.pop(0)
    rev_avg = sum(rev_change_list)/len(rev_change_list)


    print(f'Financial Analysis')
    print(f'----------------------------')
    print(f'Total Months: {len(month_count)}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(rev_avg,2)}')
    print(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})')
    print(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})')

with open("PyBank_Financial_Analysis.txt", "w") as f:
    print(f'Financial Analysis', file = f)
    print(f'----------------------------', file = f)
    print(f'Total Months: {len(month_count)}', file = f)
    print(f'Total: ${total}', file = f)
    print(f'Average Change: ${round(rev_avg,2)}', file = f)
    print(f'Greatest Increase in Profits: {maxChangeMonth} (${maxChange})', file = f)
    print(f'Greatest Decrease in Profits: {minChangeMonth} (${minChange})', file = f)

   
    










