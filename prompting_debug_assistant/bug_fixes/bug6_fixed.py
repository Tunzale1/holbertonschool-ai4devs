# Read a JSON file and display the user's name

import json

def get_user_name(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    name = data["user"]["name"].upper()
    return name


assert get_user_name("user.json") == "ALICE"

print("Bug 6 fixed successfully!")
print(get_user_name("user.json"))