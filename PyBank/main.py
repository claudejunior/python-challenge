
import os
import csv

# Set path for file
csvpath = os.path.join("raw", "budget_data_1.csv")

#Define variables for count
count = 0
sumofrevenue = 0
previousrevenue = 0
sumofrevenuechange = 0
changerevenue = 0
averagerevenuechange = 0
maxrevenuechange = 0
maxrevenuechangedate = 0
minrevenuechange = 0
minrevenuechangedate = 0

# Open the CSV document 
with open(csvpath, newline="") as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=",")  
    
    # Loop through the revenues column and dates column while creating the conditions
    for row in csvreader:

    #Adding the current revenue to the next revenue amount to return the sum of all revenues
        count = count + 1 
        currowrevenue = int(row["Revenue"]) 
        sumofrevenue = sumofrevenue + currowrevenue
    
    #Calculating the change in revenues for each row to find the sum of revenue changes which can be used to calculate the average of revenue changes
        if count >= 2:
            changerevenue = currowrevenue - previousrevenue
            sumofrevenuechange = sumofrevenuechange + changerevenue

    #Creating conditions to find the greatest increase in revenue changes
            if changerevenue > maxrevenuechange:
                maxrevenuechange = changerevenue
                maxrevenuechangedate = row["Date"]

    #Creating conditions to find the greatest decrease in revenue changes 
            if changerevenue < minrevenuechange:
                minrevenuechange = changerevenue
                minrevenuechangedate = row["Date"]

    #Setting the previous revenue to the current one
        previousrevenue = currowrevenue

    #Creating the formula to calculate the average revenu change 
    averagerevenuechange = sumofrevenuechange/(count-1)
                       
    #Printing the results 
    print("```")
    print("Financial Analysis")
    print("--------------------------------")
    print("Total Months:", end =" ");print(str(count))
    print("Total Revenue:", end =" ");print("$", end ="");print(str(sumofrevenue))
    print("Average Revenue Change:", end =" ");print("$", end ="");print(str(averagerevenuechange))
    print("Greatest Increase in Revenue:", end=" ");print(maxrevenuechangedate, end=" "); print("$", end ="");print(str(maxrevenuechange))
    print("Greatest Decrease in Revenue:", end=" ");print(minrevenuechangedate, end=" "); print("$", end ="");print(str(minrevenuechange))
    print("```")