class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        total_length = len(s)
        vowels = []
        for i in range(total_length):
            if s[i] in 'AEIOUaeiou':
                vowels.append(i)
        vowel_length = len(vowels)

        for i in range(vowel_length//2):
            s[vowels[i]], s[vowels[vowel_length-1-i]] = s[vowels[vowel_length-1-i]], s[vowels[i]]

        s = ''.join(s)
        return s