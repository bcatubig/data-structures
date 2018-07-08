import uuid


class Box:
    def __init__(self, contents=None):
        self._id = uuid.uuid4()
        self._contents = contents

        print("Created box: {}".format(self._id))

    def __repr__(self):
        return "<Box {}>".format(self._contents)

    @property
    def contents(self):
        return self._contents

    @property
    def id(self):
        return self._id

    def contains_box(self):
        return isinstance(self._contents, Box)

    def found_key(self):
        return self._contents == "key"


def find_key(box):
    if box.found_key():
        print("I found the key in box {}!".format(box.id))
        return
    elif box.contains_box():
        print("Found a box! Opening box {}".format(box.contents.id))
        find_key(box.contents)

    else:
        print("Did not find a key!")
        return


def main():
    box1 = Box(contents=Box(contents=Box(contents=Box(contents="key"))))
    print(box1.contents)
    find_key(box1)


if __name__ == "__main__":
    main()
