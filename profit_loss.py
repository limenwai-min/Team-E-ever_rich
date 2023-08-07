def profitloss_function():

    '''
    - This function computes the difference in net profit if net profit on current day is lower than previous day.
    - If net profit is always increasing, the function finds the day and amount the highest increment occurs.
    - Required paramaters : none
    '''

    from pathlib import Path
    import csv

    # create path to folder containing csv files
    profitLoss_path = Path.home()/'Team_E'/'csv_reports'/'Profits_and_Loss.csv'
    # profitLoss_path = Path.home()/'Team_E'/'csv_reports'/'test_ProfitAlwaysIncreasing.csv'


    # read csv file
    with profitLoss_path.open(mode='r', encoding='UTF-8', newline='') as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create empty list to store the csv data
        profitLoss_records = []

        # append data from csv file into the list
        for row in reader:
            profitLoss_records.append(row)


    # Create empty list to store potential days with profit deficits,
    # and list to store differences between net profit on each day
    profit_deficit_days = []
    netProfit_differences = []

    # Create variable to store potential 'day with highest increment'
    highest_increment_day = 0

    # assign variable to first 'net profit of previous day'
    previous_netProfit = int(profitLoss_records[0][4])

    # create variable to store potential 'highest increment in net profit'
    highest_increment = 0


    for row in profitLoss_records:
        # assign variables to their respective data
        day = int(row[0])
        net_profit = int(row[4])

        # Find difference in net profit and append into list of netProfit_differences
        difference = net_profit - previous_netProfit
        netProfit_differences.append(difference)

        # Append days with profit loss into list of profit_deficit_days
        if difference < 0:
            profit_deficit_days.append((day, abs(difference)))

        # If there is positive profit, assign the value to highest_increment
        # Every time a higher than before profit increase is calculated, it 
        # replaces the previous value of highest_increment
        elif difference > highest_increment:
            highest_increment = difference
            highest_increment_day = day
        
        # current day's net profit becomes previous day's net profit
        previous_netProfit = net_profit


    # create variable to be returned at end of function
    profitloss_summary = ''

    # if there are days with profit deficit, add them to profitloss_summary
    for day, deficit in profit_deficit_days:
        profitloss_summary += (f"[PROFIT DEFICIT] Day: {day}, AMOUNT: USD{deficit}\n")


    # sum up negative differences in net profit
    # sum_negative_profits = 0
    # for difference in netProfit_differences:
    #     if difference < 0:
    #         sum_negative_profits += difference

    # # if sum is 0, there are no days with negative profits, and 
    # # profits are always increasing.
    # if sum_negative_profits == 0:
    #     profitloss_summary += ('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n')


    # if there are no days with negative difference in net profit, 
    # profit_deficit_days remains empty
    if profit_deficit_days == []:
        profitloss_summary += ('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n')
        # add day of highest increase in profit and amount to profitloss_summary
        profitloss_summary += (f'[HIGHEST NET PROFIT SURPLUS] DAY: {highest_increment_day}, AMOUNT: USD{highest_increment}\n')

    return profitloss_summary

print(profitloss_function())