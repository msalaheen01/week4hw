class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dynamicProg = [0]*n
        dynamicProg[0] = 1
        s = 0
        for i in range(delay,n):
            s += dynamicProg[i-delay]
            dynamicProg[i] = s
            if i-forget+1 >= 0:
                s -= dynamicProg[i-forget+1]
        return(sum(dynamicProg[-forget:]))%(10**9+7)