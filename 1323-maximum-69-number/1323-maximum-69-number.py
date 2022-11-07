class Solution:
    def maximum69Number (self, num: int) -> int:
        to_list = []
        while num > 0:
            to_list.append(str(num % 10))
            num = num // 10
        to_list.reverse()
        for i in range(len(to_list)):
            if to_list[i] == '6':
                to_list[i] = '9'
                break
        return int("".join(to_list))