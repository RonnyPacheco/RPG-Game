from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "damage": 60},
		{"name": "Thunder", "cost": 10, "damage": 60},
		{"name": "Blizzard", "cost": 10, "damage": 60}]


player = Person(460, 65, 60, 34, magic)

print(player.attack_gen())
print(player.magic_gen(2))
print("Current life of the character is:", player.current_hp)
