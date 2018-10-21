import random


class BColors:
	# colors for game
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


class Person:
	#constructor for the person class.
	def __init__(self, hp, mp, attack, df, magic):
		self.max_hp = hp
		self.current_hp = hp
		self.max_mp = mp
		self.current_mp = mp
		self.attack_high = attack + 10
		self.attack_low = attack - 10
		self.defense = df
		self.magic = magic  # array of magic attacks.
		self.actions = ["Attack", "Magic"]

	def attack_gen(self):
		# getter to calculate damage.
		return random.randrange(self.attack_low, self.attack_high)

	def magic_gen(self, mg):
		# getter to calculate name and damage of magic attack being used.
		magic_low = self.magic[mg]["damage"] - 5
		magic_high = self.magic[mg]["damage"] + 5
		# print(self.magic[mg]["name"])
		return random.randrange(magic_low, magic_high)

	def take_damage(self, dmg):
		self.current_hp -= dmg
		if self.current_hp < 0:
			self.current_hp = 0
		return self.current_hp








