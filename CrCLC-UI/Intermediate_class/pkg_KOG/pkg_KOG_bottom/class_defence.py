# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23
# Description:
#   攻击类道具
# ------------------------(max to 80 columns)-----------------------------------


# 引用自定义的类及功能包
from pkg_KOG_bottom.class_equipment import Equipment

class EQDefence(Equipment):
    # 添加独有加成
    armor = 0.0
    magical_spells = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +护甲:%0.2f' % (self.armor))
        print('     +魔法抗性:%0.2f' % (self.magical_spells))
        print('-----------------')
        return
