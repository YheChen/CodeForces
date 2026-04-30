username = str(input())
chars = set([s for s in username])
print("IGNORE HIM!") if len(chars) % 2 == 1 else print("CHAT WITH HER!")
