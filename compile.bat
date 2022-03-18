@echo off
call "D:\Program Files\QGIS 3.24.0\bin\o4w_env.bat"
call "D:\Program Files\QGIS 3.24.0\bin\qt5_env.bat"
call "D:\Program Files\QGIS 3.24.0\bin\py3_env.bat"

@echo on
pyrcc5 -o resources.py resources.qrc