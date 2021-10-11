def printRev ( n ):
  if n >= 0 :
    print( n )
    if n == 0:
      print('BOOMMMMM !!!')
      return
    printRev( n - 1)

n = 10
printRev( n )