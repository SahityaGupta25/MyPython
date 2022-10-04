# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}
# ======================================================================================

thisset={"Python","Java","Django"}
s1={e for e in thisset if e in "Python"}
print(s1)