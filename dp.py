import sys
import time
import os
import tracemalloc


def addEdge(adj, x, y):
    adj[x].append(y)
    adj[y].append(x)


def dfs(adj, dp, src, par):
    for child in adj[src]:
        if child != par:
            dfs(adj, dp, child, src)

    for child in adj[src]:
        if child != par:
            # not including source in the vertex cover
            dp[src][0] = dp[child][1] + dp[src][0]

            # including source in the vertex cover
            dp[src][1] = dp[src][1] + min(dp[child][1], dp[child][0])


def minSizeVertexCover(adj, N):
    tracemalloc.start()
    start_time = time.time()

    dp = [[0 for j in range(2)] for i in range(N + 1)]
    for i in range(1, N + 1):
        # 0 denotes not included in vertex cover
        dp[i][0] = 0

        # 1 denotes included in vertex cover
        dp[i][1] = 1

    dfs(adj, dp, 1, -1)

    # printing minimum size vertex cover
    print("MVC =", min(dp[1][0], dp[1][1]))

    end_time = time.time()
    _, peak_mem_usage = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    delta_time = end_time - start_time

    # WRITE TRACE FILES
    with open("Output/" + inputfile.split(".")[0] + "_DP.trace", "w") as f:
        f.write("%.2f seconds, %.2f bytes\n" % (delta_time, peak_mem_usage))


inputfile = sys.argv[1]
with open(inputfile, "r") as f:
    # number of nodes in the tree
    N = int(f.readline().split()[0])

    # adjacency list representation of the tree
    adj = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        neighbors = f.readline().split()
        for neighbor in neighbors:
            addEdge(adj, i, int(neighbor))


_, inputfile = os.path.split(inputfile)
minSizeVertexCover(adj, N)
