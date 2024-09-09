class Computer:
    def __init__(self, cpu: float, memory: float):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self) -> float:
        return self.__cpu

    def set_cpu(self, cpu: float):
        self.__cpu = cpu

    def get_memory(self) -> float:
        return self.__memory

    def set_memory(self, memory: float):
        self.__memory = memory

    def make_computations(self):
        addition = self.__cpu + self.__memory
        multiplication = self.__cpu * self.__memory
        subtraction = self.__cpu - self.__memory
        return {
            "addition": addition,
            "multiplication": multiplication,
            "subtraction": subtraction
        }

    def __str__(self):
        return f"Computer: CPU = {self.__cpu} GHz, Memory = {self.__memory} GB"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self) -> list:
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number: int, call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Calling {call_to_number} from SIM card {sim_card_number} - {sim_card}")
        else:
            print("Invalid SIM card number")

    def __str__(self):
        return f"Phone: SIM cards = {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: float, memory: float, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location: str):
        print(f"Building route to {location}...")

    def __str__(self):
        return f"SmartPhone: CPU = {self.get_cpu()} GHz, Memory = {self.get_memory()} GB, SIM cards = {', '.join(self.get_sim_cards_list())}"


computer = Computer(3.2, 16)
phone = Phone(["Beeline", "Megacom"])
smartphone1 = SmartPhone(2.8, 8, ["O!", "Beeline"])
smartphone2 = SmartPhone(3.5, 12, ["Megacom"])

print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

print("\n=== Methods testing ===")
print(computer.make_computations())

phone.call(1, "+996702789910")

smartphone1.use_gps("Bishkek")
smartphone1.call(2, "+996700345712")

print("\n=== Comparison ===")
print(computer > smartphone1)
print(smartphone1 == smartphone2)