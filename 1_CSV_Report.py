import csv
file= r"C:\temp\expenses.csv"
all_expen = []

def all_expenses():
    with open(file,mode='r',encoding='ascii',newline='') as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            if not row[2]:
                continue
            try:
                clean_amount=abs(float(row[2].replace('$','').replace(" ",'').strip()))
                clean_description=row[1].strip()
                clean_category=row[3].strip()

                transaction={
                    'Date':row[0],
                    'Description':clean_description,
                    'Amount':clean_amount,
                    'Category':clean_category
                }
                all_expen.append(transaction)
            except ValueError:
                pass

all_expenses()

def get_count(the_list):
    return len(the_list)

row_count=get_count(all_expen)
print(f'{"Total Transactions:":<22} {row_count:>5,.2f}')

def get_amount(the_list):
    total=0.0
    for row in the_list:
        total+= row['Amount']
    return total

total_amount=get_amount(all_expen)
print(f'{"Total Amount Spent:":<22} ${total_amount:>5,.2f}')

def avg_transaction(the_list):
    return total_amount/row_count

average_trans= avg_transaction(all_expen)
print(f'{"Average Transaction:":<22} ${average_trans:>5,.2f}')

def highest(the_list):
    highest_value=0.0
    highest_name=None
    for row in the_list:
        if row['Amount']>highest_value:
            highest_value=row['Amount']
            highest_name=row['Category']
    return highest_value,highest_name

highest_val,highest_item = highest(all_expen)
print(f'{"Highest Purchase Was:":<22} ${highest_val:.2f}, {"Item:":.5} {highest_item}')

def lowest(the_list):
    lowest_value=float('inf')
    lowest_name=None
    for row in the_list:
        if row['Amount']==0:
            continue
        if row['Amount']<lowest_value:
            lowest_value=row['Amount']
            lowest_name=row['Category']
    return lowest_value,lowest_name

lowest_val,lowest_item = lowest(all_expen)
print(f'{"Lowest Purchase Was:":<22} ${lowest_val:.2f}, {"Item:":.5} {lowest_item}')

def spend_on_count(the_list):
    food=transport=entertainment=shopping=health=utilities=software=0
    for row in the_list:
        cat = row['Category'].upper()
        if cat == 'FOOD':
            food += 1
        elif cat == 'TRANSPORT':
            transport += 1
        elif cat == 'ENTERTAINMENT':
            entertainment += 1
        elif cat == 'SHOPPING':
            shopping += 1
        elif cat == 'HEALTH':
            health += 1
        elif cat == 'UTILITIES':
            utilities += 1
        elif cat == 'SOFTWARE':
            software += 1
        
    result={
        'Food':food,
        'Transport':transport,
        'Entertainment':entertainment,
        'Shopping':shopping,
        'Health':health,
        'Utilities':utilities,
        'Software':software
    }
    sorted_amount=sorted(result.items(),key=lambda x:x[1], reverse=True)
    return sorted_amount

final_ranking = spend_on_count(all_expen)
print(f'\n{"Category":^15}| {"Count":^9}')
print(f'-'*30)
for category,count in final_ranking:
    print(f'{category:<15}: {f"{count:}":>9}')

def spend_on_count(the_list):
    food=transport=entertainment=shopping=health=utilities=software=0.0
    for row in the_list:
        amount=row['Amount']
        cat = row['Category'].upper()
        if cat == 'FOOD':
            food += amount
        elif cat == 'TRANSPORT':
            transport += amount
        elif cat == 'ENTERTAINMENT':
            entertainment += amount
        elif cat == 'SHOPPING':
            shopping += amount
        elif cat == 'HEALTH':
            health += amount
        elif cat == 'UTILITIES':
            utilities += amount
        elif cat == 'SOFTWARE':
            software += amount
        
    result={
        'Food':food,
        'Transport':transport,
        'Entertainment':entertainment,
        'Shopping':shopping,
        'Health':health,
        'Utilities':utilities,
        'Software':software
    }
    sorted_amount=sorted(result.items(),key=lambda x:x[1], reverse=True)
    return sorted_amount

final_ranking = spend_on_count(all_expen)
print(f'\n{"Category":^15}| {"Amount":^9}')
print(f'-'*30)
for category,count in final_ranking:
    print(f'{category:<15}: {f"{count:,.2f}":>9}')


def first_tran(the_list):
    min_date='9999-01-01'
    min_name=None
    for row in the_list:
        if not row['Date']:
            continue
        if row['Date']<min_date:
            min_date=row['Date']
            min_name=row['Category']
    return min_date,min_name

start_date,start_name=first_tran(all_expen)
print(f'\nFirst Transaction On: {start_date}, Item: {start_name}')

def last_tran(the_list):
    max_date='0001-01-01'
    max_name=None
    for row in the_list:
        if not row['Date']:
            continue
        if row['Date']>max_date:
            max_date=row['Date']
            max_name=row['Category']
    return max_date,max_name

end_date,end_name=last_tran(all_expen)
print(f'Last Transaction On: {end_date}, Item: {end_name}')
