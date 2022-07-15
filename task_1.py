'''
TASK 1

судя по примеру
print(task("111111111110000000000000000"))
# >> OUT: 11
в качестве аргумента может передаваться и строка, которая в последующем преобразуется в список.
'''

def task(array):
	if type(array) == str:
		try:
			str_to_list = list(map(int, array))
		except ValueError as e:
			print("YOU SHOULD ENTER VALID DATA")
			raise e
		return str_to_list.index(0)

	return array.index(0)


int_list = [1, 2, 3, 5, 47, 0, 4, 0, 0, 0]
str_list = "111111111110000000000000000"

if __name__ == '__main__':
	print(task(int_list))
	print(task(str_list))