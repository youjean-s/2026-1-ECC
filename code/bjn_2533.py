import sys
from sys import setrecursionlimit
input=sys.stdin.readline
setrecursionlimit(1<<20) #N이 최대 100만


def dfs(v,parent):
    dp[v][1] =1 #자기 자신을 E.A로 선택
    for child in graph[v]:
        if child==parent:
            continue
        dfs(child,v)
        dp[v][0]=dp[v][0]+dp[child][1] #자기 자신이 E.A가 아닐 때, 자식은 무조건 E.A
        dp[v][1]=dp[v][1]+min(dp[child][0],dp[child][1]) #자기 자신이 E.A일 때,자식은 최솟값

N=int(input())
graph=[[]for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

dp=[[0,0] for _ in range(N+1)]
dfs(1,0)
print(min(dp[1][0], dp[1][1]))    
