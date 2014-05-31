@echo off
cls

set OLDPATH=%PATH%
set PATH=d:\miktex\miktex\bin;%PATH%

echo ***
echo *** Cleanup and update basic info files
echo ***
set PROJECT=technical_indicators

python py_app_ver.py
for /f "delims=" %%f in (py_ver.txt) do set PY_VER=%%f
for /f "delims=" %%f in (app_ver.txt) do set APP_VER=%%f
del py_ver.txt
del app_ver.txt

rd /s /q build
rd /s /q dist
rd /s /q %PROJECT%.egg-info
rd /s /q %PROJECT%-%APP_VER%
if exist *.pyc del *.pyc
if exist %PROJECT%\*.pyc del %PROJECT%\*.pyc

copy /y AUTHORS.rst AUTHORS.txt > nul
copy /y ChangeLog.rst ChangeLog.txt > nul
copy /y README.rst README.txt > nul
copy /y LICENSE.rst LICENSE.txt > nul

copy /y README.txt %PROJECT% > nul
copy /y AUTHORS.txt %PROJECT% > nul
copy /y LICENSE.txt %PROJECT% > nul
copy /y ChangeLog.txt %PROJECT% > nul

echo ***
echo *** Create documentation
echo ***
set SPHINXOPTS=-W -E

ren doc\index.rst index.ori
python prep_rst2pdf.py
cd doc
cmd /c make clean
cmd /c make latex
cd _build\latex
pdflatex.exe %PROJECT%.tex
echo ***
echo *** Repeat to correct references
echo ***
pdflatex.exe %PROJECT%.tex
if not exist ..\..\..\%PROJECT%\doc md ..\..\..\%PROJECT%\doc
copy /y %PROJECT%.pdf ..\..\..\%PROJECT%\doc > nul
cd ..\..
del index.rst
ren index.ori index.rst

cmd /c make clean
cmd /c make html
xcopy /y /e _build\html\*.* ..\%PROJECT%\doc\ > nul

cmd /c make clean
cd ..
pause
cls

if "%1"=="test" goto :TEST
if "%1"=="pypi" goto :PYPI
if "%1"=="cxf" goto :CXF
if "%1"=="py2exe" goto :PY2EXE

echo ***
echo *** Build only
echo ***
python setup.py sdist bdist_egg bdist_wininst bdist_wheel
goto :EXIT

:TEST
echo ***
echo *** TEST: Register, build and upload
echo ***
python setup.py register -r test
echo ***
echo *** End register
echo ***
pause
cls

python setup.py sdist bdist_egg bdist_wininst bdist_wheel
python setup.py sdist bdist_egg bdist_wininst bdist_wheel upload -r test
goto :EXIT

:PYPI
echo ***
echo *** PYPI: Register, build and upload
echo ***
python setup.py register -r pypi
echo ***
echo *** End register
echo ***
pause
cls

python setup.py sdist bdist_egg bdist_wininst bdist_wheel
python setup.py sdist bdist_egg bdist_wininst bdist_wheel upload -r pypi
goto :EXIT

:CXF
echo ***
echo *** CXF build
echo ***
python cxf_setup.py build bdist_msi
rem python cxf_setup.py build_exe
rem cxfreeze cxf_setup.py build_exe
copy build\exe.win32-%PY_VER%\%PROJECT%\*.* build\exe.win32-%PY_VER%
goto :EXIT

:PY2EXE
echo ***
echo *** PY2EXE build
echo ***
python setup.py py2exe
if exist dist\__main__.exe ren dist\__main__.exe %PROJECT%.exe
goto :EXIT

:EXIT
set PATH=%OLDPATH%
set OLDPATH=
set PY_VER=
set APP_VER=
