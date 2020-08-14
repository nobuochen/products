#讀取檔案
products = []
with open('products.csv','r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue  #繼續 跳到下一回
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)		
#products = []

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q' :
        break
    price = input('請輸入價格: ')
#    p = []
#    p.append(name)
#    p.append(price)
#    products.append(p)
    p = [name, price]
    products.append(p)
print(products)

#印出商品價格
for p in products:
	print(p[0], '的價格是', p[1])

#寫入商品價格
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
