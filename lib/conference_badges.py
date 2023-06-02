def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_queue = list()
    # for name in names:
    #     badge_queue.append(f"Hello, my name is {name}.")
    [badge_queue.append(f"Hello, my name is {name}.") for name in names]
    return badge_queue

def assign_rooms(names):
    room_assignments = list()
    # for index, name in enumerate(names):
    #     room_assignments.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    [room_assignments.append(f"Hello, {name}! You'll be assigned to room {index + 1}!") for index, name in enumerate(names)]
    return room_assignments

def printer(names):
    badge_list = batch_badge_creator(names)
    # for badge in badge_list:
    #     print(badge)
    [print(badge) for badge in badge_list]
    room_list = assign_rooms(names)
    [print(assignment) for assignment in room_list]
    # for assignment in room_list:
    #     print(assignment)
    return None
