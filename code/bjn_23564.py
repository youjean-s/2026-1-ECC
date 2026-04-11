import sys
input = sys.stdin.readline

def decompose(t):
    """t를 X_i 구조로 분해하여 (S, A_list) 반환"""
    L = len(t)
    if L == 0:
        return ("", [])
    
    # t = X s X s ... s X (X가 a+1번, s가 a번)
    # lx = len(X), ls = len(s), a >= 1
    for lx in range(0, L):
        for ls in range(1, L - lx + 1):
            if (L - lx) % (lx + ls) != 0:
                continue
            a = (L - lx) // (lx + ls)
            if a < 1:
                continue
            
            X_cand = t[:lx]
            s_cand = t[lx:lx + ls]
            
            # 구조 검증
            valid = True
            for i in range(a):
                pos_s = lx + i * (lx + ls)
                if t[pos_s:pos_s + ls] != s_cand:
                    valid = False
                    break
                pos_x = pos_s + ls
                if t[pos_x:pos_x + lx] != X_cand:
                    valid = False
                    break
            
            if valid:
                sub = decompose(X_cand)
                if sub is not None:
                    S_sub, A_sub = sub
                    if S_sub == "":
                        return (s_cand, [a])
                    else:
                        return (S_sub, A_sub + [a])
    
    return None

def solve():
    T = input().strip()
    result = decompose(T)
    if result:
        S, A = result
        print(S)
        print(*A)

solve()