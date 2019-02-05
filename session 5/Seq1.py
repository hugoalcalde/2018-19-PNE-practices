class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print("New empty sequence created")
        self.strbases = strbases
    def len(self):
        return len(self.strbases)
class Gene(Seq):
    """This class is derived from the Seq
       All the objects of class Gene will
       inheritage from methods from Seq Class"""
    pass


s1 = Gene("ATTCGATCC")
s2 = Seq("AAGG")


str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("The sequences inside the object are : " , str1 , str2)
print("The length of the sequence 1 is {} and the length of the sequence 2 is {}".format(l1,l2))
print("The end")