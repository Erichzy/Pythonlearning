import random
# 假设现在有n/2必须是偶数,否则晋级赛会出现落单球队
teams = ['中国队', '美国队', '法国队', '日本队', '韩国队', '俄罗斯队', '乌克兰队', '德国队']
order = []
n = 1
def vs(teams, order):
    # n += 1
    # 打乱球队顺序
    random.shuffle(teams)
    # 获取球队比赛场次
    scene = int(len(teams)/2)
    # 获取主球队
    home_team_list = teams[0:scene]
    # 获取客队
    guest_teams_list = teams[scene:]
    # 将主客队两两组合
    vsteam = list(zip(home_team_list, guest_teams_list))
    # 开始比赛

    for t in vsteam:
        # 主队得分
        h_code = random.randint(0, 10)
        # 客队得分
        g_code = random.randint(0, 10)
        order.append([(t[0], h_code),(t[1], g_code)])
    print('-----------------------------------第{0}轮比赛结果-----------------------------------'.format(n))

    print('晋级球队:{0}'.format(order))
    winner = []
    for o in order:
        if o[0][1] > o[1][1]:
            winner.append(o[0][0])

        else:
            winner.append(o[1][0])
    order=[]

    if (len(winner) > 1):
        print('胜者:{0}'.format(winner))
        vs(winner, order)
    else:
        print("冠军:{0}".format(winner))
vs(teams, order)