"""
    Copyright (C) 2021  Koviubi56

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
    
    To see the source code: https://github.com/koviubi56/countdown
"""
# IDEA: NEW UPDATE (1.0.1) az órának most már van tell-je
import time
import sys


def sec(sec, tell=True):
    """Countdown by one second

    Args:
        sec (int): Time
        tell (bool, optional): Tell the remained time to the user? Defaults to True.
    """
    MYtime = sec
    if MYtime < 0:
        return None
    while MYtime > 0:
        if tell:
            print("Wait " + str(MYtime) + " second(s)!")
        time.sleep(1)
        MYtime -= 1


def min(min, tell=True):
    """Countdown by one minute

    Args:
        min (int): Time
        tell (bool, optional): Tell the remained time to the user? Defaults to True.
    """
    MYtime = min
    if MYtime < 0:
        return None
    while MYtime > 0:
        if tell:
            print("Wait " + str(MYtime) + " minute(s)!")
        time.sleep(60)
        MYtime -= 1


def hour(hour, tell=True):
    """Countdown by one hour

    Args:
        hour (int): Time
        tell (bool, optional): Tell the remained time to the user? Defaults to True.
    """
    MYtime = hour
    if MYtime < 0:
        return None
    while MYtime > 0:
        if tell:
            print("Wait " + str(MYtime) + " hour(s)!")
        time.sleep(3600)
        MYtime -= 1


if __name__ == '__main__':
    while True:
        print("This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.\nTo see the source code: https://github.com/koviubi56/countdown")
        user = input("[S]ec; [M]in; [H]our; or [T]imer>").upper()
        if user == "S":
            user = int(input("Sec>"))
            if user == "__EXIT__":
                sys.exit()
            sec(user)
            print("END")
            for i in range(19):
                print(
                    "*******************************************************************************")
                time.sleep(0.1)
        elif user == "M":
            user = int(input("Min>"))
            if user == "__EXIT__":
                sys.exit()
            min(user)
            print("END")
        elif user == "H":
            user = int(input("Hour>"))
            if user == "__EXIT__":
                sys.exit()
            hour(user)
            print("END")
        elif user == "T":
            # Minimal UI
            user = input("Use minimal user interface [Y/N]>").upper()
            if user == "Y":
                minimalUI = True
            else:
                minimalUI = False

            # The timer
            for i in range(1, 2147483647):
                if minimalUI:
                    # Minimal UI
                    if i / 3600 >= 1:
                        print("\n***\nSec: " + str(i) + "\nMin: " +
                              str(i / 60) + "\nHour: " + str(i / 3600))
                    elif i / 60 >= 1:
                        print("\n***\nSec: " + str(i) +
                              "\nMin: " + str(i / 60))
                    else:
                        print("\n***\nSec: " + str(i))
                    time.sleep(1)
                else:
                    print(
                        "\n\n************\n*SEC_______*\n*MIN_______*\n*HOUR______*\n************")
                    # Standard UI
                    if i / 3600 >= 1:
                        print(
                            "************\n*%-10s*\n*%-10s*\n*%-10s*\n************" % (i, i / 60, i / 3600))
                    elif i / 60 >= 1:
                        print("************\n*%-10s*\n*%-10s*\n************" %
                              (i, i / 60))
                    else:
                        print("************\n*%-10s*\n************" % i)
                    time.sleep(1)

            print(
                "You reached 2147483647 seconds! It's 68.0495348189 YEAR. Yes, ~68 YEAR!")
        elif user == "__EXIT__":
            sys.exit()
        else:
            print("[ERROR]")
            print("Write S; M; H; or T!")
            continue
