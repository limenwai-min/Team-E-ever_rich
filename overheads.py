def overhead_function():

    from pathlib import Path
    import csv

    # create path to overheads csv file
    overheads_path = Path.home()/'Team_E'/'csv_reports'/'Overheads.csv'


    # read csv file
    with overheads_path.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create empty list to store the csv data
        overheads_records = []

        # append data from csv file into the list
        for row in reader:
            overheads_records.append(row)


    # create variable to store highest overhead category
    highest_overhead = 0

    # create variable to store highest expense
    highest_expense = 0


    for row in overheads_records:
    # assign variables to their respective values
        expense_type = row[0]
        percentage_expense = float(row[1])

    # if percentage_expense is higher than current value of highest_expense, 
    # it will replace the current highest_expense, and the expense_type will 
    # replace the current highest_overhead
        if percentage_expense > highest_expense:
            highest_overhead = expense_type
            highest_expense = percentage_expense

    # print the highest overhead category and its respective value
    return(f'[HIGHEST OVERHEAD] {highest_overhead}:{highest_expense}%\n')

print(overhead_function())