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

    while search_queue:
        person = search_queue.popleft()
        for friend in person.friends:
            print(f"Checking {friend.name}")
            if is_a_developer(friend):
                print(
                    f"{friend.name} is a friend of {person.name} and is a developer! Let me ask them for a code review."
                )
                return friend
            else:
                print(f"Adding {friend} to queue")
                search_queue.append(friend)
    return False


def main():

    brandon = Person("Brandon", "Cloud Engineer")
    joe = Person("Joe", "Security Consultant")
    jeff = Person("Jeff", "Developer")
    tom = Person("Tom", "Analyst")

    brandon.friends.append(joe)
    brandon.friends.append(tom)

    tom.friends.append(jeff)

    dev = find_developer(brandon)
    print(f"I found {dev.name}! Maybe he can help me code a game.")


if __name__ == "__main__":
    main()
