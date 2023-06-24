'''Question --- 

In Mexico, foods and beverages that are high in saturated fat, trans fat, sugar, sodium, and/or calories appear with warning labels that are designed to help consumers make healthy food choices.

For instance, the box of cookies in the image below appears with two labels (in the upper right corner):

EXCESO CALORÍAS (in English, EXCESS CALORIES)
EXCESO AZÚCARES (in English, EXCESS SUGAR)
drawing
In this question, you'll work with a function get_labels() that takes the nutritional details about a food item and prints the needed warning labels. This function takes several inputs:

food_type = one of "solid" or "liquid"
serving_size = size of one serving (if solid, in grams; if liquid, in milliliters)
calories_per_serving = calories in one serving
saturated_fat_g = grams of saturated fat in one serving
trans_fat_g = grams of trans fat in one serving
sodium_mg = mg of sodium in one serving
sugars_g = grams of sugar in one serving
Note that some of the code here should feel unfamiliar to you, since we have not shared the details of how some of the functions like excess_sugar() or excess_saturated_fat() work. But at a high level, these are functions that return a value of True if the food is deemed to have an excess of sugar or saturated fat, respectively. These functions are used within the get_labels() function, and whenever there is an excess (of sugar or saturated fat, but also of trans fat, sodium, or calories), it prints the corresponding label.

add Codeadd Markdown
(food_type, serving_size, calories_per_serving, saturated_fat_g, trans_fat_g, sodium_mg, sugars_g)
# import functions needed to make get_labels work
from learntools.intro_to_programming.ex4q5 import excess_sugar, excess_saturated_fat, excess_trans_fat, excess_sodium, excess_calories'''

# Solution --->

def get_labels(food_type, serving_size, calories_per_serving, saturated_fat_g, trans_fat_g, sodium_mg, sugars_g):
    # Print messages based on findings
    if excess_sugar(sugars_g, calories_per_serving) == True:
        print("EXCESO AZÚCARES / EXCESS SUGAR")
    if excess_saturated_fat(saturated_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT")
    if excess_trans_fat(trans_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS TRANS / EXCESS TRANS FAT")
    if excess_sodium(calories_per_serving, sodium_mg) == True:
        print("EXCESO SODIO / EXCESS SODIUM")
    if excess_calories(food_type, calories_per_serving, serving_size) == True:
        print("EXCESO CALORÍAS / EXCESS CALORIES")