#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
		#如果不想顯示'商品,價格，不要加進去項目
			continue
			#遇到'商品,價格'，跳過這一次，直接讀下次，不是結束回圈break
		name, price = line.strip().split(',')
		products.append([name, price])
		#不能把continue放在這裡，不然等於跑完迴圈了才要跳，沒有意義，沒有跳過這一次的意義
print(products)
		#因為split分成兩個直接存
		# 或者 name = s[0]
		# 或者price = s[1]
#每個字串，先把換行strip去掉，用逗點','當作切點
while True:
	name = input('請輸入商品名稱')
	if name == 'q':
		break
	price = input('請輸入商品價格')
	price = float(price)
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

with open('products.csv', 'w', encoding='utf-8') as f:
#打開文件檔寫入 當作"f""，要先確定編碼，不然sublime會亂碼(放到excel好像沒差)
	f.write('商品,價格\n')
#直接寫入項目的欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
#把商品名＋逗點＋價格＋換行 寫入f資料夾
#寫入csv檔 逗點可以分格
#之前把價格的字串存成浮點數，需改成字串str才能用加法