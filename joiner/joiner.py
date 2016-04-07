#!/bin/env python3
final_string = ""
separator = ","
do_loop = True
print("Paste the strings you want to join here, leave an empty row to finish:\n")
while do_loop:
	tmp_string = input()
	if tmp_string == "":
		do_loop = False
	else:
		final_string = final_string + separator + tmp_string

try:
	if final_string[-1] == ",":
		print(final_string[1:-1])
	else:
		print(final_string[1:])
except:
	print("Invalid string.")