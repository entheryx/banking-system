@echo off
set count=0

:Start
set /a count+=1
echo Running attempt %count% of 10
python main.py

if %count% lss 10 (
    echo Waiting for 10 seconds before next run...
    timeout /t 10 /nobreak
    goto Start
)

echo Program has run 10 times. Exiting now.
pause