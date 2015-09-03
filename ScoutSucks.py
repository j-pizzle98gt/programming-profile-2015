#band name generator
import random

titles = ["gigantic", "sour", "steamy", "gross", "stupid", "ironic", "greasy", "tangy", "smelly", "small", "inventive", "spherical", "green", "blue", "pot bellied", "pickled", "prickly"]

adjs = ["tiny", "fat", "shiny", "eccectic", "fluffy", "bright", "corrupt", "aggressive", "alarming", "amazing", "magical", "courageous", "fierce", "colorless", "red", "thoughtless", "smart", "delirous", "fabulous", "fergalicious", "dangerous"]

plural_nouns = ["apples", "oranges", "kiwis", "clementines", "wildabeasts", "mammoths", "rabbits", "sloths", "crashes", "spices", "eggs", "herbs", "pony tails", "bears", "snitches", "unicorns", "kermits", "signs", "indians", "cowboys"]

def title():
	return random.choice(titles)

def adj():
	return random.choice(adjs)

def plural_noun():
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("Jp")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and the", adj(), plural_noun()