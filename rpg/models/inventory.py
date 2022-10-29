class Inventory:
    def __init__(self, items=None):
        if items is not None:
            self._items = items
        else:
            self._items = []

    def add_item(self, item_id: int):
        self._items.append(item_id)

    def take_item(self, item_id: int):
        self._items.remove(item_id)

    def get_items(self, start: int = 0, end: int = -1):
        if end > len(self._items) or end < 0:
            end = len(self._items)
        for i in range(start, end):
            yield self._items[i]
