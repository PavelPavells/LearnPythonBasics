from collections import Counter, defaultdict, OrderedDict
li = [1,2,3,4,5,6,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(int, {'a': 1, 'b': 2})
print(dictionary['b'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2
print(d)