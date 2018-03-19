import copy

# Replace a with data from lidar
a = [0,0,0,0,0,0,0,3,2,2,3,2,2,3,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0]
b = copy.deepcopy(a)

threshold =  0.001
change = 10.0
it = 0
while change >= threshold:
	change = 0.0
	it+=1
	for i in range(len(a)):
		aux = b[i]
		b[i]+=  (0.02*(a[i]-b[i]))  + (0.2*(b[i-1]+b[(i+1)%len(a)]-2*b[i]))
		change += abs(aux-b[i])

robots = []
for i in range(len(a)):
	if b[(i+1)%len(a)]<b[i] and b[i-1]<b[i]:
		print (b[i],b[i-1])
		robots.append(i)


print (a)
print(["%.1f" % x for x in b])
print (robots)