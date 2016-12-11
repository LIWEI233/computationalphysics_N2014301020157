# 摘要
  5.7   用python解决偏微分方程
# 背景
  电势在空间中的分布满足拉普拉斯方程，利用数值算法可以求出该方程的解
# 正文
  Jacobi法：V（i，j）=1/4[v（i+1,j)+v(i-1,j)+v(i,j+1)+v(i,j-1)]
           V（i，j)=αΔV（i，j）+v(i,j)
                  ∴α=2/（1+πL)
             根据以上公式，可编写出python程序:
    https://github.com/LIWEI233/computationalphysics_N2014301020157/commit/5000b294a4640e047fec4016fa0ddad197eec9d8
    https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/12%E4%BB%A3%E7%A0%81.py
    运用该程序可以得到update次数分别为10、100、1000的效果图：
    10：https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/update10.png
    100：https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/update100.png
    1000：https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/update1000.png
    再利用Gauss-Seidel算法与Jacobi法作比较：
    https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/Jacobi%E7%AE%97%E6%B3%95%E4%BB%A3%E7%A0%81.py
# 结论
  从运行程序跟效果图可以看出，Jacobi法update100次与1000次差别不明显，而且1502次update后无法再提高精度，一开始Jacobi法接近速度快，
  当达到一定update次数后Gauss-Seidel算法接近速度快
# 致谢
  感谢段俊磊同学的帮助
