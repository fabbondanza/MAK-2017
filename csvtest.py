import csv
import time

with open('names.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow([456])
    spamwriter.writerow(['Date:',time.strftime('%m/%d/%Y')])
    spamwriter.writerow(['Time:', time.strftime('%H:%M:%S')])
    spamwriter.writerow([' '])
    spamwriter.writerow([' '])
    spamwriter.writerow([' '])
    spamwriter.writerow([' '])
    csvfile.close()