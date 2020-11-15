import file_operations
import random
from faker import Faker

fake = Faker("ru_RU")

skills = [
   "Стремительный прыжок",
   "Электрический выстрел",
   "Ледяной удар",
   "Стремительный удар",
   "Кислотный взгляд",
   "Тайный побег",
   "Ледяной выстрел",
   "Огненный заряд"
]
letters_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}
runic_skills = []

for skill in skills:
    for key in letters_mapping.keys():
        skill = skill.replace(key, str(letters_mapping[key]))
    runic_skills.append(skill)

person_amount = 10
min_ability_value = 8
max_ability_value = 14
for person in range(person_amount):
    random_skills = random.sample(runic_skills, 3)
    male_name = [fake.first_name_male(), fake.last_name_male()]
    female_name = [fake.first_name_female(), fake.last_name_female()]
    names = [male_name, female_name]
    random_name = random.choice(names)
    first_name = random_name[0]
    last_name = random_name[1]
    context = {
      "first_name": first_name,
      "last_name": last_name,
      "job": fake.job(),
      "town": fake.city(),
      "strength": random.randint(min_ability_value, max_ability_value),
      "agility": random.randint(min_ability_value, max_ability_value),
      "endurance": random.randint(min_ability_value, max_ability_value),
      "intelligence": random.randint(min_ability_value, max_ability_value),
      "luck": random.randint(min_ability_value, max_ability_value),
      "skill_1": random_skills[0],
      "skill_2": random_skills[1],
      "skill_3": random_skills[2]
    }

    file_operations.render_template("templates/charsheet.svg", "output/svg/charsheet_{}.svg".format(person+1), context)

