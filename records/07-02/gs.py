__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '7/2/2020 10:27 AM'


# 把自己带入 非成勿扰 录制现场
def gs_matching(man_preferences, woman_preferences):
    length = len(man_preferences)
    is_man_dated = [False] * length  # 10位男嘉宾是否已经撩到妹妹了
    is_woman_dated = [False] * length  # 10位美人是否已经名花有主
    result = [-1] * length

    while False in is_man_dated:
        new_man = is_man_dated.index(False)
        girls_he_likes = man_preferences[new_man]  # 康康这个男生最喜欢谁
        for girl in girls_he_likes:
            # 查看女生是否已经被约
            if is_woman_dated[girl] is False:  # 发现没有，那就当场拿下
                result[new_man] = girl
                is_woman_dated[girl] = True
                is_man_dated[new_man] = True
                break  # 换下一个男嘉宾登场，进行选择
            else:
                # 女嘉宾已经心有所属，现在进入权利反转环节， 女生对两位男嘉宾进行挑选
                current_boyfriend = result.index(girl)
                if woman_preferences[girl].index(current_boyfriend) > woman_preferences[girl].index(new_man):
                    # 看看是不是更喜欢 新来的这个小鲜肉，如果是，果断甩掉之前的蓝朋友
                    is_man_dated[current_boyfriend] = False
                    result[current_boyfriend] = -1
                    is_man_dated[new_man] = True
                    result[new_man] = girl
                    break  # 换下一个男嘉宾登场，进行选择
    print(result)


if __name__ == '__main__':
    MP = [[1, 4, 3, 6, 2, 5, 8, 7, 9, 0],
          [2, 1, 0, 3, 4, 8, 5, 9, 7, 6],
          [4, 3, 8, 9, 0, 2, 1, 7, 6, 5],
          [2, 7, 6, 1, 4, 3, 8, 0, 9, 5],
          [5, 3, 8, 4, 2, 0, 7, 6, 1, 9],
          [5, 0, 1, 7, 2, 8, 9, 4, 6, 3],
          [6, 2, 9, 8, 0, 7, 5, 1, 4, 3],
          [9, 7, 1, 8, 0, 2, 5, 6, 3, 4],
          [8, 0, 5, 9, 6, 7, 1, 2, 4, 3],
          [7, 9, 1, 6, 2, 0, 5, 8, 4, 3]]

    WP = [[3, 5, 0, 6, 9, 4, 8, 7, 2, 1],
          [0, 1, 3, 2, 7, 8, 5, 9, 4, 6],
          [1, 0, 7, 9, 3, 2, 5, 8, 6, 4],
          [2, 0, 6, 3, 4, 1, 5, 7, 9, 8],
          [5, 6, 8, 3, 2, 0, 9, 4, 1, 7],
          [3, 0, 1, 7, 9, 8, 2, 4, 6, 5],
          [6, 2, 7, 8, 0, 9, 4, 1, 5, 3],
          [9, 3, 1, 2, 0, 7, 5, 6, 8, 4],
          [4, 1, 5, 9, 6, 7, 0, 2, 8, 3],
          [6, 0, 1, 7, 2, 9, 5, 8, 4, 3]]

    gs_matching(MP, WP)