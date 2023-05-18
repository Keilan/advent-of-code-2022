def find_common_item(rucksack):
    # Split into compartments
    midpoint = len(rucksack)//2
    compartment1 = rucksack[:midpoint]
    compartment2 = rucksack[midpoint:]

    # Use set intersection to find common item
    sharedItems = set(compartment1).intersection(set(compartment2))

    # We know there is only one shared item
    return sharedItems.pop()


def find_badge(rucksacks):
    """
    Instead of a single rucksack split in two, we take 3 rucksacks and find
    the common element between them.
    """
    shared = set(rucksacks[0])
    for rucksack in rucksacks:
        shared = shared.intersection(set(rucksack))

    return shared.pop()


def get_priority(item):
    # Use the ASCII values of the items to get priority
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27



if __name__ == "__main__":
    # Read list of rucksacks
    with open('input.txt', 'r') as f:
        rucksacks = f.read().splitlines()

    # Part 1 - sum up the priorities of the common elements
    priority_sum = 0
    for rucksack in rucksacks:
        common = find_common_item(rucksack)
        priority_sum += get_priority(common)
    print(f'The sum of priorities for the common items is {priority_sum}.')

    # Part 2 - find the common element in groups of 3 rucksacks
    # We know the range will work because the number of rucksacks is a multiple of 3
    # and the upper end isn't inclusive
    priority_sum = 0
    for index in range(0, len(rucksacks), 3):
        elfGroup = rucksacks[index:index+3]
        badge = find_badge(elfGroup)
        priority_sum += get_priority(badge)
    print(f'The sum of badge priorities is {priority_sum}')


