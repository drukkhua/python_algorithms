'''Program with some examples with OOP & JSON'''

import json
from json import JSONEncoder


class Encoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Student:  # full_name:str, avg_rank: float, courses:list

    def __init__(self, full_name, avg_rank, courses):
        self.full_name = full_name
        self.avg_rank = avg_rank
        self.courses = courses

    @classmethod
    def from_json(cls, file):
        with open(file) as json_file:
            dictionary = json.load(json_file)
        return cls(**dictionary)

    def __str__(self):
        return f"{self.full_name} ({self.avg_rank}): {self.courses}"

    def serialize_to_json(self, json_file):
        with open(json_file, "w") as write_file:
            json.dump(self, write_file, cls=Encoder)

    @classmethod
    def serialize_list_to_json(cls, students, file):
        with open(file, "w") as write_file:
            json.dump(students, write_file, cls=Encoder)


class Group:  # title: str, students: list
    def __init__(self, title):
        self.title = title
        self.students = []

    def __str__(self):
        return f"{self.title}: {[str(Student(**item)) for item in self.students]}"

    @classmethod
    def create_group_from_file(cls, students_file):
        with open(students_file) as read_file:
            students = json.load(read_file)
            g = Group(title=str(students_file).split(".")[0])
            if isinstance(students, list):
                g.students = students
            else:
                g.students = [students]
            return g

    @classmethod
    def serialize_to_json(cls, groups, file):
        with open(file, "w") as write_file:
            json.dump(groups, write_file, cls=Encoder)


def print_file(file_name):
    with open(file_name, 'r') as f:
        for line in f.readlines():
            print(line, end="")


user1 = Student.from_json("2020-01.json")
print(user1)

with open("2020_2.json") as read_file:
    user2 = json.load(read_file)
print([str(Student(**item)) for item in user2])

g1 = Group.create_group_from_file("2020_2.json")
g2 = Group.create_group_from_file("2020-01.json")
Group.serialize_to_json([g1, g2], "g1")
print_file("g1")

g1 = Group.create_group_from_file("2020_2.json")
print(g1)

g2 = Group.create_group_from_file("2020-01.json")
print(g2)
