# Remove in public
from utils.utilities import color, colourprint, wait, clear

art2 = """@@@@@@@@@@@@@@@@@@@@@@@@@%###%%%#%%%%%@@@@@@@@@@@@@@@@@@+++=::::::::::::::::::::::::::::::::::::::-+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@%###%%%%%%%#%@@@@@@@@@@@@@@@@@#+-:::::::::::::::::::::::::::::::::::::::::-=+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@####%#%%@%##%@@@@@@@@@@@@@@%*-::::::::::::::::::::::::::::::::::::::::::::-=+*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@%####%#%@%####@@@@@@@@@@@%+:::::::::::::::::::::::::::::::::::::::::::::::-=+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@#######%@%###%@@@@@@@@@*:::::::::::::::::::::::::::::::::::::::::::::::::-+**#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@%#######%@@@@@@@@@@@@%=:::::::::::::::::::::::::::::::::::::::::::::::::::-+#*#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@########@@@@@@@@@@@#-:::::::::::::::::::::::::::::::::::::::::::::::::::::-+*++*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*****%@@@@@@@@@@@+::::::::::::::::::::::::::::::::::::::::::::::::::::::::-==+*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@%@@@@@@@@@@@@@@@@%***#%%@@@@@@@@@@#=::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-=+%@@@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@%##%@@#@@@@@@@@@%=::::::::::::::::::::::::::::::::::::::::::::::-====-::::::::::-=*%@@@@@@@@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@%=:::::::::::::::::::::::::::::::::::::::::::-========--:::::::::-=*%@@@@@%#@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@%=::::::::::::::::::::::::::::::::::::::::::-+=+*%%%%@%%*=:::::::::-+%@@@@@#%@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=:::::::::::::::::::::::::::::::::::::::::-=+#@@@%##%@@@%+:::::::::-=#@@@@%#%%@@@@@@@@@@@@@@#
@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-:::::::::::::::::::::::::::::::::::::::::-=%@%=::-:::+%@#-:::::::::-=*@@@@%%%@@@@@@@@@@@@@@#
@@@@@@@@@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#::::::::::-=======--::::::::::::::::::::::-*%%=::+@@+::*%#-::::::::::-+*@@@%%@@@@@@@@@@@@@@@#
@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*::::::::-==*#%%%%%#*=-:::::::::::::::::::::+%%+:::=+-:-*#+::::::::::::=+#@@@%@@@@@@@@@@@@@@@#
@@@@@@@@@@@%%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:::::::=++*%@@#+==+**=-::::::::::::::::::::-#%%#+====+**=::::::::::::::=*%@@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=:::::-==*%@%=:-*+::=+-:::::::::::::::::::::-+#%%%##*+=-::::::::::::::::=*%@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+:::::-==#@@#-:+@%-:+*=::::::::::::::::::::::--====--:::::::::::::::::::-+#@@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#::::::--*@@@*-:::-+#*=:::::::::::::::::::::-------::::::::::::::::::::::-+%@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%::::::::-+%@@@@@%%##+--::::::::::::::::::::-------::::::::::::::::::::::-=#@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%:::::::::-=*#%%##*+=----:::::::::::::::::::::---:::::::::::::::::::::::::=*@@@@@@@@@@@@@@@@#
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#:::::::::::-------------:::::::::::::::::::::::::::::::::::::::::::::::::-+%@@@@@@@@@@@*=*#*
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+::::::::::::::::::-----::::::::::::::::::::::::::::::::::::::::::::::::::-+#@@@@@@@@@@%+=--:
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-=+%@@@@@@@@@@+-:::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::--=*%@@@@@@@@@+::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::--+#@@@@@@@@@+::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::--=*@@@@@@@@@*::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-==-::::::::-+@@@@@@@@@*::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::=+#*=::::::::::=%@@@@@@@@#::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*-::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-+*##*+-::::::::::=%@@@@@@@@#-:::
@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@+::::::::::::::::::::::::::::::::::::::::::::::::::::::::=+#%%#*+-::::::::::-+%@@@@@@@@#-:::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=::::::::::::::::::::::::::::::::::::::::::::::::::::-+*#%%##*+-:::::::::::-+@@@@@@@@@%-:::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=::::::::::-==-:::::::::::::::::::::::::::::::::::-+*######*=-:::::::::::-=#@@@@@@@@@#-:::
@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+-::::::::-=+++=-:::::::::::::::::::::::::::::-==++*####*+=:::::::::::::-+@@@@@@@@@@#-:::
@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-::::::::-=+**#*=:::::::::::::::::-==------==-:=*#%%##+-:::::::::::::-+%@@@@@@@@@#+::::
@@@@@@@@@@@@@@@@%%%%%@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@*=:::::::::-=+*###*=-:::-==------:::::::::::::-+#%##*+-:::::::::::::-=#@@@@@@@@@@#=::::
@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=:::::::::-=+*#####**+=-::::::::::::::::::=+*###**+=::::::::::::--=*@@@@@@@@@@@#=::::
@@@@@@@@@@@@@@@%%%%%####%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%+-::::::::-+**####+-:--::-::::::::::::--=+####**+=-:::::::::::-==*%@@@@@@@@@@@*-::::
@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#+-:::::::-=+**###+-:::::::::::::::::=++******+=--:::::::::--=+*%@@@@@@@@@@@@+=::::
@@@@@@@@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@%*+--:::::-=+**###*-:::::::::----::-=+=-+#*++=--:::::::::-==+*#@@@@@%@@@@@@%+-::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@##+==-:::::-=+*###*=+***==+++++=------=#**+==--::-:::::-=++*#@@@@%++%@@@@%*=-::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#%@@*#@@*=*#*=-::::::=+*###+--=+=----:::::::=##**#+===----:::--=+*##@@@@%+-+*#@@@@+=-::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=*@@%+@@#-:-##*=-:--::-+*#%%%*-::::::::::=*##**###++*+====-:-=+*##%@@@@@*-=*+#@@@@+=-::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+==#@@#%@@+:::-*#*+===-:-=*#%%%%%%####%%%#****##%#*##*==--::-=*#%@@@@@@@#--+*=*@@%%=-:::::
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#**#@@@@@@@@@@@@@@@@+=-+%@%#@@*:::::-*%#***+--+##%%%%##**####***##%%##%%#+=-----=*@@@@@@@@@%=---+=*%%##=-:::::
@@@@@@@@@@@@@@@@@@@@@@@@@@%+-::::::-=+*%@@@@@@@@@*====#%%*%@#-::::::-*@@@%*==+#%%%%%%###%%%##%%%%%%@%#*==---==*%@@@@@@@@%+----=+*#*#+=-----:"""

def test10():
  clear()
  wait(0.5)
  colourprint(f"{color.RED}" + art2 + f"{color.END}")
  wait(0.2)
  clear()
  return