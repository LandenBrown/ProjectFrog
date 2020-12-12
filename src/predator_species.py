"""Outlining predators and how they will function"""

class Predator:
    """#Predator Class"""

    def __init__(self, name, transport_function, external_attributes, internal_attributes, attack_methods, lifespan_days):
        self.name = name
        self.transport_function = transport_function
        self.external_attributes = external_attributes
        self.internal_attributes = internal_attributes
        self.attack_methods = attack_methods
        self.lifespan_days = lifespan_days