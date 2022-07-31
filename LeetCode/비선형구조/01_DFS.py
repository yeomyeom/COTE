graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

def recursive_dfs(v, discover=[]):
    discover.append(v)
    for w in graph[v]:
        if not w in discover:
            discover = recursive_dfs(w,discover)
    return discover

print(recursive_dfs(1))
