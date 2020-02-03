products = []
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

products[0][0]


#四三行變一行，p = [name, price]
#三行變一行，products.append([name, price])