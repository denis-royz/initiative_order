import uuid


class Actor:

    def __init__(self, name, initiative, has_turn=False):
        self.name = name
        self.initiative = initiative
        self.has_turn = has_turn
        self.id = uuid.uuid4()

    def append_initiative(self, value):
        self.initiative += value

    def set_initiative(self, value):
        self.initiative = value

    def get_name(self):
        return self.name

    def __lt__(self, other):
        return self.initiative > other.initiative
