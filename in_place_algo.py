    def reverseString(s: List[str]) -> None:
        for i in range(0,math.floor((len(s))/2)):
            tmp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = tmp
         return s
