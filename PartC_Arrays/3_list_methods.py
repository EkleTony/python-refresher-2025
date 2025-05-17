# ================= List Methods ===============

people: list[str] = ["Tono", "Mario", "Katie"]
people.append("John")


print(people)

# === Remove item ===
# people.remove("Katie")
print(people)

mario = people.count("Mario")
print(mario)

people.append("Oche!")
people.insert(50, "Ekle")
print(people)

# poping items
popped = people.pop(0)
print(popped)

# people.remove("Ekle")
print(people)

people.reverse()
print(people)

# sorting
people.sort()
print("sorting: ", people)

# soring with lower
people.sort(key=lambda name: len(name), reverse=True)
print(people)
