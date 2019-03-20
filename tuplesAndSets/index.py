tup = (1, 2, 3)
# can be used like a list except it's immutable
# can use slice, len, loop over it, accessing is tup[1], use index to check the index

# sets are grouping of values without order and no duplicates
# cannot accessing via index 
s = {1, 2, 3, 4, 5, 5, 5,} #print out {1, 2, 3, 4, 5}
output = 6 in s
# print(output)

# for num in s:
    # print(num)

# can also create a set be using set('iterable item)
print(set(['Los Angeles', 'Tokyo', 'Berlin', 'Osaka', 'Toronto', 'Vancouver', 'Vancouver', 'Tokyo']))
