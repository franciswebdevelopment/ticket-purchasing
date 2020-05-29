TICKET_PRICE = 10

tickets_remaining = 100

while tickets_remaining >= 1:
	print("There are {} tickets remaining".format(tickets_remaining))
	customer_name = input("What is your name?  ")
	print("Hi there, {} ".format(customer_name))
	ticket_request = input("How many tickets would you like?  ")
	# Expect a ValueError to happen and handle it appropriately...remember to test it out!
	try:
		ticket_request = int(ticket_request)
		# Raise a ValueError if the request is for more tickets than available
		if ticket_request > tickets_remaining:
			raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
	except ValueError as err:
		# Include the error text in the output
		print("Oh no, we ran into an issue. {}. Please try again".format(err))
	else:
		order_cost = ticket_request * TICKET_PRICE
		print("The total due is ${}".format(order_cost))
		proceed = input("Would you like to proceed? Y/N ").upper()
		if proceed == "Y":
			# TODO: Gather credit card information and process it.
			print("SOLD!")
			tickets_remaining -= ticket_request
		elif proceed == "N":
			print("Thank you for your time, {}".format(customer_name))
print("Sorry, {} the tickets have sold out!".format(customer_name))