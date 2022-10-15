def login(database, username, password):
    if username in database and password in database[username]:
        print("Welcome back", username)
        return username
    elif username in database and database[username] != password:
        print("\nIncorrect password for admin.")
        return ""
    else:
        print("\nUser not found. Please register.")
        return ""

def register(database, username):
    if username in database.keys():
        print("\nUsername already registered")
        return ""
    else:
        print("\nUsername", username, "registered.")
        return username

