import random



def get_word():
    # wortliste holen
    word_list = ["hallo", "grüen", "prost", "fäldi", "wixxe", "chlei", "auäää", "liebi"]
    word = random.choice(word_list)
    return word

word = get_word()
