users={"RAJESH":"Active","gangadhar":"InActive","saran":"InActive","puti":"Active"
}
for user,status in users.copy().items():
    if status=="InActive":
        del users[user]

Active_users={}
for user,status in users.items():
    if status=="Active":
        Active_users[user] = status
print(Active_users)


# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status