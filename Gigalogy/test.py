class Perent(object):
    x = 1

class child1(Perent):
    pass

class child2(Perent):
    pass


print(Perent.x, child1.x, child2.x)
child1.x = 2
print(Perent.x, child1.x, child2.x)
Perent.x = 3
print(Perent.x, child1.x, child2.x)