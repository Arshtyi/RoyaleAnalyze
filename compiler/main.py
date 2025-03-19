"""
这个脚本用于生成Nuitka打包命令，也许会结合Github Actions使用.
"""
import os
if __name__ == '__main__':
    command = "python -m nuitka --mingw64 --standalone --show-memory --show-progress --include-package=src --include-package-data=src:* --output-dir=out --remove-output"
    ico_path = "res/icons/RA-1.ico"
    command+=" --windows-icon-from-ico="+ico_path
    LICEnSE_path = "LICENSE"
    command+=" --include-data-files="+LICEnSE_path+"="+LICEnSE_path
    README_path = "README.md"
    command+=" --include-data-files="+README_path+"="+README_path
    input_path = "data/input/clansInformation.xlsx"
    command+=" --include-data-files="+input_path+"="+input_path
    assets_path = "assets"
    command+=" --include-data-dir="+assets_path+"="+assets_path
    command+=" main.py"
    with open("compiler.txt", "w", encoding="utf-8") as file:
        file.write(command)