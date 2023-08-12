#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # #
# Create Time: 2023/8/1215:26
# Fang YJ
# Real-Time Systems Group
# Hunan University HNU
# # # # # # # # # # # # # # # #
# 规则，各枪手向当前存活的枪手开枪，最厉害的枪手先开枪然后从强向弱轮换
import copy
import random

def Gunner_game(Game_num, Gunner_num=3):
    # Gunner_id , hit_rate
    # Gunner_dict = {Gunner_id:{'hit_rate':} for Gunner_id in range(Gunner_num) }
    max_hit_rate = 0.9
    min_hit_rate = 0.1
    hitrate_interval = (max_hit_rate - min_hit_rate)/(Gunner_num + 1)
    Gunner_list = [(Gunner_id, max_hit_rate - hitrate_interval * (Gunner_id + 1)) for Gunner_id in range(Gunner_num)]
    # Gunner_list = [(0,0.5),(1,0.3),(2,0.2)]
    ret = []
    for exma_num in range(Game_num):
        # print(f'############################################################')
        losser_list = []
        winer = None
        while len(Gunner_list) - len(losser_list) > 1:
            for Gunner_id, Hit_rate in Gunner_list:
                if (Gunner_id, Hit_rate) in losser_list:
                    continue
                # print(f'#(1)# I am the Gunner_{Gunner_id}, my Hit rate is:{Hit_rate}')
                Gunner_list_x = copy.deepcopy(Gunner_list)
                Gunner_list_x.remove((Gunner_id, Hit_rate))
                for losser_x in losser_list:
                    Gunner_list_x.remove(losser_x)
                Gunner_list_x.sort(key=lambda x: x[1], reverse=True)
                Gunner_target = Gunner_list_x.pop(0)
                # print(f'#(2)# my target is Gunner_{Gunner_target[0]}, his Hit rate is:{Gunner_target[1]}')
                if random.random() <= Hit_rate:
                    # print(f'#(3)# I kill the Gunner_{Gunner_target[0]}, his Hit rate is:{Gunner_target[1]}')
                    losser_list.append(Gunner_target)
                    if len(Gunner_list) - len(losser_list) == 1:
                        winer = (Gunner_id, Hit_rate)
                        break
                else:
                    # print(f'#(3)# I failed kill the Gunner_{Gunner_target[0]}, his Hit rate is:{Gunner_target[1]}')
                    pass
        # print(f'exam_num:{exma_num}_the winner is {winer[0]}, his hit rate is {winer[1]}')
        ret.append(winer[0])

    for Gunner_id, Hit_rate in Gunner_list:
        winnum = len([retx for retx in ret if retx == Gunner_id])
        print(f'Guner_{Gunner_id};hit_rate is:{Hit_rate}; win_num is :{winnum};win rate:{winnum/Game_num}')


if __name__ == "__main__":
     Gunner_game(100000)    # 100 000 4s