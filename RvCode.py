import random
from N4Tools.Design import Text
from N4Tools.Design import Animation
import os
os.system("clear")
try:
    T=Text()
    An=Animation()
    def h():

        print ("\033[1;33m")



        logo=(r"""

 _______             _______  _______  ______   _______
(  ____ )|\     /|  (  ____ \(  ___  )(  __  \ (  ____ \
| (    )|| )   ( |  | (    \/| (   ) || (  \  )| (    \/
| (____)|| |   | |  | |      | |   | || |   ) || (__
|     __)( (   ) )  | |      | |   | || |   | ||  __)
| (\ (    \ \_/ /   | |      | |   | || |   ) || (
| ) \ \__  \   /    | (____/\| (___) || (__/  )| (____/\
|/   \__/   \_/     (_______/(_______)(______/ (_______/

                      للخروج Ctrl + c
RedVirous
whatsapp:+201024132476

        """)
        An.SlowLine(logo)
        dyxyxy=input("ادغط علي اي زر للمتابعه")
        print("")
    def c():
        try:
            while True:
                print ("""

ملاحظه اكواد شحن 16 رقم

                """)

                ran=(random.randint(1000000000000000,9999999999999999))

                An.SlowText("\033[1;34m يتم تخمين [#]")
                print (' ')
                An.SlowText("\033[1;34m جاري وضع ارقام [#]")
                print (' ')
                An.SlowText("\033[1;34m جاري تحقق من صلاحيه كود [#]")
                print (' ')
                An.SlowText("\033[1;32mتم تحقق من صلاحيه [!] ")
                print (' ')
                An.SlowText("\033[1;34mجاري نقل كود إلي  قاعده بيانات [#]")
                print (' ')
                os.system("""
echo ''' """ + str(ran) + """

'''>>/sdcard/RedVirous/بيانات.txt

                """)
                An.SlowText("\033[1;34m : كود [!]\033[1;32m" + " " + str(ran))
                print (' ')
        except KeyboardInterrupt:
            print ("""



            """)
            ghfhg=input("ادغط علي اي زر للمتابعه او اضغط مرتين CTRL + c للخروج")
            c()


    h()
    c()
except KeyboardInterrupt:


    try:
        print ("""



        """)
        ghfhg=input("ادغط علي اي زر للمتابعه او اضغط CTRL + c للخروج")
        c()
    except KeyboardInterrupt:
        os.system("""
clear
echo ""
        """)

        print (' ')
        print ("تم تخمين")
        print ("روح لذاكره جهاز")
        print ("خش علي مجلد RedVirous")
        print ("وافتح ملف بيانات.txt وجرب اكواد")
        print ("")
        exit()
