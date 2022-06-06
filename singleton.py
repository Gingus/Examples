# Course on LinkIn Learning, Python: Design Patterns-2422610 by Jungwoo Ryoo
class Borg:
    """The Borg design pattern"""
    _shared_data = {}  # Attribute dictionary

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute dictionary


class Singleton(Borg):
    """The Singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)

    def __str__(self):
        return str(self._shared_data)


# Lets create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Test Transfer Protocol")


# Print the object
print(x)
# Lets create another singleton and if it refers to the same
# attributes dictionary by adding another acronym

y = Singleton(SNMP="Simple Network Management Protocol")
print(y)
