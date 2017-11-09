def both_ends(s):
   if len(s)>=2:
       x=s[0:2]
       y=s[-2:]
       return x+y
   else:
       return ''
# x=both_ends('spring')
# print(x)

def mix_up(a, b):
  if len(a) >=2 and len(b) >=2:
      x=a.replace(a[0:2],b[0:2])
      y=b.replace(b[0:2],a[0:2])
      return x+" "+y
  else:
      return a+b

# x=mix_up('dog','dinner')
# print(x)
def fix_start(s):
    if len(s)>=1:
        new_str = s[1:].replace(s[0], '*')
        return s[0]+new_str
    else:
        return s;
# x=fix_start("aardvark")
# print(x)
def donuts(count):
  if count >=10:
    count='many'
  return 'Number of donuts: {0}'.format(count)


def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print('donuts')
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')


    print('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')


    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')


    print('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

