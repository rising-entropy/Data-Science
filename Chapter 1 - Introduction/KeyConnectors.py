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

#Data Scientists You May Know
friendsOfFriends = {}
for k, v in friendships.items():
    mutuals = []
    for friend in v:
        mutuals += friendships[friend]
    mutuals = list(set(mutuals))
    mutuals.remove(k)
    for each in v:
        try:
            mutuals.remove(each)
        except:
            pass
    friendsOfFriends[k] = mutuals

print("Data Scientists You May Know:")    
print(friendsOfFriends)
print()

# Count of Mutuals
def countOfMutuals(f1, f2):
    lst1 = friendships[f1]
    lst2 = friendships[f2]
    return len(list(set(lst1) & set(lst2)))
# print (countOfMutuals(1,2))

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

#map interests with users
InterestsOfUsers = {}
for interest in interests:
    if interest[0] in InterestsOfUsers.keys():
        InterestsOfUsers[interest[0]].append(interest[1])
    else:
        InterestsOfUsers[interest[0]] = [interest[1]]

print("Map Interests of Users:")
print(InterestsOfUsers)
print()

#map users with interests
UsersOfInterest = {}
for interest in interests:
    if interest[1] in UsersOfInterest.keys():
        UsersOfInterest[interest[1]].append(interest[0])
    else:
        UsersOfInterest[interest[1]] = [interest[0]]
        
print("Map Users of Interest:")
print(UsersOfInterest)
print()

#popular keywords
keywords = {}
for interest in interests:
    thatInterest = interest[1].split()
    for inter in thatInterest:
        keywords[inter] = keywords.get(inter, 0)+1

#sort in descending order
thoseKeywords = sorted(keywords.items(), key = lambda kv:(kv[1], kv[0]))
thoseKeywords.reverse()

print("Popular Keywords")
print(thoseKeywords)
print()