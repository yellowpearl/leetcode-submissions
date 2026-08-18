class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Лид нули
        # Больше 255
        # Бектрекинг, иду по индексам и выбираю поставить ли мне точку в каждой позиции, если от предыдущего индекса есть лид нули или число больше 255 то останавливаюсь, если дошел до конца, то добавляю в результат, отсекаю до рекурсии числа, перебираю индексы начиная с текущего + 1 до конца строки
        # O(4**n) по памяти O(n) для ответа
        res = []
        curr = []
        def bt(start, dots):
            if start == len(s) and dots == 0:
                res.append('.'.join(curr))

            for i in range(start+1, len(s)+1):
                if (
                    int(s[start:i]) > 255
                ) or (
                    s[start:i].startswith('0') and len(s[start:i]) > 1
                ):
                    break
                if dots == 1 and i < len(s):
                    continue
                
                curr.append(s[start:i])
                bt(i, dots-1)
                curr.pop()
        
        bt(0, 4)
        return res
        