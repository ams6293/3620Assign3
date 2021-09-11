class Computer:
    def __init__(self, Ram, CPU, Color):
        self.Ram = Ram
        self.CPU = CPU
        self.Color = Color

    def get_specs(self):
        self.Ram = input("Enter how much ram: ")
        self.CPU = input("Enter type of processor: ")
        self.Color = input("Enter Color: ")

    def display_specs(self):
        print("Ram: " + self.Ram)
        print("Color: " + self.Color)
        print("Cpu: " + self.CPU)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_laptop_specs(self):
        self.weight = input("Enter the laptop weight: ")

    def display_laptop_specs(self):
        print("Weight: " + self.weight)


class Desktop(Computer):
    def __init__(self, wifi):
        self.wifi = wifi

    def get_desktop_specs(self):
        self.wifi = input("Enter if the desktop has wifi: ")

    def display_desktop_specs(self):
        print("Wifi: " + self.wifi)


computer1 = Desktop("")
computer1.get_desktop_specs()
computer1.get_specs()
print("Desktop1 Specs: ")
computer1.display_desktop_specs()
computer1.display_specs()

laptop1 = Laptop("")
laptop1.get_laptop_specs()
laptop1.get_specs()
print("Laptop1 Specs: ")
laptop1.display_laptop_specs()
laptop1.display_specs()
