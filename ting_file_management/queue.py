class Queue:
    def __init__(self):
        self.queue = []

    def __len__(self):
        return self.size()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None

    def search(self, index):
        if index < 0 or index >= self.size():
            raise IndexError
        else:
            return self.queue[index]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return not bool(self.queue)
