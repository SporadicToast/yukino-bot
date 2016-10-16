@echo off
set currentdir = %~dp0
title  Command Prompt Insta
echo Current directory is %currentdir%
cd %currentdir%
:main
python bottest.py
echo.
echo Press any key to run again
PAUSE > NUL
goto main