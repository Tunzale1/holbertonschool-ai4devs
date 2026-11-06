# Read a JSON file and display the user's name

import json

def get_user_name(filename):
    with open(filename, "r") as file:
        data = json.loads(file)

    name = data["user"]["name"].upper()
    return name

# Example JSON file content:
# {
#     "user": {
#         "name": "Alice"
#     }
# }

print(get_user_name("user.json"))