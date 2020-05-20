import random
start = input('请决定随机数字范围开始值： ') #由用户确定起始值
end = input('请决定随机数字范围结束值： ')   #由用户确定结束值
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0             # 设定计数，猜了几次
while True:
	count += 1         #增加计数器
	num = input('请猜数字： ')
	num = int(num)
	if num == r:
		print('终于猜对了！ ')
		print('这是你猜的第', count, '次')  #猜对以后，继续显示猜了几次
		break
	elif num > r:
		print('您的数字比答案大！ ')
	elif num < r:
		print('您的数字比答案小！ ')
	print('这是你猜的第', count, '次')      #共计猜了几次
		