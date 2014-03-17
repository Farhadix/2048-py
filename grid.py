import random

class Grid():
    cells = ['' for i in range(16)]
    size = 4

    def __init__(self, size):
        self.size = size
        self.cells[self.get_rnd_position()] = self.get_rnd_number()
        self.cells[self.get_rnd_position()] = self.get_rnd_number()

    def print_table(self):
        values = [self.cells[i] for i in range(self.size * self.size)]
        
        table = """
+----+----+----+----+
|%4s|%4s|%4s|%4s|
+----+----+----+----+
|%4s|%4s|%4s|%4s|
+----+----+----+----+
|%4s|%4s|%4s|%4s|
+----+----+----+----+
|%4s|%4s|%4s|%4s|
+----+----+----+----+""" % tuple(values)

        return table
       
    def get_rnd_number(self):
        return 2 if random.random() < 0.9 else 4

    def get_rnd_position(self):
        while True:
            rnd_position = int(random.random() * (self.size - 1))
            if not self.cells[rnd_position]:
                return rnd_position


