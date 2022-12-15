import os
import csv

# files to Use
csv_path = "pybank/resources/budget_data.csv"
output_path = "pybank/analysis/profit_and_lost_analysis.txt"

# define parameters

month_of_change = []
Val_change_list = []
Gr_increase = ["", 0]
Gr_decrease = ["", 999999999999]
Total_Months = 0
Prev_Val = 0
Total_Val = 0

# Read the CSV 
with open(csv_path) as budget_data:
    csvreader = csv.reader(budget_data)

    # read the header row
    csv_header = next(csvreader)

    # Read each row of data
    for row in csvreader:

        #calculate totals
        Total_Months = Total_Months + 1

        date_string = row[0]
        value_string =  row[1]
        
        # convert above and calculate                    
        Total_Val = Total_Val + int(value_string) 
        x = int(value_string)
        vDate = date_string

        # Calculate profit & loss change
        Prof_Loss_Change = x - Prev_Val
        
        if Prev_Val != 0:
            Val_change_list.append(Prof_Loss_Change)

        Prev_Val = x
       
        month_of_change.append(vDate)

        # Calculate greatest increase
        if (Prof_Loss_Change > Gr_increase [1]):

            Gr_increase [0] = vDate
            Gr_increase [1] = Prof_Loss_Change

        # Calculate greatest decrease

        if (Prof_Loss_Change < Gr_decrease [1]):

            Gr_decrease [0] = vDate
            Gr_decrease [1] = Prof_Loss_Change

    #calculate average profit loss change
    average_change = sum(Val_change_list) / len(Val_change_list)
    average_change = round(average_change,2)
    
    #Get output
    output = (
        f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total months: {Total_Months}\n"
        f"Total : ${Total_Val}\n"
        f"Average Change : ${average_change}\n"
        f"Greatest increase : {Gr_increase [0]} (${Gr_increase [1]})\n"
        f"Greatest decrease : {Gr_decrease [0]} (${Gr_decrease [1]})\n"
    )

    #print output
    print(output) 

    # Send output to text file
    with open(output_path, "w") as txt_file:
        txt_file.write(output)




        












