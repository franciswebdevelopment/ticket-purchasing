TICKET_PRICE = 10

tickets_remaining = 100

# Out how many tickets are remaining using the tickets_remaining variable

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