import random
r = random.randint(1,100)
#count = 0             # 设定计数，猜了几次
while True:
	count += 1
	num = input('请猜数字： ')
	num = int(num)
	if num == r:
		print('终于猜对了！ ')
#		print('这是你猜的第', count, '次')
		break
	elif num > r:
		print('您的数字比答案大！ ')
	elif num < r:
		print('您的数字比答案小！ ')
#	print('这是你猜的第', count, '次')
		