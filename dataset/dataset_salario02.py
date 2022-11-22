f = open('dataset/salario.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]
count = 0

print(full_data)