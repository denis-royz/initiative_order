from model.InitiativeHolder import InitiativeHolder


class InitiativeService:

    holder = InitiativeHolder()

    def get_session_holder(self):
        return self.holder

    def reset(self):
        self.holder = InitiativeHolder()

