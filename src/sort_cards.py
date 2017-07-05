"""Sort a deck of cards."""

# ===== Sans Priority Queue Solution =====


def sort_cards(deck):
    """Sort the deck."""
    abstract_sorted = 'A23456789TJQK'
    list_deck = list(deck)
    sorted_deck = []
    for card in abstract_sorted:
        while card in list_deck:
            card_index = list_deck.index(card)
            sorted_deck.append(list_deck.pop(card_index))
    return sorted_deck


# ===== Priority Queue Solution =====


class CardsPriorityQueue(object):
    """Implement a cards priority queue."""

    def __init__(self, deck):
        """Initialize our cards priority queue."""
        self.deck = list(deck)
        self.abstract_sorted_dict = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13
        }

    def heapify(self, deck):
        """Function to heapify our dictionary in deck."""
        heap_list = deck

        def bubble_up(parent, current_node):
            """Helper function to reduce clutter."""
            current_node = parent
            parent = (current_node - 1) // 2
            return (parent, current_node)

        for item in heap_list[::-1]:
            current_node = heap_list.index(item)
            parent = (current_node - 1) // 2
            while current_node > 0:
                parent_priority = list(heap_list[parent].values())[0]
                current_node_priority = list(
                    heap_list[current_node].values())[0]
                if current_node_priority > 0:
                    if parent_priority is 0 or parent_priority > current_node_priority:
                        curr_val = heap_list[parent]
                        heap_list[parent] = heap_list[current_node]
                        heap_list[current_node] = curr_val
                        parent, current_node = bubble_up(parent, current_node)
                    else:
                        parent, current_node = bubble_up(parent, current_node)
                else:
                    parent, current_node = bubble_up(parent, current_node)

        return heap_list

    def sort(self):
        """Pop function for removing highest priority item from queue."""
        this_deck = self.deck
        returned_deck = []
        new_deck = []
        for card in this_deck:
            if card not in self.abstract_sorted_dict:
                raise KeyError("Invalid card in deck.")
            returned_deck.append({card: self.abstract_sorted_dict[card]})
            if len(returned_deck) > 1:
                returned_deck = self.heapify(returned_deck)
        while len(returned_deck) > 0:
            pop_it = list(returned_deck.pop(0).keys())[0]
            new_deck.append(pop_it)
            returned_deck = self.heapify(returned_deck)
        return new_deck
