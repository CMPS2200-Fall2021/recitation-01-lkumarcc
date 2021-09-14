"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
###import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		#enumerate makes the list into a dictionary w a key and an index. matches the key and returns the index number rather than the key number
		#search runs through the list, finds where its index is and then returns the correct index. if its not there its not in the list
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
	"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search
	
	"""
	mid = (left + right)//2
	if mylist[mid] == key:
		return mid
	if left == right:
		return -1
	if right-left == -2:
		return -1
	elif mylist[mid] <= key:
		return _binary_search(mylist, key, mid+1, right)
	elif mylist[mid] >= key:
		return _binary_search(mylist, key, left, mid-1)
	"""

	Returns:
	  index of key in mylist, or -1 if not present.
	"""
	### TODO
	pass

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
	### TODO: add two more tests here.
	assert binary_search([1,2,3,4,5], -7) == -1
	assert binary_search([1,2,3,4,5], 3) == 2
	pass


def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.
	
	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
	### TODO

	first = time.time()
	search_fn(mylist, key)
	last = time.time()
	total = last-first
	return total	


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	"""
	Compare the running time of linear_search and binary_search
	for input sizes as given. The key for each search should be
	-1. The list to search for each size contains the numbers from 0 to n-1,
	sorted in ascending order. 

	You'll use the time_search function to time each call.

	Returns:
	  A list of tuples of the form
	  (n, linear_search_time, binary_search_time)
	  indicating the number of milliseconds it takes
	  for each method to run on each value of n
	"""
	lslist = []
	bslist = []
	for n in sizes:
		n = int(n)
		newlist = list(range(0, n))
		lslist.append(time_search(linear_search, newlist, -1))
		bslist.append(time_search(binary_search, newlist, -1))

	tuplelist = list(zip(sizes, lslist, bslist))
	return tuplelist


def print_results(results):
	""" done """
	#results parameter will be the list of tuples from compare search
	print(tabulate.tabulate(results,
		headers=['n', 'linear', 'binary'],
		floatfmt=".3f",
		tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1


print(test_binary_search())
test_compare_search()