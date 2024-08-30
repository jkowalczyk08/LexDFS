from typing import Optional, List, TypeVar, Generic

from model.lex_bfs_plus.node import Node

T = TypeVar('T')


class DoublyLinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None

    def append(self, node: Node[T]):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def prepend(self, node: Node[T]):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_before(self, node: Node[T], new_node: Node[T]):
        new_node.next = node
        new_node.prev = node.prev
        if node.prev is not None:
            node.prev.next = new_node
        node.prev = new_node

        if self.head is node:
            self.head = new_node

    def insert_behind(self, node: Node[T], new_node: Node[T]):
        new_node.next = node.next
        new_node.prev = node
        if node.next is not None:
            node.next.prev = new_node
        node.next = new_node

        if self.tail is node:
            self.tail = new_node

    def delete(self, node: Node[T]):
        if self.head is None:
            return

        if self.head is node:
            self.head = node.next

        if self.tail is node:
            self.tail = node.prev

        if node.next is not None:
            node.next.prev = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        node.next = None
        node.prev = None

    def first(self) -> Node[T]:
        if self.head is None:
            raise Exception('Empty List')
        return self.head

    def last(self) -> Node[T]:
        if self.tail is None:
            raise Exception('Empty List')
        return self.tail

    def is_not_empty(self) -> bool:
        return self.head is not None

    def __iter__(self):
        self._current_node = self.head
        return self

    def __next__(self) -> Node[T]:
        if self._current_node is None:
            raise StopIteration
        next_result = self._current_node
        self._current_node = self._current_node.next
        return next_result

    def __str__(self) -> str:
        result: List[T] = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next

        return str(result)
