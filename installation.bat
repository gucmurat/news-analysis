@echo off
start cmd /c "cd newsanalysis/ & echo Python icin gerekli libraryler yukleniyor. & python setup_env.py"
start cmd /c "cd news-analysis-api & echo Node.JS ve Express yukleniyor. & npm install"
start cmd /c "cd news-analysis-website & echo React yukleniyor. & npm install"
schtasks /create /tn "execute.py task" /tr "%cd%\newsanalysis\execute.bat" /sc daily /st 00:00
exit