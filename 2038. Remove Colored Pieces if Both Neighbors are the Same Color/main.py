class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        last_char = colors[0]
        num_of_last_char = 1
        alice, bob= 0, 0
        for char in colors[1:]:
            if char == last_char:
                num_of_last_char += 1
                if num_of_last_char > 2:
                    if char == 'A':
                        alice += 1
                    else:
                        bob += 1
            else:
                num_of_last_char = 1
                last_char = char
        if alice > bob: 
            return True
        else:
            return False

tc = "AA"
print(Solution().winnerOfGame(tc))