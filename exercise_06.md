# 摘要
  考虑海拔高度的影响，使用绝热模型进行计算，误差描述使用最简单的均匀分布描述（也就是在误差范围内每个取值概率是一样的）
# 背景介绍
  L1 2.10题强化版（引入迎面风阻）
# 正文
  已知目标高度求初始速度，有两种情况：炮弹上升过程中击中目标；炮弹下落的过程中击中目标。可以计算，当发射速度大小一定时，炮弹发射速度与水平方向成45°斜向
  上时，发射的距离最远，所以为了缩小发射的角度范围，可以在45°附近考虑（25°~65°）。以炮弹为原点，目标水平方向坐标为循环停止，对角度进行扫描。
  代码：https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/6%E4%BB%A3%E7%A0%81.py
# 结论
  利用上述代码可以在目标高度一定时，无限逼近求得最小发射速度
# 致谢
  感觉狄福明，段俊磊，周璟怡的帮助
