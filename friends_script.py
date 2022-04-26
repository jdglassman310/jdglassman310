# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from collections import Counter
from collections import defaultdict

#-----------------------------------------------------------------------------#
# Functions                                                                   #
#-----------------------------------------------------------------------------#
# Function to identify the total number of connections.
# Do this by summing up the lengths of all the friends lists
def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"] 
    # Output: user returns {'id':9, 'name': 'Klein'} - therefore user["id"] will just return 9 in this case.
    friend_ids = friendships[user_id]
    # Output: An array of friends associated with the user in play
    return len(friend_ids)

# [Deprecated] Function to identify users with a certain interest.
def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id for user_id, user_interest in interests
            if user_interest == target_interest]

# Function to identify users who share common interests:
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
        )

#-----------------------------------------------------------------------------#
# Main script                                                                 #
#-----------------------------------------------------------------------------#

#--Inputs---------------------------------------------------------------------# 

# Build the users list, which is a list with keys, "id" and "name", that make it a dictionary.
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
    ]

# Build the friendship_pairs list (shape is 12 rows x 2 columns)
friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), 
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

# Build a 'list of pairs' of users and their interests
interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (9, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"), 
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artifical intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]


#--Analysis 1-----------------------------------------------------------------#
# Identify the "key connectors" to identify who are the most connected people in the social network.

# Initialize a dictionary (called 'friendships') with an empty list for each user id:
friendships = {user["id"]: [] for user in users}
# Output looks like: {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
# NOTE: {} define a dictionary, which is a data structure that maps one value to another.

# Loop over the friendship pairs to populate the 'friendship' dictionary:
for i, j in friendship_pairs:
    friendships[i].append(j) # Add j as a friend of user i
    friendships[j].append(i) # Add i as a friend of user j
    
#--Analysis 2-----------------------------------------------------------------#
# Identify the average number of connections.

# Find the total number of connections by summing up the lengths of all the friends lists:
total_connections = sum(number_of_friends(user) for user in users)

# Divide the total number of connections by the number of users:
num_users = len(users)
avg_connections = total_connections/num_users


#--Analysis 3-----------------------------------------------------------------# 
# Identify the most and least connected people. 

# Create a list (user_id, number_of_friends):
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(                             # Sort the list
    key=lambda id_and_friends: id_and_friends[1],   # by num_friends
    reverse=True)                                   # largest to smallest
# Output is a pair with the user_id and the number_of_friends for that user_id

#--Analysis 4-----------------------------------------------------------------#
# Count the number of mutual friends shared.

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]       # For each of my friends,
        for foaf_id in friendships[friend_id]       # find their friends
        if foaf_id != user_id                       # who are not me
        and foaf_id not in friendships[user_id]     # and aren't my friends
        )

print(friends_of_friends(users[3]))
# Output is: Counter({0:2, 5:1})

#--Analysis 5-----------------------------------------------------------------#
# Identify users who share similar interests.

# Keys are interests, values are lists of user_ids with that interest:
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Keys are user_ids, values are lists of interests for that user_id:
interests_by_user_id = defaultdict

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
