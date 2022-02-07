def create_dictionary():
    x = {"day": "when the sun is out",
         "night": "when the moon is out",
         "food": "something you eat"}
    return x


def add_to_dictionary(in_dictionary, new_word,
                      new_definition):
    in_dictionary[new_word] = new_definition


def output_dictionary(in_dictionary):
    print(type(in_dictionary))
    print(in_dictionary)
    # definition = in_dictionary["night"]
    add_to_dictionary(in_dictionary, "lunch", "mid-day meal")
    print(get_definition(in_dictionary, "lunch"))
    print(in_dictionary.keys())
    print(in_dictionary.values())
    print(in_dictionary.count)


def get_definition(in_dictionary, word):
    another_way = in_dictionary.get(word)
    print(another_way)
    definition = in_dictionary[word]
    return definition


if __name__ == "__main__":
    my_dictionary = create_dictionary()
    output_dictionary(my_dictionary)
