'''
Problem source : LEETCODE(2210)
problem statement overview

both greater == hill
both lesser ==valley
one greater one lesser == neither hill nor valley

'''

# input for the list and valley

a=[2,4,1,1,6,5]
b=[]

# to find the length of the list
count_a=0
for i in a:
    count_a+=1

#filter the element from the reptivie element
for i in range(0,(count_a)):
    if i != count_a-1:
        if a[i] != a[i+1]:
            b.append(a[i])
    elif i == (count_a-1):
        b.append(a[i])

#length of the filter element
count_b=0

for i in b:
    count_b+=1

hill_and_valleys=0


for i in range (1,(count_b-1)):

        left_closest_neighbour=i-1
        right_closest_neighbor=i+1
        
        # both greater
        if b[left_closest_neighbour] > b[i] and b[right_closest_neighbor] > b[i]:
            hill_and_valleys+=1

        # both lesser
        elif b[left_closest_neighbour] < b[i] and b[right_closest_neighbor] < b[i]:
            hill_and_valleys+=1


print(hill_and_valleys)