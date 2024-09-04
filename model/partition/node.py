from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None

    def __str__(self):
        return str(self.data)
