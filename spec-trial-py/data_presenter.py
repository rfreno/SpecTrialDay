import csv
with open('CupcakeInvoices.csv',newline='') as file:
    reader = csv.reader(file, delimiter=',')
    total = 0
    for row in reader:
        current = float(row[3]) * float(row[4])
        total += current
    print(total)
    
    # print each row
        # print(' '.join(row))
    # type of cupcakes purchased
        # print(''.join(row[2]))
    # Total for each invoice
        # total = float(row[3]) * float(row[4])
        # print(total)
    # Total for all invoices combined     
    