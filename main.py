import cash_on_hand,  overheads, profit_loss

from pathlib import Path

# created a list containing the functions
summary = [overheads.overhead_function(),
           cash_on_hand.coh_function(),
           profit_loss.profitloss_function()]


# created a new text file under the same folder
new_file = Path.cwd()/'summary_report.txt'
new_file.touch()

# wrote the contents of summary into the text file
with new_file.open(mode='w') as report:
    for line in summary:
        report.write(line)