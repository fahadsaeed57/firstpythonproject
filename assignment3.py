def match_ends(words):
   count=0
   for x in words:
       if len(x)>=2 and x[0]==x[-1]:
           count=count+1
   return count

# x=match_ends(['xyx','xyz','xyx'])
# print(x)

def front_x(words):
    list2=[]
    word2=[]
    for x in words:
        if x[0:1]=='x':
            list2.append(x)
        else:
            word2.append(x)
    return sorted(list2)+sorted(word2)
# z=front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
# print(z)

def sort_last(tuples):
        return sorted(tuples,key=lambda x: x[1])
# z=sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
# print(z)
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '

    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():

    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)


    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()


