def group_by_rhyme(words):
    rhyme_groups = {}

    for word in words:
        # last two characters of the word
        rhyme = word[-2:]

        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            # create a new group
            rhyme_groups[rhyme] = [word]

    # list of lists
    result = list(rhyme_groups.values())

    return result


word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
rhyme_group = group_by_rhyme(word_list)
print(rhyme_group)
