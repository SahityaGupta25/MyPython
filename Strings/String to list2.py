# Converting from string to list also adding while Converting adding only integer values.
# =========================================================================================


x="1j2h3g4f5d6a"
print(sum([int(e) for e in x if ord(e)>=49 and ord(e)<=57]))