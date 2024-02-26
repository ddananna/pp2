import re

# 1
pattern1 = re.compile(r'ab*')

# 2
pattern2 = re.compile(r'ab{2,3}')

# 3
pattern3 = re.compile(r'[a-z]+_[a-z]+')

# 4
pattern4 = re.compile(r'[A-Z][a-z]+')

# 5
pattern5 = re.compile(r'a.*b$')

# 6
pattern6 = re.compile(r'[ ,.]+')

# 7
pattern7 = re.compile(r'(?<!^)(?=[A-Z])')

# 8
pattern8 = re.compile(r'(?<!^)(?=[A-Z])')

# 9
pattern9 = re.compile(r'(?<!^)(?=[A-Z])')
