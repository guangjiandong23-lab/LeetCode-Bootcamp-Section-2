def matrix_chain_order(p):
    """
    计算矩阵连乘的最小代价并记录最优分割点
    :param p: 维度列表，p[i]为第i个矩阵的行数，p[i+1]为第i个矩阵的列数
    :return: (m, s)，m是最小代价表，s是最优分割点表
    """
    print("=" * 10)
    print("开始矩阵连乘动态规划计算")
    print("=" * 10)
    
    # 矩阵的数量 = 维度列表长度 - 1（因为p包含n+1个元素对应n个矩阵）
    n = len(p) - 1  
    print(f"\n矩阵数量: {n}")
    print(f"维度列表: {p}")
    
    # 初始化代价表m：m[i][j]表示计算矩阵链A_i到A_j的最小代价
    # 初始化分割点表s：s[i][j]表示矩阵链A_i到A_j的最优分割位置
    # 采用n+1 x n+1的大小，索引从1开始（方便对应矩阵编号1~n）
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    
    print("\n初始化完成，开始按矩阵链长度计算...")
    print("-" * 10)
    
    # 按矩阵链长度递增计算（长度为1时，单个矩阵无需乘法，代价为0，已默认初始化）
    # length表示当前计算的矩阵链长度（从2开始，直到n）
    for length in range(2, n + 1):  
        print(f"\n当前计算矩阵链长度: {length}")
        
        # i表示矩阵链的起始矩阵索引（从1开始）
        # 循环条件确保j = i + length - 1不超过n（矩阵最大索引）
        for i in range(1, n - length + 2):  
            j = i + length - 1  # j表示矩阵链的结束矩阵索引（i + 长度 - 1）
            print(f"\n  处理矩阵链 A{i}~A{j} (i={i}, j={j})")
            
            m[i][j] = float('inf')  # 初始化当前矩阵链的最小代价为无穷大（用于后续比较）
            print(f"    初始化 m[{i}][{j}] = {m[i][j]}")
            
            # 尝试所有可能的分割点k（k在i到j-1之间）
            # 将矩阵链A_i~A_j分割为A_i~A_k和A_{k+1}~A_j两部分
            for k in range(i, j):
                print(f"\n    尝试分割点 k={k}")
                print(f"      左子链: A{i}~A{k}, 右子链: A{k+1}~A{j}")
                
                # 计算当前分割方式的总代价：
                # 左子链代价（A_i~A_k） + 右子链代价（A_{k+1}~A_j） + 合并两子链的代价
                # 合并代价公式：左子链行数 × 左子链列数（=右子链行数） × 右子链列数
                # 对应维度：p[i-1]（A_i行数） × p[k]（A_k列数） × p[j]（A_j列数）
                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
                
                print(f"      计算代价: m[{i}][{k}] ({m[i][k]}) + m[{k+1}][{j}] ({m[k+1][j]}) + {p[i-1]}×{p[k]}×{p[j]} ({p[i-1]*p[k]*p[j]}) = {cost}")
                
                # 如果当前分割的代价更小，更新最小代价和最优分割点
                if cost < m[i][j]:
                    print(f"      发现更优解！更新 m[{i}][{j}] 从 {m[i][j]} 到 {cost}")
                    print(f"      更新最优分割点 s[{i}][{j}] = {k}")
                    m[i][j] = cost  # 更新最小代价
                    s[i][j] = k     # 记录当前最优分割点k
                    print(f"这是{s[i][j]}")

                else:
                    print(f"      当前代价 {cost} 不优于当前最小值 {m[i][j]}，不更新")
        
        print(f"\n长度为 {length} 的矩阵链计算完成")
        print("-" * 40)
    
    print("\n" + "=" * 60)
    print("矩阵连乘动态规划计算完成")
    print("=" * 60)
    
    # 打印最终的m和s表格
    print("\n最终代价表 m:")
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            if m[i][j] == float('inf'):
                row.append("inf")
            else:
                row.append(str(m[i][j]))
        print(f"  行 {i}: {' '.join(['%4s' % x for x in row])}")
    
    print("\n最优分割点表 s:")
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(str(s[i][j]))
        print(f"  行 {i}: {' '.join(['%4s' % x for x in row])}")
    
    return m, s  # 返回代价表和分割点表


def print_optimal_order(s, i, j):
    """
    回溯最优分割点表，打印最优乘法顺序
    :param s: 最优分割点表
    :param i: 起始矩阵索引
    :param j: 结束矩阵索引
    :return: 最优顺序的字符串
    """
    # 递归终止条件：如果起始和结束索引相同（只有一个矩阵），直接返回矩阵编号
    if i == j:
        return f"A{i}"
    else:
        # 递归处理左子链：从i到最优分割点s[i][j]
        left = print_optimal_order(s, i, s[i][j])
        # 递归处理右子链：从s[i][j]+1到j
        right = print_optimal_order(s, s[i][j]+1, j)
        # 拼接左右子链，用括号表示当前层次的乘法顺序
        return f"({left}{right})"


# 示例用法（当模块直接运行时执行）
if __name__ == "__main__":
    # 示例1：3个矩阵，维度分别为3×2, 2×5, 5×3
    # p1列表含义：p1[0]=3（A1行数）, p1[1]=2（A1列数=A2行数）, p1[2]=5（A2列数=A3行数）, p1[3]=3（A3列数）
    p1 = [3, 2, 5, 3,6,7]
    print("=" * 80)
    print("示例1：3个矩阵")
    print("=" * 80)
    m1, s1 = matrix_chain_order(p1)  # 计算代价表和分割点表
    print(f"\n最终结果：")
    print(f"最小代价：{m1[1][5]}")  # 输出A1~A3的最小代价（预期48）
    print(f"最优顺序：{print_optimal_order(s1, 1, 5)}")  # 输出最优乘法顺序（预期(A1(A2A3))）
    
    # 示例2：4个矩阵，维度分别为2×3, 3×4, 4×5, 5×2
    # p2 = [2, 3, 4, 5, 2]
    # print("\n" + "=" * 80)
    # print("示例2：4个矩阵")
    # print("=" * 80)
    # m2, s2 = matrix_chain_order(p2)
    # print(f"\n最终结果：")
    # print(f"最小代价：{m2[1][4]}")  # 输出A1~A4的最小代价（预期124）
    # print(f"最优顺序：{print_optimal_order(s2, 1, 4)}")  # 输出最优乘法顺序（预期((A1A2)(A3A4))）