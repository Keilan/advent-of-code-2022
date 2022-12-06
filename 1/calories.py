def get_pack_sums(elf_packs):
    pack_sums = [sum(pack) for pack in elf_packs]
    return pack_sums

if __name__ == "__main__":
    # Read input into a list of lists - containing the calories for each elf
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    elf_packs = []
    current_list = []
    for calories in lines:
        calories = calories.strip()
        if calories.isnumeric():
            current_list.append(int(calories))
        else:
            elf_packs.append(current_list)
            current_list = []
    elf_packs.append(current_list)

    pack_sums = get_pack_sums(elf_packs)
    print(f"Day 1 Part 1: {max(pack_sums)}")

    # For day 2, sort the list and take the sum of the top 3 values
    pack_sums.sort()
    print(f"Day 1 Part 2: {sum(pack_sums[-3:])}")
