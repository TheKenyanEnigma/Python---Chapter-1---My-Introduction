import datetime
import time

# 1.

# diem1 = datetime.date.today().day
# diem2 = datetime.date.today().month
# diem3 = datetime.date.today().year
# diem = diem1, diem2, diem3


# 2.

# diem = datetime.date.isoformat(datetime.date.today())

# 3.
#
# diem1 = datetime.date.isoformat(datetime.date.today().day)
# diem2 = datetime.date.isoformat(datetime.date.today().month)
# diem3 = datetime.date.isoformat(datetime.date.today().year)
#
# diem = diem1, diem2, diem3

# Failed attempt at reordering the arrangement of the date format prescribed by the isoformat function.

# The following code shall invoke a couple of time functions to test Python's time module.

# The print function is used by any of the code implementations above to display the computed date result.
# print(diem)

# ---------------------------------------------------------------------------------------------------------------------

# 4.
#

# now = time.strftime("%H:%M")

# 5.
#
# now = time.strftime("%A %p")

# 6.
#
now = time.strftime("%A, %H%M %p")

# The print function is used by any of the code implementations above to display the computed time result.
# print(now)

# ----------------------------------------------------------------------------------------------------------------------

# 7.
#
today = time.strftime("%A")
if today == 'Saturdsy':
    print('Woop Woop!!!')
elif today == 'Sunday':
    print('Recharge')
elif today == "Monday":
    print('Vumilia Bro')
else:
    print('!!!GRIND!!!')






