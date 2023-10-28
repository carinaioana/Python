def compose(musical_notes, moves, start_position):
    song_length = len(musical_notes)
    song = []

    for m in moves:
        song.append(musical_notes[start_position])
        start_position = (start_position + m) % song_length

    song.append(musical_notes[start_position])

    return song


def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    move = [1, -3, 4, 2]
    start = 2
    result = compose(notes, move, start)
    print(result)


if __name__ == "__main__":
    main()
