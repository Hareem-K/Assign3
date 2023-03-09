import threading
import random
import time

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.head = self.tail = -1
        self._lock = threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

    def enqueue(self, data):
        while True:
            # Try to acquire lock on the queue
            self.lock()

            # Check if queue is full
            if (self.tail + 1) % self.size == self.head:
                # Queue is full, wait for 1 second and try again
                self.unlock()
                time.sleep(1)
                continue
            else:
                # Queue has space, insert the element and release the lock
                if self.head == -1:
                    # First element
                    self.head = 0
                self.tail = (self.tail + 1) % self.size
                self.queue[self.tail] = data
                self.unlock()
                return

    def dequeue(self):
        while True:
            # Try to acquire lock on the queue
            self.lock()

            # Check if queue is empty
            if self.head == -1:
                # Queue is empty, wait for 1 second and try again
                self.unlock()
                time.sleep(1)
                continue
            else:
                # Queue has elements, remove the head element and release the lock
                data = self.queue[self.head]
                if self.head == self.tail:
                    # Last element
                    self.head = -1
                    self.tail = -1
                else:
                    self.head = (self.head + 1) % self.size
                self.unlock()
                return data


def producer():
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)
        
        # Wait for num seconds
        time.sleep(num)
        
        # Enqueue the number to the queue
        q.lock()
        if (q.tail + 1) % q.size == q.head:
            # Queue is full
            q.unlock()
            continue
        elif q.head == -1:
            # First element
            q.head = 0
            q.tail = 0
            q.queue[q.tail] = num
        else:
            q.tail = (q.tail + 1) % q.size
            q.queue[q.tail] = num
        q.unlock()

def consumer():
    while True:
        # Generate a random number between 1 and 10
        num = random.randint(1, 10)
        
        # Wait for num seconds
        time.sleep(num)
        
        # Dequeue a number from the queue and print it to the terminal
        q.lock()
        if q.head == -1:
            # Queue is empty
            q.unlock()
            continue
        else:
            data = q.queue[q.head]
            if q.head == q.tail:
                # Last element
                q.head = -1
                q.tail = -1
            else:
                q.head = (q.head + 1) % q.size
            q.unlock()
            print(data)


if __name__ == '__main__':
    q = CircularQueue(5)
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()