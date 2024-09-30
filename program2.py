def decode_message( s: str, p: str) -> bool:

        m, p = len(message), len(pattern)
        
        dp = [[False] * (m + 1) for _ in range(p + 1)]
        
        # Base case: empty pattern matches empty message
        dp[0][0] = True
        
        for i in range(1, p + 1):
                if pattern[i - 1] == '*':
                dp[i][0] = dp[i - 1][0]
        
        for i in range(1, p + 1):

                for j in range(1, m + 1):

                if pattern[i - 1] == '*':
                        # '*' can match zero or more characters
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

                elif pattern[i - 1] == '?' or pattern[i - 1] == message[j - 1]:
                        # '?' matches any single character or exact match of current character
                        dp[i][j] = dp[i - 1][j - 1]
        
        # The answer is whether the entire pattern matches the entire message
        return dp[p][m]
