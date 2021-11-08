import random 
a=[4, 5 ,1 ,6, 7, 8, -1 ,-6, -3, -6]
def quick_sort(a):
    if len(a)>1:
        x=a[random.randint(0, len(a)-1)]
        l=[n for n in a if n<x ]
        e=[n for n in a if n==x]
        h=[n for n in a if n>x]
        a=quick_sort(l)+e+quick_sort(h)
    return a
s=quick_sort(a)
print('Сортований список - ' , s)
b=int(input("Введіть значення "))
if b in a: 
    print('Значення ' ,b,' є в списку')
else:
    print('Значення немає в списку')
print('Середнє арифметичне - ' ,sum(a)/len(a))
p=str(input('Введіть послідовність через кому '))
a=str(a)
s=str(s)
if p in a:
    print('Послідовність ', p, ' є в списку')
elif p in s:
    print('Послідовності ', p ,' немає в основному списку, але є в сортованому списку')
else:
    print('Послідовності немає')
print("П'ять мінімальних елементів")
for i in range(0,5):
    print(s[i])
v=sorted(a, reverse=True)
print("П'ять максимальних елементів")
for x in range(0,5):
        print(v[x])
def f(a):
    n=[]
    for i in a:
        if i not in n:
            n.append(i)
    return n 
print(f(s))