class ClassQueue:
    def __init__(self):
        self.queue = []

    def add(self, queue):
        return self.queue.append(queue)

    def remove(self):
        return self.queue.pop(0)
