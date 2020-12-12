"""Creating the differnet biomes that the frogs can live in"""

class Biome:
    def __init__(self, name, climate, foliage_type, foliage_density, predators, weather_consistency, food_density):
        self.name = name
        self.climate = climate
        self.foliage_type = foliage_type
        self.foliage_density = foliage_density
        self.predators = predators
        self.weather_consistency = weather_consistency
        self.food_density = food_density