p = 1
while(1):
  a,c,z = [],[],0
  a1 = input()
  if a1 == 'z':
    break
  a2,a3,a4,a5,a6  = input(),input(),input(),input(),input()
  a = [list(a1),list(a2),list(a3),list(a4),list(a5)]
  for i in range(len(a)):
    for j in range(len(a[i])):
      if a[i][j] == ' ':
        m,n = i,j
  b = list(a6)
  for k in range(len(b)):
    if b[k] == 'A':
      if m == 0:
        print('this puzzle has no configaration')
        break
      else:
        a[m][n],a[m-1][n] = a[m-1][n],a[m][n]
        m,n = m-1,n
    elif b[k] == 'B':
      if m == 4:
        print('this puzzle has no configaration')
        break
      else:
        a[m][n],a[m+1][n] = a[m+1][n],a[m][n]
        m,n = m+1,n
    elif b[k] == 'L':
      if n == 0:
        print('this puzzle has no configaration')
        break
      else:   
        a[m][n],a[m][n-1] = a[m][n-1],a[m][n]
        m,n = m,n-1
    elif b[k] == 'R':
      if n == 4:
        print('puzzle has no fial configaration')
        break
      else:
        a[m][n],a[m][n+1] = a[m][n+1],a[m][n] 
        m,n = m,n+1
    else:
      print("puzzle #",end = '')
      print(p)
      for i in range(len(a)):
        for j in range(len(a[i])):
          print(a[i][j],end = ' ') 
        print()
      p += 1
      
    
