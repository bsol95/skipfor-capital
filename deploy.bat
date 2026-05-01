@echo off
cd /d "%~dp0"
git add -A
git commit -m "Update site"
git push
echo.
echo Done. Live at https://bsol95.github.io/skipfor-capital
pause
