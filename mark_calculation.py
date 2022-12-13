bro = [
100,
92.65,
97.5,
79.60,
96.55,
65.90,
77]
sum = 0
for x in bro:
    sum+= x

assignments = (sum/len(bro)) 

mt1 = 87
mt2 = 73
iclick = 58.2 * 4/3

no_iclick = assignments * 0.45 + mt1 * 0.07 + mt2 * 0.13 
curr = assignments * 0.45 + mt1 * 0.07 + mt2 * 0.13 + iclick * 0.05
print(no_iclick / 0.65)
print (curr / 0.7)
x = (60 - curr ) / 0.3

print(x)