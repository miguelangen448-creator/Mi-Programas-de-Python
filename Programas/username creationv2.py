print("Create an username Program :D")

print("RULES:")
print("1.- The username must be between 3 and 20 characters")
print("2.- The username must not include spaces")
print("3.- the username must start with a letter")
print("4.- Teh username must not be 'admin', 'username' or 'user'")

username = input("Input your username: ")

if len(username) < 3 or len(username) > 20:
	print("invalid username. Reason: Shorter than 3 characters or longer than 20 characters")
elif not username.find(" ") == -1:
	print("invalid username. Reason: Username contains spaces")
elif not username[0].isalpha():
	print("invalid username. Reason: Username doesn't start with a letter")
elif username == 'admin' or username == 'username' or username == 'user':
	print("invalid username. Reason: the username is 'admin', 'username' or 'user'")
else:
	print(f"Welcome {username}")
