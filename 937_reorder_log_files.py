# https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        letter = []
        count = 0
        for log in logs:
            for string in log:
                if string == " ":
                    idx = log.index(string)
                    break
            identifier = log[:idx]
            rest = log[idx:]
            rest_check = ''.join(rest.split())
   
            if rest_check.isdigit():
                digit.append(identifier+rest)
            else:
                letter.append([identifier, rest])
                count += 1

        sorted_letter = sorted(letter, key=lambda x: (x[1], x[0]))
        letter = [sorted_letter[i][0]+sorted_letter[i][1] for i in range(count)]

        return [*letter, *digit]