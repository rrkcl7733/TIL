def recognize_dice(face):
    if face == [':::', ':o:', ':::']:
        return 1
    if face == ['o::', ':::', '::o']:
        return 2
    if face == ['::o', ':::', 'o::']:
        return 2
    if face == ['o::', ':o:', '::o']:
        return 3
    if face == ['::o', ':o:', 'o::']:
        return 3
    if face == ['o:o', ':::', 'o:o']:
        return 4
    if face == ['o:o', ':o:', 'o:o']:
        return 5
    if face == ['ooo', ':::', 'ooo']:
        return 6
    if face == ['o:o', 'o:o', 'o:o']:
        return 6
    return 'unknown'

face = [input() for _ in range(3)]
print(recognize_dice(face))
