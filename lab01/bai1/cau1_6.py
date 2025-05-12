input_str = input("Nhập X, Y: ")
dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]

# Tạo ma trận với giá trị ban đầu là 0
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]

# Gán giá trị cho từng phần tử trong ma trận
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col

print(multilist)