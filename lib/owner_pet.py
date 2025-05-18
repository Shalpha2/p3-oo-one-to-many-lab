class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type  # This uses the setter for validation
        self._owner = None  # Internal attribute
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of Owner class")
            self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        if value not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: {value}. Must be one of {Pet.PET_TYPES}")
        self._pet_type = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise Exception("Owner must be an instance of Owner class")
        self._owner = value
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
