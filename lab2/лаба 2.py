from abc import ABC, abstractmethod

class GameObject:
    next_id = 1
    
    def __init__(self, name, coord_x, coord_y):
        self.id = GameObject.next_id
        GameObject.next_id += 1
        self.name = name
        self.coord_x = coord_x
        self.coord_y = coord_y

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getX(self):
        return self.coord_x

    def getY(self):
        return self.coord_y

class Unit(GameObject):
    def __init__(self, name, coord_x, coord_y, health):
        super().__init__(name, coord_x, coord_y)
        self.health_points = health

    def getHp(self):
        return self.health_points

    def isAlive(self):
        return self.health_points > 0

    def receiveDamage(self, damage_amount):
        self.health_points -= damage_amount
        if self.health_points < 0:
            self.health_points = 0

class Building(GameObject):
    def __init__(self, name, coord_x, coord_y, built_status=False):
        super().__init__(name, coord_x, coord_y)
        self.is_built = built_status

    def isBuilt(self):
        return self.is_built

    def build(self):
        self.is_built = True

class Attacker(ABC):
    @abstractmethod
    def attack(self, target_unit):
        pass

class Moveable(ABC):
    @abstractmethod
    def move(self, target_x, target_y):
        pass

class Archer(Unit, Attacker, Moveable):
    def __init__(self, name, coord_x, coord_y, health, power):
        super().__init__(name, coord_x, coord_y, health)
        self.attack_power = power

    def move(self, target_x, target_y):
        if self.isAlive():
            print(f"{self.getName()} moves from ({self.getX()}, {self.getY()}) to ({target_x}, {target_y})")
            self._coord_x = target_x
            self._coord_y = target_y

    def attack(self, target_unit):
        if self.isAlive():
            print(f"{self.getName()} shoots at {target_unit.getName()}")
            target_unit.receiveDamage(self.attack_power)

class Fort(Building, Attacker):
    def __init__(self, obj_name, coord_x, coord_y, firepower):
        super().__init__(obj_name, coord_x, coord_y, built_status=True)
        self.firepower = firepower

    def attack(self, target_unit):
        if self.isBuilt():
            print(f"{self.getName()} fires at {target_unit.getName()} with cannons!")
            target_unit.receiveDamage(self.firepower)

class MobileHouse(Building, Moveable):
    def __init__(self, obj_name, coord_x, coord_y, built_status=True):
        super().__init__(obj_name, coord_x, coord_y, built_status)

    def move(self, target_x, target_y):
        print(f"{self.getName()} moves from ({self.getX()}, {self.getY()}) to ({target_x}, {target_y})")
        self._coord_x = target_x
        self._coord_y = target_y

archer = Archer("Archer", 1, 2, 100, 10)
enemy_unit = Unit("Enemy", 3, 77, 10)
fort = Fort("Fort", 6, 5, 20)
mobile_house = MobileHouse("Mobile House", 2, 7)

archer.attack(enemy_unit) 
fort.attack(enemy_unit)     
mobile_house.move(9, 4)     
print(f"Enemy's health: {enemy_unit.getHp()}")