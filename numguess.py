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
import sys
from PyQt5.QtWidgets import *
import time
import random


# *     |  hu | en
# *     V
LANG = "__USER__"


class TextIsNotInt(Exception):
    pass


class TextIsNotRelativeToNumber(Exception):
    pass


szerda_mode = False


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.lineEntry = QLineEdit(self)
        self.lineEntry.move(16, 16)
        self.lineEntry.resize(130, 20)

        self.qlabel = QLabel(self)
        self.qlabel.move(16, 64)

        self.lineEntry.textChanged.connect(self.onChanged)

        self.setGeometry(50, 50, 320, 200)
        self.setWindowTitle(texts["title"])
        self.show()

    def onChanged(self, text):
        try:
            if int(text) < myNumber:
                myIsGood = texts["bigger"]
            elif int(text) == myNumber:
                myIsGood = ":)"
                for i in range(21):
                    print(
                        "*******************************************************************************")
                    time.sleep(0.047619047619047616)
                print("This program comes with ABSOLUTELY NO WARRANTY. \nThis is free software, and you are welcome to redistribute it under certain conditions.")
            elif int(text) > myNumber:
                myIsGood = texts["smaller"]
            elif text == None or text == "" or text == " ":
                myIsGood = ""
            else:
                raise TextIsNotRelativeToNumber(
                    "The text you entered, is an int (good), but it's not bigger, smaller, or equal to the number (bad).")
        except ValueError:
            if text == None or text == "" or text == " ":
                myIsGood = ""
            else:
                raise TextIsNotInt(texts["notInt"])
        else:
            self.qlabel.setText(myIsGood)
        finally:
            self.qlabel.adjustSize()
            self.lineEntry.adjustSize()


if __name__ == '__main__':
    if LANG == "__USER__":
        LANG = input("HU | EN>").lower()

    if LANG == "hu":
        texts = {
            "title": "Számkitalálás",
            "bigger": "A szám nagyobb!",
            "smaller": "A szám kisebb!",
            "notInt": "Amit megadtál, az nem szám!"
        }
    else:
        texts = {
            "title": "Number guess",
            "bigger": "The number is bigger",
            "smaller": "The number is smaller",
            "notInt": "Write numbers!"
        }

    print("This program comes with ABSOLUTELY NO WARRANTY. \nThis is free software, and you are welcome to redistribute it under certain conditions.")

    if szerda_mode:
        myNumber = random.choice([36, 56, 69, 756])
    else:
        myNumber = random.randrange(1, 101)

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
