__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/22/2020 11:52 PM'

"""
可 今日 小 主要 参加 殿 选
小主 殿选
"""

while True:
    try:
        raw = input().split()
        true_words = input().split()
        need2process = []
        for word in true_words:
            for c in word:
                if c in raw:
                    target = raw.index(c)
                    need2process.append(target)
                    raw[target] = word
                    break

        print(raw)
    except:
        break