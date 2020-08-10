__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '8/8/2020 4:24 PM'


class Solution:
    def ladderLength(self, beginWord, endWord, wordList) -> int:

        if beginWord in wordList:
            wordList.remove(beginWord)

        queue = [beginWord]

        word_length = len(beginWord)

        visited = set()
        visited.add(beginWord)
        ans = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                word = queue.pop(0)
                word_c_list = [c for c in list(word)]

                for i in range(word_length):
                    original_c = word_c_list[i]

                    for k in range(26):
                        replaced_c = chr(ord('a') + k)
                        if replaced_c != original_c:
                            word_c_list[i] = replaced_c
                        else:
                            continue
                        new_str = ''.join(word_c_list)
                        if new_str in wordList:
                            if new_str == endWord:
                                return ans + 1

                            if new_str not in visited:
                                queue.append(new_str)
                                visited.add(new_str)
                    word_c_list[i] = original_c
            ans += 1
        return 0


beginWord = "a"
endWord = "c"
wordList = ["a", "b", "c"]

ss = Solution().ladderLength(beginWord, endWord, wordList)
print(ss)
