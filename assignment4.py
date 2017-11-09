def remove_adjacent(nums):
  list = []
  for i in range(0,len(nums)-1):
      if nums[i]==nums[i+1]:
          continue
      else:
          list.append(nums[i])
  return list+nums[-1:]

# x=remove_adjacent([1, 2, 2, 3])
# print(x)

def linear_merge(list1, list2):
    list3=list1+list2
    return sorted(list3)

# x=linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
# print(x)
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():

  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])


  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
