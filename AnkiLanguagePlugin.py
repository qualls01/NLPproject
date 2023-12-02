from aqt import mw
from aqt.qt import QAction

def hello_anki():
    print("Hello, Anki!")

action = QAction("Hello, Anki!", mw)
action.triggered.connect(hello_anki)
mw.form.menuTools.addAction(action)
