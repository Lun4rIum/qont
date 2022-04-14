@echo off
curl https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe --output "%programfiles%/python3.10.exe"
cd "%programfiles%"
START /WAIT python3.10.exe /quiet InstallAllUsers=1 PrependPath=1
cd /D "%~dp0"
"C:\Program Files\Python310\python.exe" -m pip install Flask
"C:\Program Files\Python310\python.exe" -m pip install zip-files

curl -L http://cdn.discordapp.com/attachments/706560559390130178/964187645519470623/contactGH.zip --output "%programfiles%/qont.zip"

cd "%programfiles%"
powershell Expand-Archive qont.zip




set SCRIPT="%TEMP%\%RANDOM%-%RANDOM%-%RANDOM%-%RANDOM%.vbs"

echo Set oWS = WScript.CreateObject("WScript.Shell") >> %SCRIPT%
echo sLinkFile = "%USERPROFILE%\Desktop\qont.lnk" >> %SCRIPT%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %SCRIPT%
echo oLink.TargetPath = "%programfiles%\qont\contactGH\launch.bat" >> %SCRIPT%
echo oLink.Save >> %SCRIPT%

cscript /nologo %SCRIPT%
del %SCRIPT%