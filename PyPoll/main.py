import os, csv

csvpath = os.path.join('Resources', 'election_data.csv')
txt_path = os.path.join("analysis", "analysis.txt")
votes = 0
mostvotes = 0
counts = {}

# count total votes and stores number of votes for
# each candidate in dictionary
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        votes += 1
        if row[2] in counts:
            counts[row[2]] += 1
        else:
            counts[row[2]] = 1

# calculate winner, percentages for each candidate and
# writes to txt file
with open(txt_path, "w") as txtfile:    
    txtfile.write (f'Total votes: {votes}\n')    
    for name in counts:
        txtfile.write (f'{name}: {round((counts.get(name) / votes * 100), 3)}% {(counts.get(name))}\n')
        if counts.get(name) > mostvotes:
            mostvotes = counts.get(name)
            winner = name
    txtfile.write (f'Winner: {winner}\n')


# print txt file to terminal
with open(txt_path, "r") as txtfile:
    print(txtfile.read())

    

    

