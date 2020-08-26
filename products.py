import  os  #operation system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename,'r', encoding = 'utf-8') as f:
	    for line in f:
	        if '商品,價格' in line:
	            continue  #繼續 跳到下一回 第7,8行不執行
	        name, price = line.strip().split(',')

            products.append([name, price])
	return products

		
#products = []

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q' :
            break
        price = input('請輸入價格: ')
        p = [name, price]
        products.append(p)
    print(products)

#印出商品價格
def print_products(products):
    for p in products:
	    print(p[0], '的價格是', p[1])

#寫入商品價格
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
	    f.write('商品,價格\n')
	    for p in products:
		    f.write(p[0] + ',' + p[1] + '\n')

def main():
    if os.path.isfile(filename):
	    print('yeah!找到檔案了')
        products = read_file('products.csv')
    else:
        print('找不到檔案')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()