def coh_function():

    '''
    - This function computes the difference in cash on hand if cash on hand on current day is lower than previous day.
    - If cash on hand is always increasing, the function finds the day and amount the highest increment occurs.
    - Required paramaters : none
    '''
    
    from pathlib import Path
    import csv

    # create path to folder containing csv files
    CashOnHand_path = Path.home()/'Team_E'/'csv_reports'/'Cash_on_Hand.csv'

    # read csv file
    with CashOnHand_path.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create empty list to store the csv data
        CashOnHand_records = []

        # append data from csv file into the list
        for row in reader:
            CashOnHand_records.append(row)


    # Create empty list to store potential days with respective cash on hand deficits
    CashOnHand_deficit_days = []

    # Create variable to store potential 'day of highest increment'
    highest_increment_day = 0

    # create variable to store potential 'highest increment in cash on hand'
    highest_increment = 0

    # assign variable to first 'cash on hand of previous day'
    previous_CashOnHand = int(CashOnHand_records[0][1])


    for row in CashOnHand_records:
        # assign variables to their respective data
        day = int(row[0])
        CashOnHand = int(row[1])

        # Find difference in net profit and append into list of CashOnHand_differences
        difference = CashOnHand - previous_CashOnHand

        # Append days with decrease in cash on hand into list of CashOnHand_deficit_days
        if difference < 0:
            CashOnHand_deficit_days.append((day, abs(difference)))

        # If there is an increase in cash on hand, assign the value to highest_increment
        # Every time a higher than before cash on hand increase is calculated, it 
        # replaces the previous value of highest_increment
        elif difference > highest_increment:
            highest_increment = difference
            highest_increment_day = day
        
        # current day's cash on hand becomes previous day's cash on hand
        previous_CashOnHand = CashOnHand


    # create variable to be returned at end of function
    coh_summary = ''

    # if there are days with cash on hand deficit, print them
    for day, deficit in CashOnHand_deficit_days:
        coh_summary += (f"[CASH DEFICIT] Day: {day}, AMOUNT: USD{deficit}\n")


    # if there are no days with negative difference in cash on hand (coh always increasing), 
    # CashOnHand_deficit_days remains empty
    if CashOnHand_deficit_days == []:
        coh_summary += ('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n')
        # add day of highest increase in cash on hand and amount to coh_summary
        coh_summary += (f'[HIGHEST CASH SURPLUS] DAY: {highest_increment_day}, AMOUNT: USD{highest_increment}\n')

    return coh_summary