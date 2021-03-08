import os  # operating system 載入作業系統

products = []

if os.path.isfile('products.csv'):  # 檢查檔案在不在
    print('Yeah! 找到檔案了!')
    # 讀取檔案
    with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品種類, 價格' in line:
            continue  # continue省略這一回後面的內容，跳到下一回繼續（不是跳出迴圈，break才是逃出回圈）通常放在loop裡面很高的位置，因為這樣才有東西可以跳過
        name, price = line.strip().split(',')
        products.append([name, price])
        # print(type(line.strip().split(',')))  # split()切割完的結果是清單
else:
    print('找不到檔案...')


# 讓使用者輸入
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':  # quit
        break
    price = input('請輸入商品價格：')
    # p = []  p.append(name)  p.append(price)     #p = [name, price] products.append(p)
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格為', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品種類,價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')
