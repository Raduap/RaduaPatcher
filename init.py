import BrainClass.BrainThinkinit as brain
import Recognise
def WindowInit():
    print("---------------------------------------------------------------")
    print("                    *** * ** ****** ** ****** *")
    print("                 * ********* ******** * ***** * **              ")
    print("           ** * **** * ********* ******** * ***** * **              ")
    print("          * ** * **** * ********* ******** * ***** * ** *             ")
    print("\n")
    print("  **    ***       Welcome To Radua Patcher ver 1.3      ***         **")
    print("\n")
    print("          * ** * **** * ********* ******** * ***** * ** *             ")
    print("           ** * **** * ********* ******** * ***** * **              ")
    print("                 * ********* ******** * ***** * **              ")
    print("                    *** * ** ****** ** ****** *")
    print("---------------------------------------------------------------")
    print("\n")
    print("\n")

def Menulist():
    print("            输入搜索内容，选择搜索引擎，查找目录结果      ")
    print("                 MindMap init think node                  ")
    print("                 1. Baidu 搜索引擎                  ")
    print("                 2. Bing 搜索引擎                  ")
    print("                 3. 360  搜索引擎                  ")
    input(choice)
    MenuChoice (choice)
    
def MenuChoice(choice):
    if(choice == 1) choice=2