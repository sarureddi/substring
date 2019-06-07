st1=input()
flag31=0
for i in range(0,len(st1)-1):
  for j in range(i+1,len(st1)):
    if st1[i]<st1[j]:
      flag31=1
      print(st1[j:])
      break
  if flag31==1:
    break
else:
  print(st1)
