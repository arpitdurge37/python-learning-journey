# s = {1, 45, 33, 87, 65, 3, 3, "Arpit"}

# s.add(566)

# print(s, type(s))

# print(len(s))
# s.remove(33)
# print(s)
# s.pop()
# print(s)


s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1.union(s2))
print(s1.intersection(s2))        
print(s1.difference(s2))
print(s2.difference(s1))

s1.add(10)
s2.discard(5)

print(s1, s2)