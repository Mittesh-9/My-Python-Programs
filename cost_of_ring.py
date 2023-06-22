'''Q no.5 (Hard difficulty)

You own an online shop where you sell rings with custom engravings. You offer both gold plated and solid gold rings.

Gold plated rings have a base cost of $50, and you charge $7 per engraved unit.
Solid gold rings have a base cost of $100, and you charge $10 per engraved unit.
Spaces and punctuation are counted as engraved units.
Write a function cost_of_project() that takes two arguments:

engraving - a Python string with the text of the engraving
solid_gold - a Boolean that indicates whether the ring is solid gold'''

# Solution ---->

def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (100 + 10 * len(engraving)) + (not solid_gold) * (50 + 7 * len(engraving))
    return cost

''' Run the next code cell to calculate the cost of engraving Charlie+Denver on a solid gold ring.
	project_one = cost_of_project("Charlie+Denver", True)
	print(project_one)

	Ans) 240 '''

''' Use the next code cell to calculate the cost of engraving 08/10/2000 on a gold plated ring.
	project_two = cost_of_project("08/10/2000", False)
	print(project_two)

	Ans) 120 '''


# Same question ^ ( solution with Conditional statements ) ---->

def cost_of_project(engraving, solid_gold):
    if solid_gold == True:
        cost = (100 + 10 * len(engraving))
    else:
        cost = (50 + 7 * len(engraving))
    return cost