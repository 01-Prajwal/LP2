visited =[]
queue =[]

graph = {
  5 : [3,7],
  3 : [2, 4],
  7 : [8],
  2 : [],
  4 : [8],
  8 : []
}


def bfs(visited,graph,node):

    visited.append(node)
    queue.append(node)

    while queue:
        front = queue.pop(0)
        print(front , end=" ")
        for neigh in graph[front]:
            if neigh not in visited:
             visited.append(neigh)
             queue.append(neigh)


bfs(visited,graph,5)

