import os
# Bandit will trigger a RED CROSS for this hardcoded secret
API_KEY = "12345-ABCDE-SECRET-KEY" 

# Bandit will trigger a RED CROSS for this insecure shell command
os.system("rm -rf /")
