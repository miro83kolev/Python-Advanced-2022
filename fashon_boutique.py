clothes = [int(x) for x in input().split()]
rack_cap = int(input())

current_rack_cap = rack_cap
rack_counter = 1


while clothes:
    last_element = clothes[-1]
    if last_element > current_rack_cap:
        rack_counter += 1
        current_rack_cap = rack_cap
    else:
        current_rack_cap -= last_element
        clothes.pop()


print(rack_counter)