class Cell:
    def __init__(self, amount):
        self.amount = int(amount)

    def __str__(self):
        return f"The cell: {self.amount * '*'}"

    def __add__(self, other):
        return f"Add {Cell(self.amount + other.amount)}"

    def __sub__(self, other):
        return f"Sub {Cell(self.amount - other.amount)}" if (self.amount - other.amount) > 0 \
            else print("First cell has less cellules")

    def __mul__(self, other):
        return f"Mul {Cell(self.amount * other.amount)}"

    def __truediv__(self, other):
        return f"Truediv {Cell(self.amount // other.amount)}"

    def make_order(self, cell_ord):
        order = ''
        for i in range(int(self.amount / cell_ord)):
            order += f"{'*' * cell_ord} \n"
        order += f"{'*' * (self.amount % cell_ord)}"
        return order


cell1 = Cell(6)
print(cell1)
cell2 = Cell(4)
print(cell2)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(2))
print(cell2.make_order(3))