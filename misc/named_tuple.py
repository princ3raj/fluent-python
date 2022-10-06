from collections import namedtuple

Person = namedtuple("Person", "name Class age school")

person = Person("Prince", "16th", 28, "St. Mary")

print(person.name, person.Class, person.age, person.school)

print(person._fields)
print(person._asdict())
print(person._field_defaults)