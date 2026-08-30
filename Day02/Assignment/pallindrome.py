def pallindrome():
    s = input()
    longest = ""

    for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right<len(s):
            if s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]

                left -= 1
                right += 1
            else:
                break

        left = i
        right = i+1

        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if right - left + 1 > len(longest):
                    longest = s[left:right+1]

                left -= 1
                right += 1
            else:
                break

    print(longest)

def main():
    pallindrome()

main()
           