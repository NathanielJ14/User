class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"first_name: {self.first_name}")
        print(f"last_name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"is_rewards_member: {self.is_rewards_member}")
        print(f"gold_card_points: {self.gold_card_points}")

    def enroll(self, ):
        self.is_rewards_member = True
        self.gold_card_points += 200

    def spend_points(self, amount):
        self.gold_card_points -= amount




user1 = User(first_name="Nathan", last_name="Albert", email="Nathanjalbert@gmail.com", age=18)
user2 = User(first_name="Kennedy", last_name="Pearl", email="KennPearl12@gmail.com", age=18)
user3 = User(first_name="Felix", last_name="Yuro", email="Felix332@gmail.com", age=21)

user1.enroll()
user1.spend_points(50)

user2.enroll()
user2.spend_points(80)

user1.display_info()
user2.display_info()


