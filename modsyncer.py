# Automatically install missing dependencies, English support, Linux support.
from downloader import downloader
import os
import time
import sys
import getpass
import json
import subprocess
import pkg_resources
from guide import guide
from updater import updater

if os.name == 'nt':
    os.system('cls')
elif os.name == 'posix':
    os.system('clear')
time.sleep(1)

required = {'requests'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call(
        [python, '-m', 'pip', 'install', *missing],
        stdout=subprocess.DEVNULL
    )
# Install missing dependencies. 安装依赖

if os.name == 'nt':
    arg = '\\'
elif os.name == 'posix':
    arg = '/'

exedir = os.path.realpath(sys.argv[0])
dirct = exedir.split(arg)
exename = dirct[-1].strip()
exedir = exedir.replace(dirct[-1].strip(), '')
filelist = os.listdir(exedir)
# 获取程序目录 Get program directory.

ver = 3.5
if os.path.isfile("upgrade.bat"):
    os.remove("upgrade.bat")
# 删除升级脚本 Remove update script.

try:
    f = open("settings.json", 'r')
except FileNotFoundError:
    guide(getpass.getuser())
    f = open("settings.json", 'r')

settings = json.load(f)

print(f"================== [MobSyncer v{ver}] ====================")
print("======Powered by BiDuang & AsakiRain | [c] 2021 ========")
print(f"欢迎！ {getpass.getuser()}")
time.sleep(1)

updater(ver, exedir, settings['auto_update'])

usrinp = input("[ModSyncer] 输入[C]进入同步模式，输入[S]进入偏好设置:\n")

if usrinp.lower() == 'c':

    print("同步服务器已设置为：AsakiRain的Mod分发服务器")
    if settings['sync_mode'] == 1:
        info = '当前同步模式为[由同步服务器来决定]'
    elif settings['sync_mode'] == 2:
        info = '当前同步模式为[每次同步都删除文件夹下所有的 .jar 文件]'
    elif settings['sync_mode'] == 3:
        info = '当前同步模式为[每次同步只删除文件夹下以 [r] 开头的文件]'

    print("[ModSyncer] 同步前，请您确认：")
    print("1. ModSyncer只提供文件传输，不存储任何文件，也不为文件的稳定性或版权作任何担"
        "保")
    print(f"2. {info}，请您确认程序放置的目录是您的Mods目录：\n{exedir}")
    if settings['sync_mode'] == 2:
        print(f"3. 注意！您选择了[每次同步都删除文件夹下所有文件]，如果继续，您将失去文件"
            "夹下全部文件！")
    st = input('当您知悉以上信息并准备好开始同步，请输入[Y] (按其他键取消同步): ')

    if st.lower() == 'y':
        
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        
        print("[提示] 正在进行同步前的准备工作，这不会需要很长时间...")
        sum = 0
        for file in filelist:
            if settings['sync_mode'] == 2:
                if file != exename and file != 'settings.json':
                    print(f"[提示] 正在从 {exedir} 抹除 {file} ...")
                    os.remove(f"{exedir}/{file}")
                    sum += 1
            if settings['sync_mode'] == 3 or settings['sync_mode'] == 1:
                if file.startswith('[r]'):
                    print(f"[提示] 正在从 {exedir} 抹除 {file} ...")
                    os.remove(f"{exedir}/{file}")
                    sum += 1

        print(f"[ModSyncer] 清理工作已完成，共删除了{sum}个文件，同步将很快开始")

        if downloader(1):
            print("[ModSyncer] 同步已完成，请按任意键退出")
        else:
            print("[ModSyncer] 同步未完成，请按任意键退出")
    else:
        print("[ModSyncer] 用户取消了同步，请按任意键退出")

elif usrinp.lower() == 's':
    print("设置选项还在开发中...您可以通过删除[settings.json]以重新初始化")
    print("按任意键退出")
else:
    print("无效输入！请按任意键退出。")
anyk = input()
