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
from questionnaire.models import Questionnaire
from foodList.models import FoodList
from foodItem.models import FoodItem
from trade.models import Trade
from wardrobe.models import Wardrobe
from language.models import Language
from player.models import Player
from shopItem.models import ShopItem
from realPack.models import RealPack
from playerProgress.models import PlayerProgress
from inventory.models import Inventory
from gamePack.models import GamePack

fake = Faker()
fake.add_provider(FoodProvider)

# 🔹 Function to clear tables and reset IDs
def reset_table(model):
    table_name = model._meta.db_table  # Get the actual database table name
    print(f"🔹 Resetting table: {table_name}")
    with connection.cursor() as cursor:
        cursor.execute(f'TRUNCATE TABLE "{table_name}" RESTART IDENTITY CASCADE;')
    print(f"🗑️ Table '{table_name}' cleared and IDs reset. \n")

# 🔹 Populate BallingoUser
def populate_users(n=10):
    reset_table(BallingoUser)  # Clear and reset IDs
    for _ in range(n):
        BallingoUser.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password=f"password123{n}"
        )
    print(f"✅ {n} users created. \n")

# 🔹 Populate Clothes
def populate_clothes(n=10):
    reset_table(Clothes)
    clothes_types = ['hat', 'tshirt', 'shoes', 'accesories']
    for _ in range(n):
        Clothes.objects.create(
            type=random.choice(clothes_types),
            style=None
        )
    print(f"✅ {n} clothing items created. \n")

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
    print(f"✅ {n} food items created. \n")

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
    print(f"✅ {n} questions created. \n")

# 🔹 Populate Questionnaires (now with language field)
def populate_questionnaires(n=5):
    reset_table(Questionnaire)
    
    questions = list(Question.objects.all())  # Get all questions
    languages = list(Language.objects.all())  # Get all languages

    if not questions or not languages:
        print("⚠️ Not enough questions or languages. Populate Question and Language first. \n")
        return

    for _ in range(n):
        q = Questionnaire.objects.create(
            name=fake.word().capitalize(),
            level=random.randint(1, 10),
            unlocked=random.choice([True, False]),
            language=random.choice(languages)  # Assign a random language
        )

        # Assign random questions (up to 5)
        q.questions.add(*random.sample(questions, min(len(questions), 5)))

    print(f"✅ {n} questionnaires created. \n")

# 🔹 Populate FoodList (for each user)
def populate_food_list(n=10):
    reset_table(FoodList)
    players = list(Player.objects.all())

    if not players:
        print("⚠️ No players found. Please populate BallingoUser first. \n")
        return

    for _ in range(n):
        user = random.choice(players)
        FoodList.objects.create(player=players)

    print(f"✅ {n} food lists created. \n")

# 🔹 Populate FoodItem (assigning food to FoodLists)
def populate_food_items(n=20):
    reset_table(FoodItem)
    food_lists = list(FoodList.objects.all())
    foods = list(Food.objects.all())

    if not food_lists or not foods:
        print("⚠️ No food lists or foods found. Populate FoodList and Food first. \n")
        return

    for _ in range(n):
        FoodItem.objects.create(
            foodlist=random.choice(food_lists),
            food=random.choice(foods),
            quantity=random.randint(1, 5)  # Assign random quantity
        )

    print(f"✅ {n} food items added to food lists. \n")

# 🔹 Populate Trade (create random trades between foods)
def populate_trades(n=10):
    reset_table(Trade)
    players = list(Player.objects.all())
    foods = list(Food.objects.all())

    if not players or len(foods) < 2:
        print("⚠️ Not enough players or foods. Populate Player and Food first. \n")
        return

    for _ in range(n):
        in_food, out_food = random.sample(foods, 2)  # Ensure different foods
        Trade.objects.create(
            user=random.choice(players),
            isActive=random.choice([True, False]),
            in_food=in_food,
            out_food=out_food
        )

    print(f"✅ {n} trades created. \n")

# 🔹 Populate Wardrobe (assign random clothes to users)
def populate_wardrobes(n=10):
    reset_table(Wardrobe)
    players = list(Player.objects.all())
    clothes = list(Clothes.objects.all())

    if not players or not clothes:
        print("⚠️ No players or clothes found. Populate Player and Clothes first. \n")
        return

    for _ in range(n):
        wardrobe = Wardrobe.objects.create(player=random.choice(players))
        wardrobe.items.set(random.sample(clothes, min(len(clothes), random.randint(1, 5))))  # Assign up to 5 clothes

    print(f"✅ {n} wardrobes created. \n")

