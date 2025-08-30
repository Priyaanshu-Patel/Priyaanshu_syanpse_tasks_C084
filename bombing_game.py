land=[
[1,0,0,0,1],
[1,0,1,1,1],
[1,1,0,1,1],
[1,0,1,1,0],
[0,1,0,1,1]
]

n=len(land)


m=int(input("Enter m of the bombing splash mxm"))
if(m%2==0):
     print("m should be odd")
     m=int(input("re enter a correct m in splash mxm"))
best_splash=0
best_corner=(0,0)
best_center=(0,0)

def impact_counter(x,y):
        global best_splash,best_corner,best_center
        temp=0
        for i in range (x,x+m):
            for j in range(y,y+m):
                if land[i][j]==1:
                    temp+=1
                        
        if(temp>best_splash):
            best_splash=temp
            best_corner=(x,y)
            best_center = (int(x + m// 2),int(y + m// 2))
        



# x_count=0
# y_count=0             
# for i in land:
    
#      for j in i:
#         if j==1:
#             impact_counter(int(x_count-((m-1)/2)),int(y_count-((m-1)/2)))
#         x_count+=1
#      y_count+=1

for i in range(n - m + 1):     
    for j in range(n - m + 1): 
        cx = i + m// 2         
        cy = j + m// 2             
        if land[cx][cy] == 1:
            impact_counter(i, j)
            
               
              


corner_coords = (n - best_corner[0], best_corner[1] + 1)
center_coords = (n - best_center[0], best_center[1] + 1)

print("The best splash was at center: ",center_coords," with a Splash of: ",best_splash)
