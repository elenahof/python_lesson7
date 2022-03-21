class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        for el in self.mtrx:
            for i in el:
                print(f"{i:3}", end="")
            print()
        return ""

    def __add__(self, other):
        for a in range(len(self.mtrx)):
            for b in range(len(other.mtrx[a])):
                self.mtrx[a][b] = self.mtrx[a][b] + other.mtrx[a][b]
        return Matrix.__str__(self)

my_list = Matrix([[1, 4, 6, 8, 3], [4, 2, 2, 5, 9], [5, 8, 0, 9, 7]])
print(my_list.__str__())

new_list = Matrix([[8, 2, 4, 1, 5], [9, 3, 7, 6, 0], [4, 8, 5, 1, 5]])
print(new_list.__str__())

print("New Matrix:")
print(my_list.__add__(new_list))