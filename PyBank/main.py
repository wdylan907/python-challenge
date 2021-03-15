import os, csv

csvpath = os.path.join('Resources', 'budget_data.csv')
months = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
changes = []

# counts months, calculate total profits/losses
# and put initial values for changes list
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)    
    for row in csvreader:
        months += 1
        total += int(row[1])
        changes.append(int(row[1]))        

# calculate changes for each month in list    
for i in range(len(changes) - 1):
    changes[i] = (changes[i + 1] - changes[i])

# calculate average monthly change    
changes.pop(len(changes) - 1)
average_change = round(sum(changes)/len(changes), 2)

# calculate greatest increase and decrease
for number in changes:
    if number > greatest_increase:
        greatest_increase = number
        increase_index = changes.index(number) + 1
    elif number < greatest_decrease:
        greatest_decrease = number
        decrease_index = changes.index(number) + 1

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    data = list(csvreader)
      
# output to txt file
txt_path = os.path.join("analysis", "analysis.txt")
with open(txt_path, "w") as txtfile:
    txtfile.write (
        f'Months: {months}\n'
        f'Average change: {average_change}\n'
        f'Greatest increase: {data[increase_index][0]} {greatest_increase}\n'
        f'Greatest decrease: {data[decrease_index][0]} {greatest_decrease}\n')

# print txt file to terminal
with open(txt_path, "r") as txtfile:
    print(txtfile.read())
    
    




    


    



    
    


    
    



