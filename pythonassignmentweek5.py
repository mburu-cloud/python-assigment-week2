class Superhero:
    """Base class representing a superhero"""
    
    def __init__(self, name, real_name, power_level):
        """Constructor to initialize superhero attributes"""
        self.name = name
        self.real_name = real_name
        self.power_level = power_level
        self.energy = 100  # All heroes start with full energy
        
    def introduce(self):
        """Method to introduce the superhero"""
        return f"I am {self.name}! My real name is {self.real_name}."
    
    def use_power(self):
        """Basic power usage method"""
        if self.energy >= 20:
            self.energy -= 20
            return f"{self.name} uses their power! Energy remaining: {self.energy}"
        else:
            return f"{self.name} is too tired to use their power!"
    
    def rest(self):
        """Method to restore energy"""
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests and recovers energy. Energy: {self.energy}"

# Inheritance: Creating specialized superhero types
class FlyingSuperhero(Superhero):
    """Superhero that can fly - demonstrates inheritance"""
    
    def __init__(self, name, real_name, power_level, flight_speed):
        # Call parent constructor
        super().__init__(name, real_name, power_level)
        self.flight_speed = flight_speed
        self.is_flying = False
    
    def fly(self):
        """Special method only for flying superheroes"""
        self.is_flying = True
        return f"{self.name} soars through the sky at {self.flight_speed} mph!"
    
    def land(self):
        """Method to land"""
        self.is_flying = False
        return f"{self.name} lands gracefully on the ground."

class MagicSuperhero(Superhero):
    """Superhero with magic abilities - demonstrates inheritance"""
    
    def __init__(self, name, real_name, power_level, spell_count):
        super().__init__(name, real_name, power_level)
        self.spell_count = spell_count
    
    def cast_spell(self, spell_name):
        """Cast a magic spell"""
        if self.spell_count > 0 and self.energy >= 15:
            self.spell_count -= 1
            self.energy -= 15
            return f"{self.name} casts {spell_name}! Spells remaining: {self.spell_count}"
        else:
            return f"{self.name} cannot cast spells right now!"
