# Sets do not repeat numbers
s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(3)
s.add(4)

print(s)

s.remove(2)

print(s)
