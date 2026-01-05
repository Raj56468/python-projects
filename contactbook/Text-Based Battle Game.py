import random

player_health = 100
monster_health = 100

print("🐉 A wild monster appears!")
print("You both start with 100 health.\n")

while player_health > 0 and monster_health > 0:
    print(f"Your Health: {player_health} | Monster Health: {monster_health}")
    action = input("Choose action (attack / heal): ").lower()

    if action == "attack":
        damage = random.randint(10, 25)
        monster_health -= damage
        print(f"⚔️ You hit the monster for {damage} damage!")

    elif action == "heal":
        heal = random.randint(15, 30)
        player_health += heal
        if player_health > 100:
            player_health = 100
        print(f"💊 You healed {heal} health!")

    else:
        print("❌ Invalid action. You lose your turn.")

    if monster_health > 0:
        monster_damage = random.randint(8, 20)
        player_health -= monster_damage
        print(f"🔥 Monster hits you for {monster_damage} damage!")

    print("-" * 30)

if player_health <= 0:
    print("💀 You were defeated by the monster.")
else:
    print("🏆 You defeated the monster!")
