import datetime as dt
import time as t


UnixEpoch = dt.datetime(1970, 1, 1)  # set to Unix Epoch time
UEsec = t.time()  # Seconds since 1st Jan 1970 / Unix Epoch time
print(UnixEpoch.strftime
      ("Seconds since %B %-d, %Y:"),
      "{:,.4f}".format(UEsec), "or "
      "{:.2e}".format(UEsec),
      "in scientific notation")

today = dt.datetime.now()  # TODAY
print(today.strftime("%b %-d %Y"))  # TODAY


Seconds = "{:,.4f}".format(t.time())
ScientificNotation = "{:.2e}".format(t.time())
# print("{:,.4f}".format(Seconds))
# format with , & 4 decimal place
# print("{:.2e}".format(ScientificNotation))
# scientific notation format with 2 decimal palace

# $>python format_ft_time.py | cat -e
# Seconds since January 1, 1970: 1,666,355,857.3622
# or 1.67e+09 in scientific notation$
# Oct 21 2022$
# $>
