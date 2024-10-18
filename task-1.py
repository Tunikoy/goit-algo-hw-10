import pulp

# Оголошення проблеми лінійного програмування
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Оголошення змінних
limonade = pulp.LpVariable('Limonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Оголошення цільової функції
model += limonade + fruit_juice, "Maximize total production"

# Оголошення обмежень
model += 2 * limonade + fruit_juice <= 100, "Water constraint"
model += 1 * limonade <= 50, "Sugar constraint"
model += 1 * limonade <= 30, "Lemon juice constraint"
model += 2 * fruit_juice <= 40, "Fruit puree constraint"

# Рішення задачі
model.solve()

# Виведення результатів
print(f"Максимальна кількість лимонаду: {limonade.varValue}")
print(f"Максимальна кількість фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість: {limonade.varValue + fruit_juice.varValue}")
