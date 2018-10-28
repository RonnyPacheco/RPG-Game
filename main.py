from classes.game import Person, BColors

magic = [{"name": "Fire", "cost": 10, "damage": 60},
		{"name": "Thunder", "cost": 10, "damage": 60},
		{"name": "Blizzard", "cost": 10, "damage": 60}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(BColors.FAIL + BColors.BOLD + "Enemy Attacks!" + BColors.ENDC)

while running:
	print("===================")
	player.pick_action()
	player_input = input("Choose action: ")
	index = int(player_input) - 1

	if index == 0:
		dmg = player.attack_gen()
		enemy.take_damage(dmg)
		print("You attacked for",dmg, "points of damage. Enemy Hp:", enemy.get_hp())

	enemy_choice = 1
	enemy_dmg = enemy.attack_gen()
	player.take_damage(enemy_dmg)
	print("The enemy attack for", enemy_dmg, "points of damage. Player Hp:", player.get_hp())






