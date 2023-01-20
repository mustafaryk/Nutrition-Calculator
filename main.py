# tuple of all the foods and their nutrition

list_foods = (
        ({  # nutrition of the food
             'Protein': 11,
             'Calories': 52},
         'egg_white'),  # chicken, name of the food

        ({  # nutrition of the food
             'Protein': 31,
             'Calories': 165},
         'chicken'),  # chicken, name of the food

        ({
             'Protein': 13,
             'Calories': 200},
         'egg'),  # egg

        ({
             'Protein': 7,
             'Calories': 365},
         'rice'),  # rice

        ({
             'Protein': 3,
             'Calories': 110},
         'wheat'),  # wheat

        ({
             'Protein': 1,
             'Calories': 89},
         'banana'),  # banana

        ({
             'Calories': 52},
         'apple'),  # apples

        ({
             'Protein': 20,
             'Calories': 590},
         'almond'),  # almond

        ({
             'Protein': 18,
             'Calories': 561},
         'cashew'),  # cashew

        ({
             'Protein': 3.4,
             'Calories': 42},
         'milk'),  # milk

        ({
             'Protein': 10,
             'Calories': 59},
         'yoghurt'),  # yoghurt

        ({
             'Protein': 9,
             'Calories': 116},
         'daal'),  # daal

        ({
             'Protein': 2,
             'Calories': 22},
         'okra'),  # okra

        ({
             'Calories': 41},
         'carrot'),  # carrot

        ({
             'Calories': 47},
         'orange'),  # orange

        ({
             'Calories': 884},
         'oil'),  # oil

        ({   'Protein' : 15.6,
             'Calories': 295},
         'channe'),  # channe
        ({      'Calories': 100,
                'Protein': 20 },
         'fish'),  # fish



    )


def main():
    # we need to get bodyweight for required protein calculation also we failsafe it
    while True:
        try:
            bodyweight = round(float(input('What is your weight?').strip()))
        except ValueError:
            pass
        else:
            break

    required_protein = round(bodyweight * 1.55)
    calories_cutting = 1800
    calories_maintain = 2200

    # nutrition we got in one day
    nutrition_today = {
        'Calories': 0,  # cal
        'Protein': 0}  # g

    # function to add the nutrition of the specific quantity of eaten food to total nutrition

    def consume(food_nutrition, food_name):
        while True:
            try:
                grams = input(f'how many grams of {food_name} did you consume: ').strip()
                grams = float(grams) / 100  # /100 as nutrition is per 100 grams
            except ValueError:  # ensuring only numbers are put in
                pass
            else:
                break
        for nutrient in food_nutrition:
            nutrition_today[nutrient] += round(food_nutrition[nutrient] * grams)  # add the nutrition of the food to
            # total

    consumed_foods = input('What did you eat today? ').strip().lower().split()  # foods we ate today
    for food in consumed_foods:
        for food_ in list_foods:
            if food == food_[1]:
                consume(food_[0], food_[1])

    protein_status = None
    calories_status = None
    calorie_today_value = nutrition_today['Calories']
    protein_today_value = nutrition_today['Protein']
    if protein_today_value > required_protein:
        protein_status = 'more'
    else:
        protein_status = 'less'
    if (calories_cutting - 50) < calorie_today_value < (calories_cutting + 50):
        calories_status = '0.5 kg cut'
    elif (calories_cutting + 50) < calorie_today_value < calories_maintain:
        calories_status = 'less than 0.5 kg cut'
    elif (calories_cutting - 50) > calorie_today_value:
        calories_status = 'more than 0.5 kg cut'
    elif calories_maintain < calorie_today_value:
        calories_status = 'weight gain'
    print(f'''
            You ate {calorie_today_value} calories, compared to cutting calories of {calories_cutting}
            and maintainence calories of {calories_maintain} you will {calories_status}.
            You consumed {protein_today_value} g of protein, {protein_status} than {required_protein} required.''')

    with open('nutrition_record.txt', 'a') as file:
        file.write(f'{str(nutrition_today)} \n')
        file.close()


if __name__ == '__main__':
    main()
