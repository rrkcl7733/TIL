def min_friends_needed(smax, audience_str):
    standing = 0
    friends_needed = 0

    for shyness_level in range(smax + 1):
        num_people = int(audience_str[shyness_level])
        if num_people == 0:
            continue
        if standing < shyness_level:
            extra = shyness_level - standing
            friends_needed += extra
            standing += extra
        standing += num_people

    return friends_needed

for case_num in range(int(input())):
    smax, audience_str = input().split()
    result = min_friends_needed(int(smax), audience_str)
    print(f"Case #{case_num + 1}: {result}")
