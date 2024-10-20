class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def __str__(self):
        return f"Library with {len(self._items)} items"

    def __repr__(self):
        return f"Library({self._items})"
