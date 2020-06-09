# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.8.10

# Description:
#   编制行星数据分析 （主程序）
# ------------------------(max to 80 columns)-----------------------------------
  from func_planet.py improt cal_g,cal_v,cal_Ve,Cal_P

  planet1=(4878,3.02e+23)
  M=planet1[1]
  r=planet1[0]/2
  p1_v=cal_v(r)
  print(p1_v)

  p1_p=Cal_P(M,r)
  p1_g=cal_g(M,r)
  p1_ve=cal_Ve(M,r)
  print(p1_p)
  print(p1_g)
  print(p1_ve)
