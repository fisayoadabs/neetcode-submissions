class Solution:
    def climbStairs(self, n: int) -> int:
        hold = {}
        def fib(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in hold:
                return hold[n]
            hold[n] = fib(n-1) + fib(n-2)
            return hold[n]
        return fib(n)
        