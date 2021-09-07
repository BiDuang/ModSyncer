import sys
import subprocess
from downloader import downloader
import requests

filename = "modsyncer_lastest.exe"


def updatescript(dir: str):

    b = open("upgrade.bat", 'w')
    TempList = "@echo off\n"
    TempList += "if not exist " + filename + " exit \n"
    # 新文件不存在,退出脚本执行
    TempList += "echo ====================================================\n"
    TempList += "echo [Ice Updater] 程序正在更新...请不要断开电源或关闭程序\n"
    TempList += "echo ====================================================\n"
    TempList += "timeout /t 3\n"
    # 3秒后删除旧程序（3秒后程序已运行结束，不延时的话，会提示被占用，无法删除）
    TempList += "del /f " + filename + "\n"
    # 删除当前文件
    TempList += "cd /D " + dir + "\n"
    TempList += "rename " + 'modsyncer_lastest.exe' + ' modsyncer.exe'+"\n"
    TempList += "start modsyncer.exe\n"
    # 启动新程序
    b.write(TempList)
    b.close()
    subprocess.Popen("upgrade.bat")
    sys.exit()
    # 进行升级，退出此程序


def updater(curversion: float, dir: str, autoupdate: bool):

    print("========================================================")
    print("[Ice Updater] 正在尝试与更新服务器通讯...")
    r = requests.get("https://api.biduang.cn/modsyncer/ver.json")
    info = eval(r.text)
    if info['version'] == curversion:
        print("[Ice Updater] ModSyncer已保持最新")
        print("========================================================\n")
        return
    if autoupdate != True:
        print(f"[Ice Updater] 发现新版本，但ModSyncer不会自动更新")
        print(f"[Ice Updater] 您随时可以通过 [设置->启用自动更新] 以重新启用自动更新")
        return
    print(f"[Ice Updater] 发现新版本，ModSyncer即将自动更新，这将需要一点时间...")
    if downloader(0) == False:
        print("[Ice Updater] Notice: 升级失败，请稍后重试")
        print("========================================================\n")
        return
    updatescript(dir)

