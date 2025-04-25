import random

CHARACTERS = (
	"Frodo",
	"Sam",
	"Merry",
	"Pippin",
	"Aragorn",
	"Legolas",
	"Gimli",
	"Boromir",
	"Gandalf",
	"Saruman",
	"Sauron",
)


def random_character() -> None:
	"""My random character"""
	# length = 5
	# summ = length**2
	# area = length * 2
	# area_divided_2 = area // summ

	# print(area_divided_2)
	print(34)
	random.choice(CHARACTERS)


def ring_bearer(name: str) -> bool:
	"""Get the ring bearer"""
	# assert name == "3"
	return name in ("Frodo", "Sam")


if __name__ == "__main__":
	character = random_character()
	# if ring_bearer(character):
	# 	# print(f"{character} is a ring bearer")
	# else:
	# 	# print(f"{character} is not a ring bearer")
