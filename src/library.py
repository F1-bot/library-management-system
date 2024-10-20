class Library:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def search(self, keyword):
        return [item for item in self._items if
                keyword.lower() in item.title.lower() or keyword.lower() in item.author.lower()]

    def search_by_year(self, year):
        return [item for item in self._items if item.year == year]

    def __str__(self):
        return f"Library with {len(self._items)} items"

    def __repr__(self):
        return f"Library({self._items})"
