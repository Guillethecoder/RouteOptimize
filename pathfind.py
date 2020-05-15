class Set:
    """
    Union-Find Data Structure.
    Heuristics: path compression, union by rank.
    """

    def __init__(self, value):
        """
        Generate a set containing value.
        """
        self.value = value
        self.parent = self
        self.next = self
        self.rank = 0


    def findSet(self):
        """
        Returns the representative element of
        the set and applies path-compression.
        """
        pathToRoot = []
        element = self
        while element is not element.parent:
            pathToRoot.append(element)
            element = element.parent
        root = element
        for element in pathToRoot:
            element.parent = root
        return root


    def union(self, other):
        """
        Merges two sets applying union by rank.
        """
        selfRep = self.findSet()
        otherRep = other.findSet()
        if selfRep is not otherRep:
            if selfRep.rank < otherRep.rank:
                selfRep.parent = otherRep.parent
            else:
                otherRep.parent = selfRep.parent
                if selfRep.rank == otherRep.rank:
                    selfRep.rank += 1

            selfRep.next, otherRep.next = otherRep.next, selfRep.next


    def add(self, value):
        """
        Inserts value into the set.
        """
        self.union(Set(value))


    def getElements(self):
        """
        Generator for the elements in the set.
        """
        yield self.value
        element = self.next
        while element != self:
            yield element.value
            element = element.next


    def __str__(self):
        """
        Returns a string representing the set.
        """
        return ("{{{}}}".format(", ".join(map(str, self.getElements()))))

    def __repr__(self):
        """
        Represents the set.
        """
        return str(self)
