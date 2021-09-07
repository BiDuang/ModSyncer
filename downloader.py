
# ModSyncer下载模块
# Powered by BiDua

from ftplib import FTP
import time


def downloader(mode: str):
    ftp = FTP()
    ftp.set_debuglevel(0)

    if mode == 0:
        add = "119.188.248.230"
        port = 21
        account = "fser"
        password = "WGKSfj3zpNXkGJmz"
        notice = "Ice Updater"
    elif mode == 1:
        add = "irain.cc"
        port = 2121
        account = "modsync"
        password = "modsync"
        notice = "ModSyncer"

    try:
        ftp.connect(add, port)
        ftp.login(account, password)
    except OSError:
        print("ERROR======================================================")
        print(f"[{notice}] 无法连接至服务器")
        print("ERROR=======================================================")
        return False
    except TimeoutError:
        print("ERROR======================================================")
        print(f"[{notice}]] 服务器响应超时")
        print("ERROR=======================================================")
        return False
    print("============================================================")
    print(f"[{notice}] 成功与服务器建立连接，传输开始...")
    print("============================================================")
    time.sleep(1.0)
    ftp.encoding = 'utf-8'

    if mode == 0:
        ftp.cwd('/modsyncer')
        f = open('modsyncer_lastest.exe', 'wb')
        ftp.retrbinary('RETR modsyncer_lastest.exe', f.write)

    elif mode == 1:
        files = ftp.nlst()
        for file in files:
            print(f"[{notice}] 正在获取{file}")
            f = open(file, 'wb')
            ftp.retrbinary(f"RETR {file}", f.write)

    f.close()
    ftp.quit()
    return True
