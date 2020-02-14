#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    """
    YOUR CODE HERE
    """

    # for each ticket in tickets insert all to to hashtable
    for ticket in tickets:
        # with key = source and value = destination

        hash_table_insert(hashtable, ticket.source, ticket.destination)

    current_source = "NONE"
    # retrieve routes -1
    for i in range(length-1):
        # set routes to retrive and add them to the route
        route[i] = hash_table_retrieve(hashtable, current_source)
        current_source = route[i]

    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

results = reconstruct_trip(tickets, 3)

print(f'\n resulst: ', results)
