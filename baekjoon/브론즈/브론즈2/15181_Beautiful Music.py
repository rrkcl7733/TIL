note_positions = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}


def is_beautiful_music(notes):
    for i in range(1, len(notes)):
        previous_note = note_positions[notes[i - 1]]
        current_note = note_positions[notes[i]]
        difference = (current_note - previous_note) % 7

        if difference not in [2, 4, 6]:
            return "Ouch! That hurts my ears."

    return "That music is beautiful."


while True:
    notes = input()
    if notes == '#':
        break
    result = is_beautiful_music(notes)
    print(result)
