#1
'''d=[1,2,3,4,5,6,7,8,9]

def func(d,i):
	if (i*3)>=len(d):
		return  
	print(d[i*3])
	return func(d,i+1)

func(d,0)'''
#2
'''a=int(input())
b=int(input())
k=0
for i in range(a,b+1):
	if i%2==1:
		k+=1
print(k)'''
#3
'''senten=input()
def cap_sentence(senten):
	return ' '.join(w[0].upper() + w[1:] for w in senten.split(' ')) 
print(cap_sentence(senten))''' 
#4
"""
with '''open('smth', encoding='utf-8')''' as g:
    file = [[el.strip() for el in line.split(',')] for line in g]
	h={}
	for line in g:
		key=g[0]
		if key not in h:
			h[key]=[]
		h[key].append(g[1:])
	print(h)"""
#5
diction={...}
i = 0
max_age = smth[i]
for el in diction :
	dict[el]=value
	if max_age<value:
		max_age=value
print(value)






