def decode_message(message: str, pattern: str) -> bool:

    # Get lengths of the message and the pattern
    message_len = len(message)
    pattern_len = len(pattern)
    
    # Create a 2D table (dp array) initialized with False values
    dp = [[False] * (message_len + 1) for _ in range(pattern_len + 1)]
    
    # Base case
    dp[0][0] = True
    
    # Handle patterns that start with one or more '*' symbols
    for i in range(1, pattern_len + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]
    
    for i in range(1, pattern_len + 1):
        for j in range(1, message_len + 1):
            # If the current pattern character is '*', it can either:
            # - Ignore the current message character and move on (dp[i-1][j])
            # - Match the current message character and continue (dp[i][j-1])
            
            if pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            # If the current pattern character is '?' or matches the message character exactly,
            # the result depends on whether the previous part of the pattern and message match (dp[i-1][j-1])
            elif pattern[i - 1] == '?' or pattern[i - 1] == message[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    
    # The answer lies in whether the entire pattern matches the entire message
    return dp[pattern_len][message_len]
