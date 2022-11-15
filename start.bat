@echo off
start cmd /k "cd newsanalysis/ & python execute.py"
start cmd /c "cd news-analysis-api & npm start"
start cmd /c "cd news-analysis-website & npm start"
exit