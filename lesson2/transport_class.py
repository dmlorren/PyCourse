class Transport:
    def __init__(self, model, maxspeed, capacity):
        # атрибуты
        self.model = model
        self.maxspeed = maxspeed
        self.capacity = capacity
    # тут описывается метод, т.е действие которое может выполнить объект
    def start_engine(self):
        print(f"{self.model} делает врум-врум, двигатель транспортного средства заведён.")

    def moving(self):
        print(f"{self.maxspeed} км.ч максимальная скорость транспортного средства.")

    def contain(self):
        print(f"{self.capacity} пассажира(ов) вместительность транспортного средства.")


class Auto_trans(Transport):
    def __init__(self, model, maxspeed, capacity, transmisson):
        # вызываем конструктор суперкласса, чтобы остальные атрибуты тоже подтянулись
        super().__init__(model, maxspeed, capacity)
        self.transmission = transmisson
    def switch_transmission(self):
        print(f" Для модели {self.model} включена {self.transmission} -я(ая) передача.")


class Railway_trans(Transport):
    def __init__(self, model, maxspeed, capacity, direct_current):
        super().__init__(model, maxspeed, capacity)
        self.direct_current = direct_current
    def moving(self):
        print(f"{self.model} движется со скоростью {self.maxspeed} км.ч и ему(ей) требуется {self.direct_current} Кв переменного тока." )

class Air_trans(Transport):
    def __init__(self,model, maxspeed, capacity, flight_altitude):
        super().__init__(model, maxspeed, capacity)
        self.flight_altitude = flight_altitude
    def moving(self):
        print(f"{self.model} движется со скоростью {self.maxspeed} км.ч на высоте {self.flight_altitude} км.")


class Sea_trans(Transport):
    def __init__(self, model, maxspeed, capacity, displacement):
        super().__init__(model, maxspeed, capacity)
        self.displacement = displacement
    def contain(self):
        print(f"Вместительность пассажиров {self.capacity} человек, а водоизмещение {self.displacement} тон.")


# тут создаём экземпляр для родительского класса (супер класс)
car1 = Transport("Mitsubishi", "140", 4)
car2 = Transport("Volga", "320", 8)

# # вызываем методы экземпляров класса
# car1.start_engine()
# car1.moving()
# car1.contain()
# car2.start_engine()
# car2.moving()
# car2.contain()

# тут создаём экземпляр наследуемого класса Автотранспорт
car3 = Auto_trans("Opel", "150", 4, 5)
# car3.start_engine()
# car3.switch_transmission()

# тут создаём экземпляр наследуемого класса Железнодорожный транспорт
train = Railway_trans("Ласточка", 130, 60, 3)
# train.moving()

airplane = Air_trans("Airbus-330", 870, 295, 12)
# airplane.moving()

ship = Sea_trans("Титаник", 23, 899, 52310)
# ship.contain()