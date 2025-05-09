import logging
import random

logger = logging.getLogger(__name__)

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


def random_character() -> str:
	"""My random character"""
	return random.choice(CHARACTERS)


def ring_bearer(name: str) -> bool:
	"""Get the ring bearer"""
	return name in ("Frodo", "Sam")


if __name__ == "__main__":
	character = random_character()
	if ring_bearer(character):
		# print("Commented out") #noqa
		logger.info(f"{character} is a ring bearer")
	else:
		logger.info(f"{character} is not a ring bearer")
