class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        answer = ""
        num = min(len(str1), len(str2))
        if len(str1) == num:
            end = str1
        else:
            end = str2

        for i in range(1, num + 1):
            re = end[:i]
            n = 1
            result = []

            while len(re * n) <= len(str1) or len(re * n) <= len(str2):
                if re * n == str1:
                    result.append(re)
                
                if re * n == str2:
                    result.append(re)

                n += 1
            
                if len(result) == 2:
                    if result[0] == result[1]:
                        answer = result[0]
                        break

        return answer