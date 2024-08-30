from typing import TypeVar, Generic

from model.lex_bfs_plus.node import Node

T = TypeVar('T')


class Interval(Generic[T]):
    def __init__(self, start: Node[T], end: Node[T]):
        self.start: Node[T] = start
        self.end: Node[T] = end

    def pop_start(self):
        self.start = self.start.next

    def pop_end(self):
        self.end = self.end.prev

    def pop(self, node: Node[T]):
        if node is self.start:
            self.start = self.start.next
        elif node is self.end:
            self.end = self.end.prev

    def is_singleton(self) -> bool:
        return self.start == self.end

    def __str__(self):
        return f'(start: {self.start}, end: {self.end})'
