owner_list = []


class Owner:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.pets = []

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def add_pet(self, name, age, animal_type):
        self.pets.append(Pet(name, age, animal_type))

    def del_pet(self, pet):
        self.pets.remove(pet)

    def show_pets(self):
        print(self.pets)

    def show_pets_by_type(self, animal_type):
        filtered_pets = filter(lambda p: p.animal_type == animal_type, self.pets)
        for pet in filtered_pets:
            print(pet)


class Pet:
    def __init__(self, name, age, animal_type):
        self.name = name
        self.age = age
        self.animal_type = animal_type

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)


i = 0
while i < 1:
    print("Menu:")
    print("1)Add owner")
    print("2)Delete owner")
    print("3)Show all owners")
    print("4)Show owners and pets")
    print("5)Select owner")
    print("Type any other symbol to exit")
    select = int(input("Select:"))
    if select == 1:
        print("Type name. age and city of owner")
        name = input("Name:")
        age = input("Age:")
        city = input("City:")
        owner_list.append(Owner(name, age, city))
    elif select == 2:
        del_select = input("Type owner`s name to delete:")
        for o in owner_list:
            if o.name == del_select:
                owner_list.remove(o)
    elif select == 3:
        print(owner_list)
    elif select == 4:
        for o in owner_list:
            print(o)
            print("Pets:")
            print(o.pets)
    elif select == 5:
        ch_select = input("Type owner`s name to select:")
        selected_owner = 0
        for o in owner_list:
            if o.name == ch_select:
                selected_owner = o
        if not selected_owner:
            print("404 Not found")
        else:
            j = 0
            while j < 1:
                print("Submenu:")
                print("1)Add pet")
                print("2)Delete pet")
                print("3)Show all pets")
                print("4)Show pets by type")
                print("Type any other symbol to exit")
                secondary_select = int(input("Select:"))
                if secondary_select == 1:
                    print("Type pet name, age, animal type:")
                    name = input("Name:")
                    age = input("Age:")
                    animal_type = input("Animal type:")
                    selected_owner.add_pet(name, age, animal_type)
                elif secondary_select == 2:
                    delete_select = input("Type pet`s name to delete:")
                    for p in selected_owner.pets:
                        if p.name == delete_select:
                            selected_owner.del_pet(p)
                elif secondary_select == 3:
                    selected_owner.show_pets()
                elif secondary_select == 4:
                    animal_type = input("Type pet`s type:")
                    selected_owner.show_pets_by_type(animal_type)
                else:
                    j += 1
    else:
        i += 1
