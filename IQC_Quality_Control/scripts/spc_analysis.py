import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. 加载数据
df = pd.read_csv('../data/defects.csv')
phase1 = df.iloc[:224]  # 前 224 个样本
phase2 = df.iloc[224:]  # 后 96 个样本

# 2. 统计检验 (Anderson-Darling Test)
result = stats.anderson(df['Defects'], dist='norm')
print(f"Anderson-Darling Statistic: {result.statistic:.4f}")

# 3. C-Chart 计算 (基于 Phase I)
c_bar = phase1['Defects'].mean()
ucl = c_bar + 3 * np.sqrt(c_bar)
lcl = max(0, c_bar - 3 * np.sqrt(c_bar))
print(f"Phase I Center Line (C): {c_bar:.2f}, UCL: {ucl:.2f}, LCL: {lcl:.2f}")

# 4. 过程能力分析 (Process Capability)
# 定义规格限 (根据海报: USL=25, LSL=0)
usl, lsl = 25, 0

def calculate_cpk(data, usl, lsl):
    mu = data.mean()
    sigma = data.std()
    cpu = (usl - mu) / (3 * sigma)
    cpl = (mu - lsl) / (3 * sigma)
    return min(cpu, cpl)

cpk_p1 = calculate_cpk(phase1['Defects'], usl, lsl)
cpk_p2 = calculate_cpk(phase2['Defects'], usl, lsl)

print(f"Phase I Cpk: {cpk_p1:.2f}")
print(f"Phase II Cpk: {cpk_p2:.2f}")

# 5. 可视化输出 (可选，用于对比 Minitab)
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['Defects'], marker='o', linestyle='-', markersize=4)
plt.axhline(c_bar, color='red', linestyle='--', label='CL')
plt.axhline(ucl, color='orange', linestyle='--', label='UCL')
plt.axhline(lcl, color='orange', linestyle='--', label='LCL')
plt.title("C-Chart of Parts Defects (Replicated)")
plt.xlabel("Sample Index")
plt.ylabel("Defect Count")
plt.legend()
plt.savefig('../figures/python_replicated_chart.png')