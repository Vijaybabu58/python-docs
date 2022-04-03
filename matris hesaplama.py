x=[[1,3,5],[2,3,6],[6,7,8]]
y=[[4,2,6],[8,3,1],[5,9,4]]
z=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for a in range(len(y)):
        z[i][a]=x[i][a]+y[i][a]
        print(z)