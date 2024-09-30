def decode_message( s: str, p: str) -> bool:

        m, n = len(s), len(p)
    
        # Create a 2D dp array with False values
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        dp[0][0] = True
        
        # Handle patterns starting with '*' that can match an empty message
        for i in range(1, n + 1):
                if p[i - 1] == '*':
                   dp[i][0] = dp[i - 1][0]
        
        # Fill the dp table
        for i in range(1, n + 1):
                for j in range(1, m + 1):
                        if p[i - 1] == '*':
                                # '*' can match zero or more characters
                                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                        elif p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                                # '?' matches any single character or exact match of current character
                                dp[i][j] = dp[i - 1][j - 1]
        
        # The answer is whether the entire pattern matches the entire message
        return dp[n][m]
