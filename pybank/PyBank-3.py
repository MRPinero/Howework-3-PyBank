import os #this line work
import csv #this line work

Months = []
Profit_Losses = []

budget_data = os.path.join('..', '..', 'python-challenge', 'budget_data.csv') 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    row_count = 0
   
    for row in csvreader:
        Months.append(row[0])
        Profit_Losses.append(row[1])
        #print(row)

print("__________________________________________")

#ELIMINATE HEADERS AND PREPARE LISTS BY COLUMN NAME
    
print("__________________________________________")

#CALCULATE TOTAL NUMBER OF MONTHS
Total_number_of_months= len(Months)
print("Total number of months:", Total_number_of_months)

#CALCULATE NET TOTAL AMOUNT OF PROFIT/LOSSES
Net_total_ammount_of_profit_losses = int(sum(Profit_Losses, 0))
print ("Net total amount of profit/losses:", Net_total_ammount_of_profit_losses)

#AVERAGE OF THE CHANGES IN PROFIT/LOSSES
Total_Revenue = []
#Average_Profit_Losses.append(row[1])

Total_Revenue = 0
count = 0
for row in csvreader:
    count +=1 
    revenue = float(row[1])
    Total_Revenue = Total_Revenue + revenue

print ("Average of the changes:", Total_Revenue )

#FIND GREATEST INCREASE
Greatest_increase = Max(Total_Revenue)
print ("Greatest increase in Profit/Losses:", Total_Revenue)
     
#FIND GREATEST DESCREASE
Greatest_decrease = min(Total_Revenue)
print ("Greatest decrease in Profit/Losses:", Total_Revenue)

#Average_Profit_Losses = [Profit_Losses]-[Profit_Losses].shift(1)
#Average_Profit_Losses = Sum(Average_Profit_Losses, 0 )
#print (Average_Profit_Losses)





#for row in budget_data
    #count +=1   
#print = count

#net amount of profit/losses over entire period
#
#     

