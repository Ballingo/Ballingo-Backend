import os
import django
import random
from faker import Faker
from faker_food import FoodProvider
from django.db import connection

# Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

from user.models import BallingoUser
from clothes.models import Clothes
from food.models import Food
from question.models import Question
from questionnarie.models import Questionnarie
from foodList.models import FoodList
from foodItem.models import FoodItem
from trade.models import Trade
from wardrobe.models import Wardrobe

fake = Faker()
fake.add_provider(FoodProvider)

# 🔹 Function to clear tables and reset IDs
def reset_table(model):
    table_name = model._meta.db_table  # Get the actual database table name
    print(f"🔹 Resetting table: {table_name}")
    with connection.cursor() as cursor:
        cursor.execute(f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE;')
    print(f"🗑️ Table '{table_name}' cleared and IDs reset.")

# 🔹 Populate BallingoUser
def populate_users(n=10):
    reset_table(BallingoUser)  # Clear and reset IDs
    for _ in range(n):
        BallingoUser.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password=f"password123{n}"
        )
    print(f"✅ {n} users created.")

# 🔹 Populate Clothes
def populate_clothes(n=10):
    reset_table(Clothes)
    clothes_types = ['hat', 'tshirt', 'shoes', 'accesories']
    for _ in range(n):
        Clothes.objects.create(
            type=random.choice(clothes_types),
            style=None
        )
    print(f"✅ {n} clothing items created.")

# 🔹 Populate Food with Real Food Names
def populate_food(n=10):
    reset_table(Food)
    for _ in range(n):
        Food.objects.create(
            name=fake.dish(),  # Generates a real food name
            language=random.choice(['en', 'es', 'fr', 'de']),
            hunger_points=random.randint(1, 100),
            image=None
        )
    print(f"✅ {n} food items created.")

# 🔹 Populate Questions
def populate_questions(n=10):
    reset_table(Question)
    for _ in range(n):
        answers = [fake.sentence() for _ in range(4)]
        correct_answer = random.randint(0, 3)  # Index of the correct answer

        Question.objects.create(
            title=fake.sentence(),
            correct_answer=correct_answer,
            answers=answers
        )
    print(f"✅ {n} questions created.")

# 🔹 Populate Questionnaires
def populate_questionnaries(n=5):
    reset_table(Questionnarie)
    questions = list(Question.objects.all())

    for _ in range(n):
        q = Questionnarie.objects.create(
            name=fake.word().capitalize(),
            level=random.randint(1, 10),
            sublevel=random.randint(1, 5),
        )
        
        if questions:
            q.questions.add(*random.sample(questions, min(len(questions), 5)))

    print(f"✅ {n} questionnaires created.")


# 🔹 Populate FoodList (for each user)
def populate_food_list(n=10):
    reset_table(FoodList)
    users = list(BallingoUser.objects.all())

    if not users:
        print("⚠️ No users found. Please populate BallingoUser first.")
        return

    for _ in range(n):
        user = random.choice(users)
        FoodList.objects.create(user=user)

    print(f"✅ {n} food lists created.")

# 🔹 Populate FoodItem (assigning food to FoodLists)
def populate_food_items(n=20):
    reset_table(FoodItem)
    food_lists = list(FoodList.objects.all())
    foods = list(Food.objects.all())

    if not food_lists or not foods:
        print("⚠️ No food lists or foods found. Populate FoodList and Food first.")
        return

    for _ in range(n):
        FoodItem.objects.create(
            foodlist=random.choice(food_lists),
            food=random.choice(foods),
            quantity=random.randint(1, 5)  # Assign random quantity
        )

    print(f"✅ {n} food items added to food lists.")

# 🔹 Populate Trade (create random trades between foods)
def populate_trades(n=10):
    reset_table(Trade)
    users = list(BallingoUser.objects.all())
    foods = list(Food.objects.all())

    if not users or len(foods) < 2:
        print("⚠️ Not enough users or foods. Populate BallingoUser and Food first.")
        return

    for _ in range(n):
        in_food, out_food = random.sample(foods, 2)  # Ensure different foods
        Trade.objects.create(
            user=random.choice(users),
            isActive=random.choice([True, False]),
            in_food=in_food,
            out_food=out_food
        )

    print(f"✅ {n} trades created.")

# 🔹 Populate Wardrobe (assign random clothes to users)
def populate_wardrobes(n=10):
    reset_table(Wardrobe)
    users = list(BallingoUser.objects.all())
    clothes = list(Clothes.objects.all())

    if not users or not clothes:
        print("⚠️ No users or clothes found. Populate BallingoUser and Clothes first.")
        return

    for _ in range(n):
        wardrobe = Wardrobe.objects.create(user=random.choice(users))
        wardrobe.items.set(random.sample(clothes, min(len(clothes), random.randint(1, 5))))  # Assign up to 5 clothes

    print(f"✅ {n} wardrobes created.")

# Run functions
if __name__ == "__main__":
    #populate_users()
    #populate_clothes()
    #populate_food()
    #populate_questions()
    #populate_questionnaries()
    populate_food_list()
    populate_food_items()
    populate_trades()
    populate_wardrobes()
    print("🎉 Database successfully populated.")
