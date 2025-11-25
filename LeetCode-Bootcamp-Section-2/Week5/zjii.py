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

    for length in range(2,n+1):

        for i in range(1,n-length+2):
            j = i+length-1
            m[i][j] = float('inf') 

            for k in range(i,j):
                print(f"\n    尝试分割点k={k}")

                cost = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]

                if cost<m[i][j]:

                    m[i][j] = cost
                    s[i][j] = k
    # 必须添加return语句
    return m, s

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
        print(f"这个A{i}")
        return f"A{i}"
        
    else:
        # 递归处理左子链：从i到最优分割点s[i][j]
        left = print_optimal_order(s, i, s[i][j])
        # 递归处理右子链：从s[i][j]+1到j
        right = print_optimal_order(s, s[i][j]+1, j)
        # 拼接左右子链，用括号表示当前层次的乘法顺序
        result = f"({left}{right})"
        print(f"合并结果：{result}")
        return result


if __name__ == "__main__":
    p1 = [3, 2, 5, 3, 6, 7]
    m1, s1 = matrix_chain_order(p1)
    
    print("\n" + "=" * 60)
    print("计算完成！")
    print("=" * 60)
    
    # 打印最小代价
    print(f"\n最小代价: {m1[1][len(p1)-1]}")
    
    # 打印最优乘法顺序（带括号版）
    optimal_order = print_optimal_order(s1, 1, len(p1)-1)
    print(f"最优乘法顺序: {optimal_order}")

    
    