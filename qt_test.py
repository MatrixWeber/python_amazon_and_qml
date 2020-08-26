import os
import sys

from PyQt5.QtCore import QUrl, QObject
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
import resources  # load resources built by pyrcc5
from login_to_amazon import login_to_amazon
from handle_login_and_password_file import write_login_and_password_to_file, read_login_and_password_from_file

# Set the QtQuick Style
# Acceptable values: Default, Fusion, Imagine, Material, Universal.
os.environ['QT_QUICK_CONTROLS_STYLE'] = (sys.argv[1]
                                         if len(sys.argv) > 1 else "Material")

# Create an instance of the application
# QApplication MUST be declared in global scope to avoid segmentation fault
app = QApplication(sys.argv)

# Create QML engine
engine = QQmlApplicationEngine()
# Load the qml file into the engine
engine.load(QUrl('qrc:/qml/qt_test.qml'))

# Qml file error handling
if not engine.rootObjects():
    sys.exit(-1)

# Send QT_QUICK_CONTROLS_STYLE to qt_test qml (only for demonstration)
# For more details and other methods to communicate between Qml and Python:
#   http://doc.qt.io/archives/qt-4.8/qtbinding.html
qtquick2Themes = engine.rootObjects()[0].findChild(
    QObject,
    'qtquick2Themes'
)
loginTextField = engine.rootObjects()[0].findChild(
    QObject,
    'loginTextField'
)

passwordTextField = engine.rootObjects()[0].findChild(
    QObject,
    'passwordTextField'
)

startButton = engine.rootObjects()[0].findChild(
    QObject,
    'startButton'
)

stopButton = engine.rootObjects()[0].findChild(
    QObject,
    'stopButton'
)

login, password = read_login_and_password_from_file("C:/Users/Alex/PycharmProjects/amazon_login/login_data.txt")
if login:
    loginTextField.setProperty('text', login) 
startButton.clicked.connect(lambda: login_to_amazon(loginTextField.property('text'), passwordTextField.property('text')))
#stopButton.clicked.connect(driver.close)

# engine.quit.connect(app.quit)
# Unnecessary,
# since QQmlEngine.quit has already connect to QCoreApplication.quit

sys.exit(app.exec_())
