@echo off
echo ============================
echo OMOK AI TEAM SETUP START
echo ============================

echo Creating virtual environment...
python -m venv .venv

echo Activating venv...
call .venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing dependencies...
pip install -r requirements.txt

echo Done!
echo ============================
echo Use this before coding:
echo .venv\Scripts\activate
echo ============================

pause