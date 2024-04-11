from typing import List

class Order:

    def __init__(self, n: int) -> None:
        self.n: int = n
        self.position: List[int] = [0] * n

    def __getitem__(self, i: int) -> int:
        return self.position[i]
    
    def __setitem__(self, value: int, i: int) -> None:
        self.position[i] = value

    def __str__(self) -> str:
        return str(self.position)
    
    def reverse(self) -> None:
        pass

order = Order(5)

order[0] = 3
order[1] = 2
order[2] = 0
order[3] = 4
order[5] = 1

print(order)

order.reverse()

print(order)