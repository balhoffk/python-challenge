import csv
import os

file1 = os.path.join("Resources", "budget_data.csv")
#Confirm analysis file with TA
file2 = os.path.join("analysisfile", "budget_analysis.txt")

totalmonths = 0
netpl = 0
monthofchange = []
netchangelist = []
profitmax = ["", 0]
lossmax = ["", 999999999999999999999999999999999]

with open(file1) as records:
    reader = csv.reader(records)
    header = next(reader)
    first_row = next(reader)
    totalmonths = totalmonths + 1
    #net profit/loss, previous profit/loss
    netpl = netpl + int(first_row[1])
    prevpl = int(first_row[1])

    for row in reader:

        totalmonths = totalmonths + 1
        netpl = netpl + int(row[1])
        netchange = int(row[1]) - prevpl
        prevpl = int(row[1])
        netchangelist = netchangelist + [netchange]
        monthofchange = monthofchange + [row[0]]

        if netchange > profitmax[1]:
            profitmax[0] = row[0]
            profitmax[1] = netchange

        if netchange < lossmax[1]:
            lossmax[0] = row[0]
            lossmax[1] = netchange

monthlyaverage = sum(netchangelist) / len(netchangelist)

output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {totalmonths}\n"
    f"Total: ${netpl}\n"
    f"Average  Change: ${monthlyaverage:.2f}\n"
    f"Greatest Increase in Profits: {profitmax[0]} (${profitmax[1]})\n"
    f"Greatest Decrease in Profits: {lossmax[0]} (${lossmax[1]})\n")

print(output)

# add in writing permission
with open(file2, "w") as txt_file:
    txt_file.write(output)
