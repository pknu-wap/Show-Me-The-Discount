import csv

f = open('output.csv', 'w', encoding = 'utf-8', newline = '')
wr = csv.writer(f)
wr.writerow()

f.close()
