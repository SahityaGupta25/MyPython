from datetime import date, datetime
dt=datetime.today()
print(dt)

# %d= Shows Date
# %m= show Month
# %y= shows year like this 22
# %Y= shows full year like 2022
d1=dt.strftime("%d--%m--%y")
print(d1)

# %H= 24 Hours Format
# %I= 12 Hours Format
# %M= For Minutes
# %S= For Seconds
d2=dt.strftime("Date==%d::%m::%y and Time==%I::%M::%S")
print(d2)

# %B= To show Full name of August
# %b= To show short name of month

d3=dt.strftime("Date =%d--%b--%y")
print(d3)