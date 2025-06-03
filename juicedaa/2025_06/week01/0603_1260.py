def main():

    import sys
    from collections import deque

    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    order = []
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in graph:
        i.sort()

    def dfs(t):
        visited[t] = True
        order.append(t)
        for g in graph[t]:
            if not visited[g]:
                dfs(g)

    dfs(r)
    print(' '.join(map(str, order)))
    order = []

    visited = [False] * (n+1)
    def bfs(t):
        q = deque()
        visited[t] = True
        q.append(t)
        order.append(t)
        while q:
            x = q.popleft()
            for g in graph[x]:
                if not visited[g]:
                    order.append(g)
                    visited[g] = True
                    q.append(g)

    bfs(r)
    print(' '.join(map(str, order)))

if __name__ == "__main__":
    main()