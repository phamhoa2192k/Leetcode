class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_in_s = []
        pos_vowel_in_s = []
        s = [i for i in s]

        for i, char in enumerate(s):
            if char in vowel:
                vowel_in_s.append(char)
                pos_vowel_in_s.append(i)

        vowel_in_s.sort()
        for i, position in enumerate(pos_vowel_in_s):
            s[position] = vowel_in_s[i]

        return "".join(s)


print(Solution().sortVowels("lEetcOde"))
