"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import time


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


def hour(hour):
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
    print("This program comes with ABSOLUTELY NO WARRANTY. \nThis is free software, and you are welcome to redistribute it under certain conditions.")
    while True:
        user = input("[S]ec; [M]in; or [H]our>").upper()
        if user == "S":
            user = int(input("Sec>"))
            sec(user)
            print("END")
        elif user == "M":
            user = int(input("Min>"))
            min(user)
            print("END")
        elif user == "H":
            user = int(input("Hour>"))
            hour(user)
            print("END")
        else:
            print("[ERROR]")
            print("Write S; M; or H!")
            continue
