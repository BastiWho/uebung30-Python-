def search_list(list, element):
    if element in list:
        return True
    else:
        return False

my_list = input("Bitte gib ein, was du in deiner Liste haben möchtest. Trenne dies durch ein Komme und Leerzeichen: ").split(", ")
print()
search_element = input("Was möchtest du suchen?: ")
print()
print(search_list(my_list, search_element))