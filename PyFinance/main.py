#import file and specify path location (file source and output file)
import os
import csv

#Declare Variable (Total_Month, profitloss_change, Greatest_Increase, Greatest_Decrease)
total_months = 0
total_revenue = 0

prev_revenue=0
profitloss_changes=0

greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

#create a list to compile all the revenue change
profitloss_changes=[]

output_file=os.path.join('.','output.txt')

csvpath = os.path.join('.', 'budget_data.csv')
with open('budget_data.csv', encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:
        #calculate total_months
        total_months = total_months + 1
        total_revenue = total_revenue + int(row['Profit/Losses'])

             


        #calculate average revenue change
        prev_revenue = int(row['Profit/Losses'])
        revenue_change = int(row['Profit/Losses']) - prev_revenue

        #max revenue change
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]
    
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]

        
        #new list for revenue change
        profitloss_changes.append(int(row['Profit/Losses']))
    
    #formula for average revenue
    revenue_avg = sum(profitloss_changes) / len(profitloss_changes)

        

        #print total_months and total_revenue
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")

    #print total_months
    print("Total Months: " + str(total_months))
    #print total_revenue
    print("Total Revenue: " + "$" + str(total_revenue))
    #print average_change with 2 decimal after comma
    print("Average Change: " + "$" + str(round(sum(profitloss_changes) / len(profitloss_changes),2)))
    #print greatest_increase
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    #print greatest decrease
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")




    # Output Files
with open(output_file, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(profitloss_changes) / len(profitloss_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")