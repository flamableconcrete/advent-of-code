import math


def calculate_fuel_required(mass):
    fuel_required = math.floor(mass / 3) - 2
    return fuel_required


def calculate_fuel_required_recursive(mass):
    fuel_required = math.floor(mass / 3) - 2

    if fuel_required <= 0:
        return 0
    else:
        return fuel_required + calculate_fuel_required_recursive(fuel_required)


def part_one():
    total_fuel_required = 0
    for module_mass in get_modules():
        mass = int(module_mass)
        fuel = calculate_fuel_required(mass)
        total_fuel_required += fuel

    print(f'Part 1 fuel required: {total_fuel_required}')


def part_two():
    total_fuel_required = 0
    for module_mass in get_modules():
        mass = int(module_mass)
        fuel = calculate_fuel_required_recursive(mass)
        total_fuel_required += fuel

    print(f'Part 2 fuel required: {total_fuel_required}')


def get_modules():
    with open("modules.txt", "r") as f:
        lines = f.readlines()
    return lines


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
