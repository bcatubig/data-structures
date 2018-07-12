from collections import deque


def is_a_developer(person):
    return person.occupation == "Developer"


class Person:
    def __init__(self, name, occupation="Student"):
        self._name = name
        self._occupation = occupation
        self._friends = []

    def __repr__(self):
        return f"<Person {self._name} - {self._occupation}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def friends(self):
        return self._friends

    @friends.setter
    def friends(self, friend):
        self._friends.append(friend)

    @property
    def occupation(self):
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        self._occupation = occupation


def find_developer(id):
    """Find a Developer in your friend group"""
    search_queue = deque()
    search_queue.append(id)
    checked_names = set()
    while search_queue:
        person = search_queue.popleft()

        print(
            f"Checking {person.name}'s friend(s): {list(friend.name for friend in person.friends)}'"
        )
        for friend in person.friends:
            if friend.name == id.name or friend.name in checked_names:
                continue
            print(f"Checking {friend.name}")
            if is_a_developer(friend):
                print(
                    f"{friend.name} is a friend of {person.name} and is a developer! Let me ask them for a code review."
                )
                return friend
            else:
                print(
                    f"{friend.name} isn't a developer, but one of his/her friends might be!"
                )
                search_queue.append(friend)
                checked_names.add(friend.name)
    return False


def main():

    brandon = Person("Brandon", "Cloud Engineer")
    joe = Person("Joe", "Security Consultant")
    jeff = Person("Jeff", "Developer")
    tom = Person("Tom", "Analyst")
    xander = Person("Xander", "Astronaut")

    brandon.friends.append(xander)
    brandon.friends.append(joe)
    brandon.friends.append(tom)

    tom.friends.append(jeff)
    xander.friends.append(joe)

    joe.friends.append(brandon)

    dev = find_developer(brandon)
    if dev:
        print(f"I found {dev.name}! Maybe he/she can help me code a game.")
    else:
        print("Nah! Didn't find any dev friends")


if __name__ == "__main__":
    main()
