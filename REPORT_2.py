A = [1, 2, 3, 4, 5]  
def input_matrix():
    print("5x5 관계 행렬을 입력하세요")
    matrix = []
    for i in range(5):
        row = list(map(int, input(f"{i+1}번째 행: ").split()))
        matrix.append(row)
    return matrix

def is_reflexive(R):
    for i in range(5):
        if R[i][i] != 1:
            return False
    return True
def is_symmetric(R):
    for i in range(5):
        for j in range(5):
            if R[i][j] != R[j][i]:
                return False
    return True

def is_transitive(R):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if R[i][k] == 1 and R[k][j] == 1 and R[i][j] == 0:
                    return False
    return True
def equivalence_class(R, x):
    eq = []
    idx = x - 1
    for j in range(5):
        if R[idx][j] == 1:
            eq.append(A[j])
    return eq

def reflexive_closure(R):
    new_R = [row[:] for row in R]
    for i in range(5):
        new_R[i][i] = 1
    return new_R

def symmetric_closure(R):
    new_R = [row[:] for row in R]
    for i in range(5):
        for j in range(5):
            if R[i][j] == 1:
                new_R[j][i] = 1
    return new_R

def transitive_closure(R):
    new_R = [row[:] for row in R]
    for k in range(5):
        for i in range(5):
            for j in range(5):
                if new_R[i][k] == 1 and new_R[k][j] == 1:
                    new_R[i][j] = 1
    return new_R
def main():
    R = input_matrix()

    print("\n=== 관계 성질 체크 ===")
    r = is_reflexive(R)
    s = is_symmetric(R)
    t = is_transitive(R)

    print("반사성:", r)
    print("대칭성:", s)
    print("추이성:", t)

    if r and s and t:
        print("\n이 관계는 동치 관계입니다.\n")
        print("=== 동치류 출력 ===")
        for x in A:
            print(f"[{x}] =", equivalence_class(R, x))
    else:
        print("\n이 관계는 동치 관계가 아닙니다.")
        print("폐포를 만들어서 관계를 완성합니다.\n")

        print("\n--- 반사 폐포 ---")
        R_ref = reflexive_closure(R)
        print(R_ref)

        print("\n--- 대칭 폐포 ---")
        R_sym = symmetric_closure(R)
        print(R_sym)

        print("\n--- 추이 폐포 ---")
        R_tra = transitive_closure(R)
        print(R_tra)

        print("\n--- 모든 폐포 적용 후 ---")
        R_full = transitive_closure(symmetric_closure(reflexive_closure(R)))

        print("최종 관계 행렬:")
        for row in R_full:
            print(row)

        if is_reflexive(R_full) and is_symmetric(R_full) and is_transitive(R_full):
            print("\n최종적으로 동치 관계가 됩니다.\n")
            print("=== 동치류 출력 ===")
            for x in A:
                print(f"[{x}] =", equivalence_class(R_full, x))

main()
