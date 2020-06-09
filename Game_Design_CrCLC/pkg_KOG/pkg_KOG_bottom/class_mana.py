# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.23
# Description:
#   攻击类道具
# ------------------------(max to 80 columns)-----------------------------------


# 引用自定义的类及功能包
from pkg_KOG_bottom.class_equipment import Equipment


class EQMana(Equipment):
    # 添加独有加成
    restore_mana_power = 0.0
    mana_strength = 0.0
    mana_power = 0.0

    def show_me_unique(self):
        print('-----独有加成-----')
        print('       +法力恢复:%0.2f' % (self.restore_mana_power))
        print('     +法术强度:%0.2f' % (self.mana_strength))
        print('     +法力值:%0.2f' % (self.mana_power))
        print('-----------------')
        return
