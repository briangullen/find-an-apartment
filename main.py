def apt_search1(city: str, max_rent: int, min_beds: int, pets_allowed: bool):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budge of ${max_rent} per month...')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} apartment, all within a budget of ${max_rent} per month...')


def apt_search2(city: str, max_rent: int, min_beds: int = 2, pets_allowed: bool = True):
    if pets_allowed:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budge of ${max_rent} per month...')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in {city} for {min_beds} apartment, all within a budget of ${max_rent} per month...')


apt_search2('Detroit', 1500)  # Arguments for min_beds and pets_allowed both omitted
apt_search2('Chicago', 2500, min_beds=3)  # Argument min_bed without pets_allowed
apt_search2('New York', 3000, pets_allowed=False)  # Argument with pets_allowed and min_beds omitted

plus_one_hundred = lambda x: x + 100
square_num = lambda x: x ** 2
divide_by_three = lambda x: x / 3
concatenate = lambda word: '- ' + word


print(plus_one_hundred(50))  # 50 + 100 = 150
print(square_num(4))  # 4^2 = 16
print(divide_by_three(30))  # 30/3 = 10
print(concatenate('hello'))  # '-' + 'hello' = '- hello'


