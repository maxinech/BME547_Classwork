def interface():
	print("Blood Test Analysis")
	keep_running = True
	while keep_running:
		print("Options:")
		print("1-HDL")
		print("9-Quit")
		choice = input("Enter your choice: ")
		if choice == '9':
			keep_running = False
		elif choice == "1":
			HDL_driver()
	return


def accept_input(test_name):
	entry = input("Enter the {} test result: ".format(test_name))
	return int(entry)


def print_result(test_name, test_value, test_class):
	out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
	print(out_string)
	return


def check_HDL(HDL_value):
	if HDL_value >= 60:
		answer = "Normal"
	elif 60 > HDL_value >= 40:
		answer = "Borderline low"
	else:
		answer = "Low"
	return answer


def HDL_driver():
	HDL_value = accept_input("HDL")
	classification = check_HDL(HDL_value)
	print_result("HDL", HDL_value, classification)



interface()