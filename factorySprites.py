
class FactorySprites:

    def __init__(self, prototipes, periodos, events):
        self.prototipes = prototipes
        self.periods = periodos
        self.eventTypes = events


    def make(self, event_type):
        return self.prototipes[event_type - self.eventTypes].clone()


