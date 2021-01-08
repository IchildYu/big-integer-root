from math import log
import time
import random

#两种方式计算
#第一种，思路源于数电中逐次逼近型A/D转换器
def root1(a, b):
	result = 0
	n = int(log(a) / log(2))
	while n >= 0 and result ** b != a:
		result ^= 1 << n
		if (result ** b > a): result ^= 1 << n
		n = n - 1
	return result

#第二种，常见二分法
def root2(a, b):
	mmin = 0
	mmax = a
	mid = a // 2
	while mmin <= mmax:
		mid = (mmin + mmax) // 2
		ppow = mid ** b
		if ppow == a: break
		elif ppow > a: mmax = mid - 1
		else: mmin = mid + 1
	return mid

#测试发现bits<=1024时第二种方法较快，bits>=2048时第一种方法较快
if __name__ == '__main__':
	random.seed()
	bits = 1024
	n = 50
	b = 3
	a = []
	print('root:')
	for i in range(n):
		a.append(random.getrandbits(bits))

	t0 = time.time()
	for i in a:
		root1(i, b)
	t0 = time.time() - t0
	print '\t', t0

	print('binroot:')
	t0 = time.time()
	for i in a:
		root2(i, b)
	t0 = time.time() - t0
	print '\t', t0
