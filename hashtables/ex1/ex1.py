#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # loop through length and insert weights, length as index
    for index in range(length):
        hash_table_insert(ht, weights[index], index)

    # for every index in hashtable retrieve all in HashTable
    for index in range(length):
        # check to see if hash table contains an entry
        next_index = hash_table_retrieve(ht, (limit - weights[index]))
        if next_index:
            # if if does we found the two items that sum up to the limit
            if next_index > index:
                return [next_index, index]
            else:
                return [index, next_index]


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
