def relation_to_luke(name):
	rltn_dict = {
    "Darth Vader": "father",
    "Leia": "sister",
    "Han": "brother in law",
    "R2D2": "droid"}
	
	print("Luke, I am your "+ rltn_dict[name])

relation_to_luke("Leia")