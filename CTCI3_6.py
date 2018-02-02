#Animal shelter.  A shelter which holds dogs and cats operates on a strictly first in first out basis.  you can select
# a dog or a cat and you will get the oldest dog or cat respectively.  Implement this data struture with the functions
#enqueue, dequeueAny, dequeueDog, dequeueCat

class animalQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]

    def enqueue(self,item):
        self.items.append(item)

    def dequeueAny(self):
        tmp = self.items[0]
        self.items.__delitem__(0)
        return tmp

    def dequeueDog(self):
        for x in range(0,len(self.items)):
            if self.items[x] == "Dog":
                dog = self.items[x]
                self.items.__delitem__(x)
                return dog
        print("no dogs available.")


    def dequeueCat(self):
        for x in range(0,len(self.items)):
            if self.items[x] == "Cat":
                cat = self.items[x]
                self.items.__delitem__(x)
                return cat
        print("no cats available.")

    def display(self):
        print(self.items)
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    shelter = animalQueue()
    shelter.enqueue("Dog")
    shelter.enqueue("Dog")
    shelter.enqueue("Cat")
    shelter.display()
    shelter.dequeueAny()
    shelter.display()
    shelter.dequeueCat()
    shelter.display()
    shelter.dequeueDog()
    shelter.display()

    shelter.enqueue("Cat")
    shelter.enqueue("Cat")
    shelter.enqueue("Dog")
    shelter.display()
    shelter.dequeueAny()
    shelter.display()
    shelter.dequeueDog()
    shelter.display()
    shelter.dequeueCat()
    shelter.display()