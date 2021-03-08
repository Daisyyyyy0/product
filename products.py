products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        cell = line.strip().split(',')
        name = cell[0]
        price = cell[1]
        print(cell)
        # print(type(cell))  # split()切割完的結果是清單


while True:
    name = input('請輸入商品名稱：')
    if name == 'q':  # quit
        break
    price = input('請輸入商品價格：')
    # p = []  p.append(name)  p.append(price)     #p = [name, price] products.append(p)
    products.append([name, price])
# print(products)

for p in products:
    print(p[0], '的價格為', p[1])


with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品種類,價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')
