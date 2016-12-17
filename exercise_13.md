# 背景
  6.12   波的运动满足波动方程
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/%E6%B3%A2%E5%8A%A8%E6%96%B9%E7%A8%8B.png
  式中y为弦上各点相对平衡位置的位移，x为各点在弦上的坐标，t为时间，c为波在弦上的传播速度
# 正文
  初始时刻，在弦上施加干扰Y（X）=exp[-k（X-x）（X-x） ]，选取弦长1m，c=300m/s
  接下来讨论弦上波的power spectrum，当在弦的中心加上上述干扰后，距x=0处弦长5%的点的振动随时间的变化情况为
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/5.png
  其power spectrum图为https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/power%20spectrum.png
  代码:https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/12%E4%BB%A3%E7%A0%811.py
  现在考虑初始波形为三角波时的power spectrum，当三角形的上顶角为弦的中心时，信号为
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/1.png
  频谱为
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/2.png
  其代码为https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/13%E4%BB%A3%E7%A0%81.py
  当上顶角偏离弦中心时，信号为
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/3.png
  频谱为
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/4.png
# 结论
  power spectrum上当频率为150Hz的奇数倍时有峰值；初始时刻三角波的顶角位于弦中心时，频率谱上有几个峰值，随着频率的增大，峰值在减小；当顶角偏离弦中心时，由于初始波形失去了对称性，频谱上峰增多了。
# 致谢
  感谢许亚伦同学
