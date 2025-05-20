import random

class GameEntity:
    def __init__(self, entity_id, position=(0, 0), health=100, status="active"):
        self.entity_id = entity_id
        self.position = position
        self.health = health
        self.status = status

    def move(self, new_position):
        self.position = new_position

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.entity_id} took {amount} damage, health now {self.health}")
        if self.health <= 0:
            self.status = "dead"
            print(f"{self.entity_id} has died.")

class Player(GameEntity):
    def __init__(self, entity_id, position=(0, 0), health=100, status="active"):
        super().__init__(entity_id, position, health, status)
        self.inventory = []

    def pick_item(self, item):
        self.inventory.append(item)
        print(f"{self.entity_id} picked up {item.name}")

    def attack(self, target):
        damage = random.randint(10, 20)
        print(f"{self.entity_id} attacks {target.entity_id} for {damage} damage!")
        target.take_damage(damage)

class Enemy(GameEntity):
    def __init__(self, entity_id,
                 position=(random.randint(1, 10), random.randint(1, 10)),
                 health=50, status="active"):
        super().__init__(entity_id, position, health, status)

    def attack(self, target):
        damage = random.randint(5, 15)
        print(f"{self.entity_id} attacks {target.entity_id} for {damage} damage!")
        target.take_damage(damage)

class Item:
    def __init__(self, name, effect="none"):
        self.name = name
        self.effect = effect

    def use(self, user: GameEntity):
        if self.effect == "heal" and user.status == "active":
            amount = random.randint(10, 30)
            user.health += amount
            print(f"{user.entity_id} healed for {amount}, health now {user.health}")


class DigitalTwinGameEnvironment:
    def __init__(self):
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)
        print(f"Added {entity.entity_id} ({entity.__class__.__name__}) to world.")

    def simulate_game_event(self):
        event_type = random.choice(["player_attack", "enemy_spawn"])

        if event_type == "player_attack":
            players = [e for e in self.entities
                       if isinstance(e, Player) and e.status == "active"]
            enemies = [e for e in self.entities
                       if isinstance(e, Enemy) and e.status == "active"]
            if not players or not enemies:
                print("No valid attacker or target available.")
                return

            attacker = random.choice(players)
            target   = random.choice(enemies)
            damage   = random.randint(10, 20)

            print(f">>> EVENT: {attacker.entity_id} attacks {target.entity_id} for {damage} damage!")
            target.take_damage(damage)

        elif event_type == "enemy_spawn":
            # Count existing enemies to assign a new ID
            count = sum(isinstance(e, Enemy) for e in self.entities)
            new_enemy = Enemy(entity_id=f"Enemy-{count+1}")
            print(f">>> EVENT: New enemy spawned: {new_enemy.entity_id}")
            self.add_entity(new_enemy)

if __name__ == "__main__":
    # Create players & enemies
    p1 = Player(entity_id="Player-1")
    e1 = Enemy(entity_id="Enemy-1")

    # Create environment & add entities
    world = DigitalTwinGameEnvironment()
    world.add_entity(p1)
    world.add_entity(e1)

    # Run 5 random events
    for i in range(5):
        print(f"\n--- Simulation {i+1} ---")
        world.simulate_game_event()

