import time
import json
import os

initdict = {
    'auto_update': True,
    'sync_mode': 1
}


def guide(usr: str):
    print(f":)   嗨，初次见面！{usr}")
    time.sleep(2)
    print("ModSyncer 将进行一些准备工作，请坐和放宽...")
    print("========== 这不会需要很长时间 ==========")
    f = open('settings.json', 'w')
    
    print("[ModSyncer Guide] 欢迎您使用ModSyncer！ModSyncer是一款旨在方便地同步您与"
        "服务器Mods文件夹的程序")
    # print("[ModSyncer Guide] 如您希望跳过使用向导，请输入[C]以退出或按任意键继续向导")
    print("========== 如果您选择了跳过向导，ModSyncer 将采用推荐设置完成初始化 ======="
        "==")
    inp = input("[ModSyncer Guide] 是否跳过向导？(Y/N) ")
    
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    
    if inp.lower() == 'n':
        print("[ModSyncer Guide] 首先，让我们来选择使用何种同步模式：")
        print("[1] 由同步服务器来决定（推荐）")
        print("[2] 每次同步都删除文件夹下所有文件")
        print("[3] 每次同步只删除文件夹下以 r 开头的文件")
        slt = input("请输入您所选选项的编号：  ")
        if slt == '1':
            print("[ModSyncer Guide] 同步模式已设为[由同步服务器来决定]")
        elif slt == '2':
            print("[ModSyncer Guide] 同步模式已设为[每次同步都删除文件夹下所有文件]")
            initdict["sync_mode"] = 2
        elif slt == '3':
            print("[ModSyncer Guide] 同步模式已设为[每次同步只删除文件夹下以 [r] 开头"
                "的文件]")
            initdict["sync_mode"] = 3
        else:
            print("[ModSyncer Guide] 使用推荐设置，同步模式已设为[由同步服务器来决定]")
        print("[ModSyncer Guide] 很好，让我们继续下一个设置吧")
        print("[ModSyncer Guide] 然后，您希望 ModSyncer 启用自动更新吗：")
        print("[1] 启用自动更新（推荐）")
        print("[2] 禁用自动更新")
        slt = input("请输入您所选选项的编号：  ")
        if slt == '1':
            print("[ModSyncer Guide] 自动更新已设为[启用]")
        elif slt == '2':
            print("[ModSyncer Guide] 自动更新已设为[禁用]")
            initdict["auto_update"] = False

    json.dump(initdict, f)
    f.close()
    
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    
    print("[ModSyncer Guide] 好的，您已经完成了全部初始设定，请开始使用吧！")
    return
