#黑白图像问题
data = [[1,0,0,1,0,0],
       [0,0,1,0,1,0],
       [0,0,0,0,0,0],
       [1,1,0,0,0,0],
       [1,1,1,0,0,0],
       [0,1,0,1,0,0]]

def dfs(x, y, mat, vis):
    #0格子或已经访问过的格子返回
    #这里的0格子是外面的一圈边界
    if mat[x][y] == 0 or vis[x][y]:
        return
    vis[x][y]=1
    #访问相连的八个格子
    dfs(x-1,y,mat,vis)
    dfs(x+1,y,mat,vis)
    dfs(x,y-1,mat,vis)
    dfs(x,y+1,mat,vis)
    dfs(x-1,y-1,mat,vis)
    dfs(x-1,y+1,mat,vis)
    dfs(x+1,y-1,mat,vis)
    dfs(x+1,y+1,mat,vis)
MAXN=len(data)
vis = [[0]*(MAXN+2) for _ in range(MAXN+2)]
mat = [[0]*(MAXN+2) for _ in range(MAXN+2)]
#data外面加上一圈虚拟的白格子
for x in range(MAXN):
    for y in range(MAXN):
        mat[x+1][y+1] = data[x][y]
cnt = 0
for x in range(1,MAXN+1):
    for y in range(1,MAXN+1):
        #未访问过且为1格子
        if mat[x][y]==1 and not vis[x][y]:
            #通过dfs访问(x,y)格子
            dfs(x,y,mat,vis)
            cnt+=1
print(cnt)
