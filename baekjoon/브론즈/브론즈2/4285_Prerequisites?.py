while 1:
    line = input()
    if line == '0':
        exit()

    k, m = map(int, line.split())
    selected_courses = set(input().split())

    meets_requirements = True
    for _ in range(m):
        _, r, *category_courses = input().split()
        
        count = sum(1 for course in category_courses if course in selected_courses)
        if count < int(r):
            meets_requirements = False

    print('yes' if meets_requirements else 'no')
