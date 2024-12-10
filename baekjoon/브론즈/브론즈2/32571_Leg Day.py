n = int(input())
exercises = [input() for _ in range(n)]

calendar = []
for i in range(31):
    exercise = exercises[i % n]
    if 'leg' in exercise:
        calendar.append('🦵')
    elif 'arm' in exercise or 'biceps' in exercise:
        calendar.append('💪')
    else:
        calendar.append('🤖')

for i in range(0, 31, 7):
    print(*calendar[i:i + 7], sep='')
