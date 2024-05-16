from collections import deque
import copy
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    max_v = max(map(max, rectangle))
    graph = make_graph(rectangle, max_v)
    arr = []
    for i in range(4):
        nx = characterX + dx[i]
        ny = characterY + dy[i]
        if 0 <= nx < max_v and 0 <= ny < max_v and graph[nx][ny] == 1:
            arr.append((nx, ny))
    for x, y in arr:
        cnt = bfs(graph, x*2, y*2, max_v, itemX * 2, itemY * 2)
        answer = max(answer, cnt)
    print(answer)
    return answer


def make_graph(arr, max_v):
    graph = [[0 for _ in range(max_v * 2 + 1)] for _ in range(max_v * 2 + 1)]
    for node in arr:
        for i in range(node[0]*2, node[2]*2 + 1):
            for j in range(node[1]*2, node[3]*2 + 1):
                graph[i][j] = 1
    for node in arr:
        for i in range(node[0]*2+1, node[2]*2):
            for j in range(node[1]*2+1, node[3]*2):
                graph[i][j] = 0
    return graph

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y, n, i_X, i_Y):
    queue = deque()
    queue.append((x, y))
    n_graph = copy.deepcopy(graph)
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        if cx == i_X and cy == i_Y:
            return cnt
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n*2 and 0 <= ny < n*2:
                if n_graph[nx][ny] == 1:
                    n_graph[nx][ny] = 0
                    queue.append((nx, ny))
                    print(cnt, nx, ny)
                    cnt += 1
solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
