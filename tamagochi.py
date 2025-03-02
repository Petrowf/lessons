class Tamagochi:
    def __init__(self, name:str):
        self.name = name
        self.__hp = 100
        self.__hunger = 100
        self.view = ""

    def bit(self, hit):
        self.__hp -= hit
        self.__hunger -= 5

    def heal(self, points):
        self.__hp += points
        self.__hunger -= 5

    def feed(self, food):
        self.__hunger += food

    def __str__(self):
        return self.view + "\n" +  f"Имя {self.name}, HP: {self.__hp}, hunger: {self.__hunger}"