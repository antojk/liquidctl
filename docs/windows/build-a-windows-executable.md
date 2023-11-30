# Build a single executable for deploying to Win32 platforms

PyInstaller reads a Python script written by you. It analyzes your code to discover every other module and library your
script needs in order to execute. Then it collects copies of all those files – including the active Python interpreter! 
– and puts them with your script in a single folder, or optionally in a single executable file.

PyInstaller is tested against Windows, macOS, and GNU/Linux. However, it is not a cross-compiler: to make a 
Windows app you run PyInstaller in Windows; to make a GNU/Linux app you run it in GNU/Linux, etc. PyInstaller has been 
used successfully with AIX, Solaris, FreeBSD and OpenBSD, but is not tested against them as part of the continuous
integration tests.

There is a `cli.spec` file available in the root folder to be used with Pyinstaller tool. Currently, the spec file has been
tested against a win32 build. The tool allows you to build a platform specific executable that can be called from the 
terminal or command line.

## Install Pyinstaller

Pyinstaller can be installed into your build environment using 'pip' command

```
pip install pyinstaller
```
or
```
python -m pip install pyinstaller
```

## Pre-requisites  to build

You need the UPX compression tool to make the executable smaller. It also helps in execution bootstrap. Since this is a 
command line utility, the performance difference is significant. You can download this utility as a portable execution from
https://upx.github.io/ . Download the Win64 version and unzip the same to a convenient directory

## How to Build

* Bundled as a directory method: 
You need to run the following command in the root directory of the project:

```
pyinstaller  --distpath .\dist\ --upx-dir <you upx folder>  .\cli.spec
```

Replace `<your upx folder>` argument to where you have unzipped yours. This can be a relative path from the project root
where we are executing pyinstaller from. The executable file will be found in the `<project root>\dist\liquidCtl` folder.
You will have to copy the entire liquidCtl folder or its contents for the executable to work.

* Single Executable



### References
1. Pyinstaller: https://pyinstaller.org/en/stable/index.html
2. SpecFileFormat: https://pyinstaller.org/en/stable/spec-files.html
3. Upx tool: https://github.com/upx/upx 
