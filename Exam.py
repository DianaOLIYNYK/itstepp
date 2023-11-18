import random

import math

lower = int(input("Введіть ціле число від:- "))

upper = int(input("Введіть ціле число до:- "))

x = random.randint(lower, upper)
print("\n\tВ тебе тільки ",
	round(math.log(upper - lower + 1, 2)),
	" спроби щоб вгадати ціле число!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
	count += 1

	guess = int(input("Вгадай ціле число:- "))

	if x == guess:
		print("Вітаю!Ти зробив це за ",
			count, " спроб")

		break
	elif x > guess:
		print("Занадто маленьке число!")
	elif x < guess:
		print("Занадто велике число!")

if count >= math.log(upper - lower + 1, 2):
	print("\nЗагадане ціле число є %d" % x)
	print("\tНаступного разу пощастить;)")
