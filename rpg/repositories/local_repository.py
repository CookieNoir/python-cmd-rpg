class LocalRepository:
    def __init__(self):
        self._data = {}

    def fill_from_dict(self, data: dict):
        self._data = data.copy()

    def get_item(self, key):
        return self._data[key]
