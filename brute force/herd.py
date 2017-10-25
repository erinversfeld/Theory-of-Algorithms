def only_one_type(food_max, food, water_max, water):

    population_size = 0

    while True:
        temp_pop_size = population_size + 1
        temp_food_cost = temp_pop_size * food
        temp_water_cost = temp_pop_size * water

        if temp_food_cost > food_max:
            break

        if temp_water_cost > water_max:
            break

        population_size = temp_pop_size

    return population_size


def optimise_herd(cattle_profit, sheep_profit, goat_profit, food_max, cattle_food, sheep_food, goat_food, water_max,
                  cattle_water, sheep_water, goat_water):

    # determine upperbounds on animal populations
    max_cattle = only_one_type(food_max, cattle_food, water_max, cattle_water)
    max_sheep = only_one_type(food_max, sheep_food, water_max, sheep_water)
    max_goat = only_one_type(food_max, goat_food, water_max, goat_water)

    herd = []
    profit = 0

    for cattle_pop_size in range(max_cattle + 1):
        for sheep_pop_size in range(max_sheep + 1):
            for goat_pop_size in range(max_goat + 1):
                current_cattle_profit = cattle_pop_size * cattle_profit
                current_sheep_profit = sheep_pop_size * sheep_profit
                current_goat_profit = goat_pop_size * goat_profit
                current_profit = current_cattle_profit + current_sheep_profit + current_goat_profit

                cattle_food_cost = cattle_pop_size * cattle_food
                sheep_food_cost = sheep_pop_size * sheep_food
                goat_food_cost = goat_pop_size * goat_food
                food_cost = cattle_food_cost + sheep_food_cost + goat_food_cost

                cattle_water_cost = cattle_pop_size * cattle_water
                sheep_water_cost = sheep_pop_size * sheep_water
                goat_water_cost = goat_pop_size * goat_water
                water_cost = cattle_water_cost + sheep_water_cost + goat_water_cost

                if current_profit > profit and food_cost <= food_max and water_cost <= water_max:
                    profit = current_profit
                    herd = [cattle_pop_size, sheep_pop_size, goat_pop_size]

    return herd


if __name__ == "__main__":
    cattle_profit, sheep_profit, goat_profit = input().strip().split(' ')
    food_max = input().strip()
    cattle_food, sheep_food, goat_food = input().strip().split(' ')
    water_max = input().strip()
    cattle_water, sheep_water, goat_water = input().strip().split(' ')

    herd_demographics = optimise_herd(float(cattle_profit), float(sheep_profit), float(goat_profit), float(food_max),
                         float(cattle_food), float(sheep_food), float(goat_food), float(water_max), float(cattle_water),
                         float(sheep_water), float(goat_water))

    herd_out = ' '.join([str(pop_size) for pop_size in herd_demographics])
    print(herd_out)
