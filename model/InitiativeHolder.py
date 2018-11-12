from model.Actor import Actor


class InitiativeHolder(object):

    def __init__(self):
        self.actors = []
        self.counter = 20
        self.current = Actor("Null", 0)

    def add_actor(self, actor_name, base_init):
        self.actors.append(Actor(actor_name, base_init))

    def next_actor(self):
        selected = None
        for actor in self.actors:
            if actor.initiative > -1 and actor.has_turn:
                if selected is None or actor.initiative > selected.initiative:
                    selected = actor
        return selected

    def step(self):
        next_actor = self.next_actor()
        if next_actor is None:
            for actor in self.actors:
                actor.has_turn = True
                if actor.initiative < 0:
                    actor.append_initiative(20)
                    actor.has_turn = False
            self.counter = 20
            next_actor = self.next_actor()
        self.counter = next_actor.initiative
        next_actor.has_turn = False
        self.current = next_actor
        self.actors.sort()

    def delay_actor(self, name, value):
        for actor in self.actors:
            if actor.name == name:
                actor.append_initiative(-value)
                self.actors.sort()
                return True
        return False

    def get_actors(self):
        return self.actors

    def clear(self):
        self.actors = []

    def current_actor(self):
        return self.current
