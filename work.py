def union(lista, listb):
    result = [x for x in lista if x not in listb] + listb
    return result
    
print union([1,2], [1])# [1,2]
print union([1,2], [1,2,3])#[1,2,3]
print union([1,3,5,7], [2,4,6,7])#[1,2,3,4,5,6,7]

def intersection(lista, listb):
    return [x for x in lista if x in listb]

print intersection([1,2], [1])# [1]
print intersection([1,2], [1,2,3])#[1,2]
print intersection([1,3,5,7], [2,4,6,7])#[7]

def diff(lista, listb):
    return [x for x in lista if x not in listb]

print diff([1,2], [1])# [2]
print diff([1,2], [1,2,3])#[]
print diff([1,3,5,7], [2,4,6,7])#[1,3,5]

def symdiff(lista, listb):
    return diff(union(lista,listb), intersection(lista,listb))

print symdiff([1,2], [1])# [2]
print symdiff([1,2], [1,2,3])#[3]
print symdiff([1,3,5,7], [2,4,6,7])#[1,2,3,4,5,6]

def cart(lista, listb):
    return [(a,b) for a in lista for b in listb]

print cart([1,2], [1])# [[1,1], [1,2]]
print cart([1,2], [1,2,3])#[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3]]
print cart([1,3,5,7], [2,4,6,7])#something large
