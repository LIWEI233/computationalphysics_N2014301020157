# 摘要
  土星有多颗卫星，在此我们研究土星卫星heprion的混沌现象。
# 背景介绍
  1848年美国天文学家邦德(G. Bond)和英国的拉塞尔(W. Lassell)各自独立发现土卫七，距土星1482000公里，像大星体的碎片，表面有如海绵，是目前所发现太阳系中最大的一颗非球形天体，也是太阳系中已知星体中唯一一个自转会混沌的星体，每21.3天绕土星旋转一周。土卫七约21.3天绕土星转一圈。由于土卫七轨道偏心率大(0.03)而受土星和土卫六的引力在变化，造成它的自转周期经常变化，这在太阳系所有卫星中是很特殊的。土卫七大致近似于三轴长360×280×225公里的椭球，质量为800万亿吨。它的形状很不规则，这是严重陨击造成的。它的表面陨击坑累累，最大陨击坑的直径约120公里、深10公里。
  土卫七其表面布满蜂窝状坑体，看起来像是一个巨大的榴莲。
# 正文
  代码https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/11%E4%BB%A3%E7%A0%81.py
  以下均考虑圆和椭圆轨道
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/yuan%2Cw%2Ctheta.png
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/tuo%2Cw%2Ctheta.png
  Δθ和Δw随θ变化的关系
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/yuan%2Cdw%2Cdtheta.png
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/tuo%2Cdw%2Cdtheta.png
  θ从-π到π变化
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/tuo%2Cqudian2pi%2Cdw%2Cdtheta.png
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/yuan%2Cqudian2pi%2Cdw%2Cdtheta.png
  当Δθ=0.05时改变初始速度
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/dt%3D0.05%2C4t.png
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/dt%3D0.04%2C4w.png
  当Δθ=0.01时改变初始速度
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/dt%3D0.01%2C4w.png
  https://github.com/LIWEI233/computationalphysics_N2014301020157/blob/master/dt%3D0.01%2C4t.png
# 结论
  该模型下初始条件对最后结果影响很大，而且因为角速度从负到正在进行大的变化，从而导致下降的幅度不同
# 致谢
  感谢杜威同学的帮助
