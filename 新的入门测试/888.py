current_users=[a**2 for a in range(1,11)]
new_users=[b**2 for b in range(7,20)]
for user in new_users:
    if user in current_users:
        print(f"{user} is yes")
    else:
        print(f"{user} is no")
