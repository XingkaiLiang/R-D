"""
http://www.pythontab.com/html/2014/pythonhexinbiancheng_1114/910.html
"""
import sys
def merge(nums,first,middle,last):
	"""merge sort"""
	"slice the bountry
	lnums = nums[first:middle+1]
	rnums = nums[middle+1,last+1]
	lnums.append(sys.maxint)
	rnums.append(sys.maxint)
	l = 0
	r = 0
	for i in range(first,last+1):
		if lnums[l] <rnums[r]:
			nums[i] = lnums[l]
				l+=1
		else:
			nums[i] = rnums[r]
				r += 1

def merge_sort(nums,first,last):
	"""merge sort body, time complicity O(nlog n)"""
	if first < last:
		middle = (first+last)/2
		merge_sort(nums,first,middle)
		merge_sort(nums,middle+1,last)
		merge(nums,first,middle,last)
		

def insert_sort(a):
	"""
	有一个已经有序的数据序列，要求在这个排好的序列中插入
	一个数，要求插入后依然有序
	"""
	a_len = len(a)
	if a_len = 0 and a[j] >key:
		a[j+1],a[j] = ap[j],a[j+1]
	return a
	
"""
if __name__ == '__main__':
	nums = [10,4,5,6,7,3]
	merge_sort(nums,0,6)
	
"""