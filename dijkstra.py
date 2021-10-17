def shortest_path(n,edges,s):    
    dists=[10000 for i in range(n)]
    dists[s-1]=0
    T=list(range(1,n+1))
    for _ in range(n):
        mInd=T[0]
        for vert in T:
            mInd+=(vert - mInd)*(dists[vert-1] < dists[mInd-1])
        T.remove(mInd)
        #if given list of edges, on undirected graph.
        for e in edges:
                dists[e[0]-1]+= (dists[mInd-1]+e[2] - dists[e[0]-1])*(e[1] == mInd and dists[mInd-1]+e[2] < dists[e[0]-1])
                dists[e[1]-1]+= (dists[mInd-1]+e[2] - dists[e[1]-1])*(e[0] == mInd and dists[mInd-1]+e[2] < dists[e[1]-1])
    dists.pop(s-1)
    for i in range(len(dists)):
        dists[i]-= 10001*(dists[i] == 10000)
    return dists
    