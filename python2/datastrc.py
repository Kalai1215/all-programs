a=['a','b','c','d','e','f','g','h']
print(type(a))

print(a[4])

a[4]='z'
print(a)

a.remove('f')
print(a)

a.pop()
print(a)

a.pop(5)
print(a)

a.clear()
print(a)

#del a
#print(a)

a=[5,6,2,5,2,3]

print(len(a))

a.sort()
print(a)

a.reverse()
print(a)

b=a.copy()
print(b)

del b[2:4]
print(b)

del(b[2])
print(a)

del b

print(a.count(5))

print(max(a))

print(min(a))

print(sum(a))



#advanced

a=['a','b','c','d']
a.append('e')
print(a)

a.append(['f','g'])
print(a)

a.extend(['h','i','j'])
print(a)

a.insert(2,'z')
print(a)

a.insert(3,[1,2,3])
print(a)

print("----------------------------------------------------------------------")

#tuples

a=(4,7,5,9,2)
print(a.count(5))

print(max(a))

print(min(a))

print(sum(a))

print(len(a))

print(a[2])

print(a.index(2))

print("----------------------------------------------------------------------")

#set

a={3,6,2,5,7,9}

a.add(8)
print(a)

a.update({10,20})
print(a)

a.discard(3)
print(a)


#advanced

a={'a',1,2,'d'}
b={'b',1,2,'c'}

print(a.union(b))

print(a.intersection(b))

print(a.difference(b))

print(a.symmetric_difference(b))

print(a|b)

print(a^b)

print(a-b)

print(a&b)

a={'a','b','c'}
b={1,'a','c',2,'b',3}

print(b.issubset(a))

print(a.issubset(b))

print(a.issuperset(b))


print(b.issuperset(a))

#for j in range(16,0,-1):
print(list(range(1,16,1)))

#update

a={1,2,3,4}
b={5,6,1,2}


print(b.difference(a))
print(b)
b.difference_update(a)   
print(b)                 

a={1,2,3,4}
b={5,6,1,2}

b.symmetric_difference_update(a)
print(b)

a={1,2,3,4}
b={5,6,1,2}
print(b.union(a))

print(b)

b.intersection_update(a)
print(b)

a={i for i in range(18,0,-1)}
print(a)






