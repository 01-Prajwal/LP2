selected_node=[0,0,0,0,0]

no_of_edge = 0 

selected_node[0]= True

N=5

INF = 999999
while no_of_edge < N -1 :
    a= 0 
    b = 0 
    mini = INF

    for i in range(N):
        if selected_node[i]:
            for j in range(N):
                if((not selected_node[j] ) and G[i][j]):
                    if mini > G[i][j]:
                        mini = G[i][j]
                        a =i
                        b =j     
        
    print()
    no_of_edge +=1
    selected_node[b]=True