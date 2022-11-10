def read_line_helper(file):
    fle = open(file, "r")
    for line in fle:
        print(line)
    fle.close()


def dialogue_helper(dialogue):
    """
    It has a general template of how conversations go. I might go Bethesda style
    and make it so that you can ask four questions.
    """
    d = open(dialogue, "r")

    speech = False
    response = False

    choices = []
    replies = []

    for line in d:
        if line.lower().strip() == 'dialogue':
            speech = True

        if line.lower().strip() == 'end dialogue':
            speech = False

        if speech is True:
            print(line)

        if line.lower().strip() == 'responses':
            response = True

        if response is True:
            the_split = line.split("|")
            choices.append(the_split[0])
            replies.append((the_split[-1]))

        if line.lower().strip() == 'end dialogue':
            response = False
            dialogue_looper(choices, replies)


def dialogue_looper(choices, replies):

    selection = []

    print("Choices")
    for choice in choices:
        print(choice)
        selection.append(choice[0])

    appropriate_selection = False

    while appropriate_selection is False:

        player_selection = input("Type an option and hit 'enter': ")

        if player_selection == "":
            pass


def two_lists_to_one_dictionary(keys_list, value_list):
    """
    :param keys_list: the list that becomes the keys of the dictionary.
    :param value_list: the list that becomes the values of each key.
    :return: a dictionary.
    """
    output_dictionary = {}
    for item in keys_list:
        output_dictionary[item] = value_list[keys_list.index(item)]
    return output_dictionary


if __name__ == '__main__':
    pass
