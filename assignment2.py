def not_bad(s):
    no=s.find('not')
    bad=s.find('bad')
    if  no < bad:
        s = s.replace(s[no:bad+3],'good')
    return s;


#
# x=not_bad("Food is not very bad")
# print(x)
def verbing(s):
    if len(s)>=3:
        if s[-3:]=='ing':
            s+='ly'
        else:
            s+='ing'
    return s;


# x=verbing('do')
# print(x)
def front_back(a, b):
    if len(a)%2==0 and len(b)%2==0:
        fra = a[0:int(len(a)/2)]
        bka = a[int(len(a)/2):]
        frb = b[0:int(len(b) / 2)]
        bkb = b[int(len(b) / 2):]
      
    elif len(a)%2!=0 and len(b)%2==0:
        fra = a[0:int((len(a)/2)+1)]
        bka = a[int((len(a)/2)+1):]
        frb = b[0:int(len(b) / 2)]
        bkb = b[int(len(b) / 2):]
     
    elif len(a)%2==0 and len(b)%2!=0:
        fra = a[0:int(len(a) / 2)]
        bka = a[int(len(a) / 2):]
        frb = b[0:int((len(b) / 2) + 1)]
        bkb = b[int((len(b) / 2) + 1):]
   
    elif len(a)%2!=0 and len(b)%2!=0:
        fra = a[0:int((len(a) / 2) + 1)]
        bka = a[int((len(a) / 2) + 1):]
        frb = b[0:int((len(b) / 2) + 1)]
        bkb = b[int((len(b) / 2) + 1):]
      

    else:
        return a+b
    return fra+frb+bka+bkb

# x=front_back('abcde','xyz')
# print(x)
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():

  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')


  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")


  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()