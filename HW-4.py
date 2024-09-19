class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} погиб!")
        else:
            print(f"{self.name} получил {damage} урона. Осталось здоровья: {self.health}")


class Witcher(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.resurrection_used = False

    def resurrect(self, team):
        if not self.resurrection_used:
            for hero in team:
                if hero.health <= 0:
                    print(f"{self.name} жертвует собой, чтобы воскресить {hero.name}")
                    hero.health = 50
                    self.health = 0
                    self.resurrection_used = True
                    return
            print(f"{self.name} не нашел погибших героев для воскрешения.")


class Magic(Hero):
    def __init__(self, name, health, attack, power_increase):
        super().__init__(name, health, attack)
        self.power_increase = power_increase

    def increase_attack(self, team):
        for hero in team:
            hero.attack += self.power_increase
            print(f"Атака {hero.name} увеличена на {self.power_increase}. Теперь атака: {hero.attack}")


class Hacker(Hero):
    def __init__(self, name, health, attack, steal_amount):
        super().__init__(name, health, attack)
        self.steal_amount = steal_amount

    def steal_health(self, boss, team):
        for hero in team:
            if hero.health > 0:
                boss.health -= self.steal_amount
                hero.health += self.steal_amount
                print(f"{self.name} забирает {self.steal_amount} здоровья у босса и передает {hero.name}.")
                print(f"Здоровье босса: {boss.health}, здоровье {hero.name}: {hero.health}")
                break


class Golem(Hero):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

    def absorb_damage(self, team, boss_attack):
        absorbed = boss_attack // 5
        self.health -= absorbed
        print(f"{self.name} поглощает {absorbed} урона из атаки босса. Осталось здоровья: {self.health}")
        return boss_attack - absorbed


class Boss:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_hero(self, hero):
        hero.take_damage(self.attack)


witcher = Witcher("Witcher", 100, 10)
magic = Magic("Magic", 80, 12, power_increase=5)
hacker = Hacker("Hacker", 70, 15, steal_amount=20)
golem = Golem("Golem", 200, 5)
boss = Boss("Boss", 500, 30)

team = [witcher, magic, hacker, golem]

boss.attack_hero(golem)

magic.increase_attack(team)

hacker.steal_health(boss, team)

witcher.resurrect(team)

boss_attack = boss.attack
reduced_attack = golem.absorb_damage(team, boss_attack)
boss.attack_hero(witcher)