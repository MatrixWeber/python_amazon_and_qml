``` sh
pyrcc5 -o pyqt5_qtquick2_example/resources.py resources.qrc
pyinstaller main.py -y --windowed --additional-hooks-dir pyi_hooks/
```