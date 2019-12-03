import random

# Set the size variable to change the total number of groups
size = 25

# Create initial two lists of groups
group_list = []
shuffled_group_list = []

for i in range(size):
    group_list.append(i + 1)
    shuffled_group_list.append(i + 1)


# Shuffle the list until no elements in the new list match up with elements in the old list at the same indexes
def shuffle_list(shuffled_group_list):
    random.shuffle(shuffled_group_list)

    for i in range(size):
        if group_list[i] == shuffled_group_list[i]:
            shuffle_list(shuffled_group_list)


shuffle_list(shuffled_group_list)

# Print out the matched up groups
for i in range(size):
    print(f"Group: {group_list[i]} -> Group: {shuffled_group_list[i]}")
