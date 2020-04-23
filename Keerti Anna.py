from collections import deque
class Veterinarian:
    def __init__(self):
        self.list = deque()

    def accept(self, petName):
        self.list.append(petName)
        print(self.list)

    def heal(self):
        try:
            return self.list.popleft()
        except:
            return "IndexError Exception"


veterinarian = Veterinarian()
veterinarian.accept("Barkley")
veterinarian.accept("Mittens")
print(veterinarian.heal())
print(veterinarian.heal())


from collections import defaultdict
def find_unique_numbers(numbers):
    d = defaultdict(int)
    result = []
    for i in numbers:
        d[i] += 1
    for j in d.items():
        if j[1] == 1:
            result.append(j[0])
    return result
print(find_unique_numbers([1, 2, 1, 3]))