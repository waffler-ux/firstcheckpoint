#question 1
lst = [2, 3, 6]

result = 1
for num in lst:
    result *= num

print("Result =", result)

#question2
lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lst.sort(key=lambda x: x[-1])

print(lst)



#question3
s = {'a': 100, 'b': 200, 'c': 300}
d = {'a': 300, 'b': 200, 'd': 400}

result = s.copy()

for key, value in d.items():
    if key in result:
        result[key] += value
    else:
        result[key] = value

print(result)
#question4
n = 8

result = {}

for i in range(1, n + 1):
    result[i] = i * i

print(result)
#question5


lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

sorted_lst = sorted(lst, key=lambda x: float(x[1]), reverse=True)

print(sorted_lst)

#question6

s = {0, 1, 2, 3, 4}
print("Set:", s)
for item in s:
    print(item)

s.add(5)
print("adding 5:", s)
s.remove(2)   
print("removing 2:", s)
s.discard(10)  
print("discard:", s)