animals = ["dog", "cat", "lion", "tiger"]
example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(example[2:8])
print(example[:8])
print(example[-5: -1])
print(animals + example)
print(('d' in animals))
print(len(animals))
print(max(example))
print(min(example))
print(list("guatam"))
data = list("simplebook")
print(len(data))
data[6:] = list('mikes')
print(data)
data[5:] = []
print(data)
a, b, c, d = animals
x, y, z = "Orange", "Banana", "Cherry"
print(type(a))