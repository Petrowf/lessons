from tamagochi import Tamagochi

class Octopus(Tamagochi):
    def __init__(self, name):
        super().__init__(name)
        self.view = f"""          ,---.
         ( @ @ )
          ).-.(
         '/|||\`
           '|`   
       """



if __name__ == "__main__":
    name = input("Введите имя: ")
    octo = Octopus(name)
    print(octo)
    action = input("Выберите действие:\nq - выход, b - бить, h - лечить, f - кормить\n")
    while action != 'q':
        if action == 'b':
            hit = int(input("введите урон"))
            octo.bit(hit)
            print(octo)
        elif action == "h":
            hp = int(input("введите здоровье"))
            octo.heal(hp)
            print(octo)
        elif action == "f":
            food = int(input("введите еду"))
            octo.feed(food)
            print(octo)
        else:
            print("Неверный ввод")
        action = input("Выберите действие:\nq - выход, b - бить, h - лечить, f - кормить\n")