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

for product in products:
	print(product)
	print(product[0], '的價格是', p[1])

#四三行變一行，p = [name, price]
#三行變一行，products.append([name, price])

with open('products.csv', 'w') as f:
#打開文件檔寫入 當作"f""
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
#把商品名＋逗點＋價格＋換行 寫入f資料夾
#寫入csv檔 逗點可以分格
