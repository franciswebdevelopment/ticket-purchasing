TICKET_PRICE = 10

tickets_remaining = 100

# Run this code continuously until we run out of tickets

while tickets_remaining >= 1:

	# Output how many tickets are remaining using the tickets_remaining variable

	print("There are {} tickets remaining".format(tickets_remaining))

	# Gather the user's name and assign it to a new variable

	customer_name = input("What is your name?  ")

	# Prompt the user by name and ask how many tickets they would like

	print("Hi there, {} ".format(customer_name))
	ticket_request = input("How many tickets would you like?  ")
	ticket_request = int(ticket_request)

	# Calculate the price (number of tickets multiplied by the price) and assign it to a variable

	order_cost = ticket_request * TICKET_PRICE

	# Output the price to the screen
	print("The total due is ${}".format(order_cost))

	# Prompt user if they want to proceed. Y/N?
	proceed = input("Would you like to proceed? Y/N ").upper()

	# If they want to proceed
	if proceed == "Y":
		# print out to the screen "SOLD!" to confirm purchase
		# TODO: Gatjer credit card information and process it.
		print("SOLD!")
		# and then decrement the tickets remaining by the number of tickets purchased
		tickets_remaining = tickets_remaining - ticket_request
	# Otherwise...
	elif proceed == "N":
		# Thank them by name
		print("Thank you for your time, {}".format(customer_name))


# Notify user the tickets are sold out
print("Sorry, {} the tickets have sold out!".format(customer_name))