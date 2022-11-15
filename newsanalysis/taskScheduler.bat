@echo off
schtasks /create /tn "execute.py task" /tr "%cd%\execute.bat" /sc daily /st 00:00
exit