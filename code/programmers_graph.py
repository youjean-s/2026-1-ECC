def solution(n, results):
    # win[i][j] = i가 j를 이길 수 있는가
    win = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 직접 경기 결과 입력
    for a, b in results:
        win[a][b] = True
    
    # 플로이드-워셜: 간접 승패 결과 추론
    for k in range(1, n + 1):        # 중간 선수
        for i in range(1, n + 1):    # 출발
            for j in range(1, n + 1):# 도착
                # i가 k를 이기고, k가 j를 이기면 → i가 j도 이김
                if win[i][k] and win[k][j]:
                    win[i][j] = True
    
    # 순위 확정: 나를 제외한 n-1명 모두와 관계가 있어야 함
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if i == j:
                continue
            # i가 j를 이기거나, j가 i를 이기면 관계 확정
            if win[i][j] or win[j][i]:
                count += 1
        if count == n - 1:
            answer += 1
    
    return answer