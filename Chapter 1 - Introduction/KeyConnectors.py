users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {}
for user in users:
    friendships[user['id']] = []
    
for f1, f2 in friendship_pairs:
    friendships[f1].append(f2)
    friendships[f2].append(f1)


print("Friendship Dictionary:")
print(friendships)
print()


# Average Number of Connections
totalConnections = 0
for v in friendships.values():
    totalConnections += len(v)

print("Average Number of Connections: ", end='')
print(totalConnections/len(users))
print()

#User with most friends
numberOfFriends = []
for user in users:
    numberOfFriends.append((user["id"], len(friendships[user["id"]])))

numberOfFriends.sort(
    key = lambda numberOfFriends: numberOfFriends[1], reverse=True
)

usersWithMostFriends = []
maxFriendsCount = numberOfFriends[0][1]
for f in numberOfFriends:
    if f[1] == maxFriendsCount:
        usersWithMostFriends.append(users[f[0]]['name'])
    if f[1] < maxFriendsCount:
        break

print("Users with most friends:")
print(usersWithMostFriends)
print()

