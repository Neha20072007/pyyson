import random

class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(damage - random.randint(1, self.defense), 0)

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage_dealt = random.randint(1, self.attack)
        enemy.take_damage(damage_dealt)
        print(f"{self.name} attacks {enemy.name} for {damage_dealt} damage!\n")
        
class Player(Character):
    def __init__(self, name, player_class):
        super().__init__(name, 100, 50, 50)
        self.player_class = player_class

        if player_class.lower() == "warrior":
            self.health = 100
            self.attack = 45
            self.defense = 35
            self.special = "Berserk Strike"
            self.special_attack = 25
        elif player_class.lower() == "mage":
            self.health = 85
            self.attack = 70
            self.defense = 25
            self.special = "Lightning Strike"
            self.special_attack = 25
        elif player_class.lower() == "archer":
            self.health = 90
            self.attack = 40
            self.defense = 40
            self.special = "Rapid Shot"
            self.special_attack = 25

class Enemy(Character):
    def __init__(self, enemy_class):
        super().__init__("Ghoul", 90, 20, 20)
        self.enemy_class = enemy_class

        if enemy_class.lower() == "orc":
            self.name = "Orrra the Orc Brute"
            self.health = 100
            self.attack = 60
            self.defense = 40
        elif enemy_class.lower() == "dragon":
            self.name = "Drrra the Ancient Dragon"
            self.health = 170
            self.attack = 80
            self.defense = 90
        elif enemy_class.lower() == "goblin":
            self.name = "Grrra the Vengeful Goblin"
            self.health = 70
            self.attack = 50
            self.defense = 30

def battle(player, enemy):
    print(f"A wild {enemy.name} ({enemy.enemy_class}) appears!\n")
    
    while player.is_alive() and enemy.is_alive():
        choice = input("Do you want to Attack + Defend? Or use a Special attack? (Defend/Attack) : \n")
        if choice.lower() == ("defend"):
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_enemy(player)
        else:
            player.attack_enemy(enemy)
            if enemy.is_alive():
                enemy.attack_enemy(player)
            print(f" \t\t\t\t\t\t\t\t {player.name} uses: {player.special} !!!!! \n")
        print(f"\t\t\t\t\t\t\t{player.name}'s health: {player.health} | {enemy.name}'s health: {enemy.health}\n")

    if player.is_alive():
        print(f"{player.name} emerges victorious!")
    else:
        print(f"{player.name} has been defeated. The {enemy.name} laughs ominously.")

if __name__ == "__main__":
    player_name = input("Enter your character's name: ")
    player_class = input("Choose a class (Warrior, Mage, Archer): ")
    player = Player(player_name, player_class)

    enemy_class = input("Choose an enemy (Orc, Dragon, Goblin): ")
    enemy = Enemy(enemy_class)

    battle(player, enemy)
