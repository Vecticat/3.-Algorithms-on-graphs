l = [2, 12, 1234, 11, 5]
# l = [1,2,5,7]
print([sorted(l, reverse=True).index(x) for x in l])




a = {'a': [2, 3], 'b': [3,4]}
for i in a['a']:
    print(i)