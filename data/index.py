class Index:
     def __init__(self, labels, name=""):
        if len(labels) != len(set(labels)):
            raise ValueError("Labels not unique.")
        if not labels:
            raise ValueError("Index must contain at least one label.")
        self.labels = labels
        self.name = name

     def get_loc(self, key):
        if key not in self.labels:
            raise KeyError(f"Key {key} not found in labels.")
        return self.labels.index(key)