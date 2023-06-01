def dfs(player,board_size,source):
    graph={}
    for i in range(board_size):
       for j in range(board_size):
            if (i,j) in player.area:
                graph[(i,j)]=1
            else:
                graph[(i,j)]=0
    discovered={}
    for i in range(board_size):
        for j in range(board_size):
            if (i,j) == source:
                graph[(i,j)]=1
            else:
                graph[(i,j)]=0
    if (source[0]+1,source[1]) in player.area:           
        dfs_rec(discovered,(source[0]+1,source[1]),board_size,player)
    if (source[0]-1,source[1]) in player.area:
        dfs_rec(discovered,(source[0]-1,source[1]),board_size,player)
    if (source[0],source[1]+1) in player.area:
        dfs_rec(discovered,(source[0],source[1]+1),board_size,player)
    if (source[0],source[1]-1) in player.area:
        dfs_rec(discovered,(source[0],source[1]-1),board_size,player)
    return discovered

    
def dfs_rec(discovered,source,board_size,player):
    if source[0]<0 or source[0]>=board_size or source[1]<0 or source[1]>=board_size:
        return
    discovered[curr]=1
    if (source[0]+1,source[1]) in player.area:           
        dfs_rec(discovered,(source[0]+1,source[1]),board_size,player)
    if (source[0]-1,source[1]) in player.area:
        dfs_rec(discovered,(source[0]-1,source[1]),board_size,player)
    if (source[0],source[1]+1) in player.area:
        dfs_rec(discovered,(source[0],source[1]+1),board_size,player)
    if (source[0],source[1]-1) in player.area:
        dfs_rec(discovered,(source[0],source[1]-1),board_size,player)


def has_closed(player,board_size,new_pos):
    #check that starting point of half captured in our area, that the previous position left
    # our area and that new_pos in our area
    if len(player.halfCaptured)!=0 and player.halfCaptured[0] in player.area and (not player.position in player.area) and new_pos in player.area:
        #check that the start point and end point are connected
        discovered=dfs(player,board_size,player.halfCaptured[0])
        return discovered[new_pos]==1
    return False

def get_union_area(board_size,boundary,area):
    graph={}
    for i in range(-1,board_size+1):
        for j in range(-1,board_size+1):
            if (i,j) in area or (i,j) in boundary:
                graph[(i,j)]=0
            else:
                graph[(i,j)]=1
    discovered={}
    dfs_rec_for_union(discovered,(-1,-1),board_size,graph)
    return discovered

    
def dfs_rec_for_union(discovered,source,board_size,graph):
    if source[0]<-1 or source[0]>board_size or source[1]<-1 or source[1]>board_size:
        return
    discovered[curr]=1
    if graph[(source[0]+1,source[1])]==1:           
        dfs_rec(discovered,(source[0]+1,source[1]),board_size,graph)
    if graph[(source[0]-1,source[1])]==1:
        dfs_rec(discovered,(source[0]-1,source[1]),board_size,graph)
    if graph[(source[0],source[1]+1)]==1:
        dfs_rec(discovered,(source[0],source[1]+1),board_size,graph)
    if graph[(source[0],source[1]-1)]==1:
        dfs_rec(discovered,(source[0],source[1]-1),board_size,graph)
    
