def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = []
    for name in names:
        badges.append(f"Hello, my name is {name}.")
    return badges

def assign_rooms(names):
    rooms = []
    index = 0
    # while index < len(names):
    # for index, name in enumerate(names):
    for index in range(len(names)):
        rooms.append(f"Hello, {names[index]}! You'll be assigned to room {index + 1}!")
        # index += 1
    return rooms

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for thing in assign_rooms(names):
        print(thing)
