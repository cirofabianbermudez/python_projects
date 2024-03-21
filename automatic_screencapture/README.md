# Automatic Screencapture


## Getting started

This project is intended to be used when you want to screencapture some content automaticly in your screen in the same spot over and over again and you have to press a key on you keyboard to move to another part of the content, the solution automate this with Python. Then you can join all the images into a PDF using whatever solution you have available, here a choosed ImageMagick because is open-source and lightweight.

## Requirements

- Python 3.9.9
-  ImageMagick 7.1.1-28

## Installation

> [!note] Note
> Tested with Python 3.9.9

```bash
python --version
python -m venv venv
./venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
pip install -r .python_requirements
```

If you want to use the same version of the packages as me instead of the latest change the last command to:

```bash
pip install -r requirements.txt
```
### Installion of ImageMagick

If you are working with a Windows machine you can install almost everything using the [Scoop](https://scoop.sh/) command-line installer for Windows.

If you don't already have Scoop you can install it opening a PowerShell terminal (version 5.1 or later) and runnning:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

Then you can install [ImageMagick](https://imagemagick.org/) with this command.

```powershell
scoop install main/imagemagick
```
You can also install ImageMagick manually if you like but the advantage of installing things with Scoop is that you don't have to put the program executable into the PATH, this is take care of by Scoop by default.

## Usage
```bash
python main.py
sh convert.sh
```
> [!note] Note
> To run the bash script you need to have installed [Git For Windows](https://gitforwindows.org, the easiest way to have install it is `scoop install main/git`.
## License
MIT License.
Copyright (c) 2024 Ciro Bermudez

## Project status
The project is completed, it is easy to use and to modify to acomodate the user necesities.
TODO: Check grammar in the REAMDE.md file