# 🔹 Populate Players
def populate_players(n=10):
    reset_table(Player)
    users = list(BallingoUser.objects.all())
    inventories = list(Inventory.objects.all())
    languages = list(Language.objects.all())

    if not users or not inventories or not languages:
        print("⚠️ Not enough users, inventories, or languages. Populate them first. \n")
        return

    for _ in range(n):
        player = Player.objects.create(
            user=random.choice(users),
            inventory=random.choice(inventories),
            actualLanguage=random.choice(['en', 'es', 'de', 'ar', 'ja'])
        )
        player.languages.add(*random.sample(languages, min(len(languages), 3)))  # Assign up to 3 languages

    print(f"✅ {n} players created. \n")

# 🔹 Populate PlayerProgress
def populate_player_progress(n=10):
    reset_table(PlayerProgress)
    players = list(Player.objects.all())
    questionnaires = list(Questionnaire.objects.all())

    if not players or not questionnaires:
        print("⚠️ Not enough players or questionnaires. Populate Player and Questionnaire first. \n")
        return

    for _ in range(n):
        PlayerProgress.objects.create(
            player=random.choice(players),
            questionnaire=random.choice(questionnaires),
            completed=random.choice([True, False]),
            score=random.randint(0, 100),
            attempts=random.randint(1, 5)
        )

    print(f"✅ {n} player progress records created. \n")

# 🔹 Populate ShopItems
def populate_shop_items(n=15):
    reset_table(ShopItem)
    clothes = list(Clothes.objects.all())

    for _ in range(n):
        item_type = random.choice(['lives', 'coins', 'clothes'])
        shop_item = ShopItem.objects.create(
            type=item_type,
            quantity=random.randint(1, 10),
            clothes=random.choice(clothes) if item_type == 'clothes' and clothes else None
        )

    print(f"✅ {n} shop items created. \n")

# 🔹 Populate RealPacks
def populate_real_packs(n=10):
    reset_table(RealPack)
    shop_items = list(ShopItem.objects.all())

    if not shop_items:
        print("⚠️ No shop items found. Populate ShopItem first. \n")
        return

    for _ in range(n):
        pack = RealPack.objects.create(
            price=random.randint(5, 50),
            name=fake.word().capitalize(),
            description=fake.sentence(),
            category=random.choice(['lastOportunity', 'new', 'popular'])
        )
        pack.items.add(*random.sample(shop_items, min(len(shop_items), 3)))  # Add up to 3 shop items

    print(f"✅ {n} real packs created. \n")

# 🔹 Populate Languages (Predefined List)
def populate_languages():
    reset_table(Language)
    
    languages = ['en', 'es', 'de', 'ar', 'ja']
    for lang in languages:
        Language.objects.create(language=lang)

    print(f"✅ {len(languages)} languages created. \n")

# 🔹 Populate Inventories
def populate_inventories(n=10):
    reset_table(Inventory)
    wardrobes = list(Wardrobe.objects.all())
    food_lists = list(FoodList.objects.all())

    if not wardrobes or not food_lists:
        print("⚠️ Not enough wardrobes or food lists. Populate them first. \n")
        return

    for _ in range(n):
        Inventory.objects.create(
            clothes_inventory=random.choice(wardrobes),
            food_inventory=random.choice(food_lists),
            coins=random.randint(0, 1000),
            livesCounter=random.randint(0, 5)
        )

    print(f"✅ {n} inventories created. \n")

# 🔹 Populate GamePacks
def populate_game_packs(n=10):
    reset_table(GamePack)
    shop_items = list(ShopItem.objects.all())

    if not shop_items:
        print("⚠️ No shop items found. Populate ShopItem first. \n")
        return

    for _ in range(n):
        pack = GamePack.objects.create(
            price=random.randint(5, 50),
            name=fake.word().capitalize(),
            description=fake.sentence(),
            category=random.choice(['lastOportunity', 'new', 'popular'])
        )
        pack.items.add(*random.sample(shop_items, min(len(shop_items), 3)))  # Add up to 3 shop items

    print(f"✅ {n} game packs created. \n")

# Run functions
if __name__ == "__main__":
    # 1️⃣ Populate Independent Tables First
    #populate_languages()
    #populate_users()
    #populate_clothes()
    #populate_food()
    #populate_questions()
    #populate_shop_items()
    
    # 2️⃣ Populate Tables That Depend on the Above
    #populate_questionnaires()
    #populate_players()
    #populate_wardrobes()
    #populate_food_list()
    #populate_trades()
    #populate_real_packs()
    #populate_game_packs()
    
    # 3️⃣ Populate Tables With Many-to-Many or Foreign Key Dependencies
    #populate_food_items()
    #populate_player_progress()
    #populate_inventories()

    """Food.objects.create(
        name="Squid Rings",
        language='es',
        hunger_points=10,
        image_path="/assets/inventory/food/es/squid_rings.png"
    )"""

    Clothes.objects.create(
        type='hat',
        image_path = "winter_hat"
    )

    print("🎉 Database successfully populated.")
