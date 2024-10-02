import pygame
import tkinter as tk
from tkinter import *
import random


#插音樂  https://www.youtube.com/watch?v=pRsVfFmWfDI
pygame.mixer.init()
pygame.mixer.music.load(r'want to see you.mp3')
pygame.mixer.music.play(-1,10)
#建立主視窗
window = tk.Tk()
score=IntVar()
openend3=IntVar()
# 設定視窗標題
window.lift()
window.title('seek the past 追尋過去')
# 設定視窗大小(寬x高) 背景圖 固定大小
window.geometry('723x633+0+0')
window.resizable(0,0)
room=tk.PhotoImage(file='AnyConv.com__Room.gif')
back=tk.PhotoImage(file='AnyConv.com__back3.gif')
roompic=tk.Label(window,image=room)
roompic.pack()
#指令
def opendiary():
   if(score.get()>=0):
      diary1["state"] = ACTIVE
      diary2["state"] = ACTIVE
      diary3["state"] = ACTIVE
      diary4["state"] = ACTIVE
def diary1text():
   diary1window = tk.Toplevel()
   diary1window.title('日記 1')
   diary1window.geometry('300x300')
   diary1window.resizable(0,0)
   diary1text1=tk.Label(diary1window,font=('標楷體', 12),image=back,compound=CENTER,text='1996/6/1                        \n原來遊樂園是這樣的\n有好多好玩的器材\n哥哥還為我贏得了一個娃娃\n今天真的好開心...\n\n\n1997/5/5                        \n哥哥去出差一周了\n我也過了一週一個人的生活\n明明以前也是這樣過的\n但現在卻好不習慣\n好想哥哥...\n')
   diary1text1.pack()
def diary2text():
   diary2window = tk.Toplevel()
   diary2window.title('日記 2')
   diary2window.geometry('300x300')
   diary2window.resizable(0,0)
   diary1text1=tk.Label(diary2window,font=('標楷體', 12),image=back,compound=CENTER,text='1999/7/1                        \n今天在學校跟同學打架了\n他們說我父母是壞人\n哥哥也是\n我氣不過\n就打了回去\n哥哥聽完之後沒有生氣我打架\n只是幫我上藥\n緊緊抱住了我...\n\n\n2000/9/7                        \n原來在他們的眼中\n和一個人的相處認識比不上一段流言\n朋友什麼的\n在他們眼中就是笑話吧!\n還好還有人是在乎我的...')
   diary1text1.pack()
def diary3text():
   diary3window = tk.Toplevel()
   diary3window.title('日記 3')
   diary3window.geometry('300x300')
   diary3window.resizable(0,0)
   diary1text1=tk.Label(diary3window,font=('標楷體', 12),image=back,compound=CENTER,text='2003/8/15                        \n今天是我18歲生日\n說好要一起過每一次生日的\n但今年他失約了\n今天一到家\n我就收到了他的死訊\n這次的我真的是孤身一人了...\n\n\n2006/8/15                        \n你果然是希望我可以好好活下去\n但孤身一人要怎麼活下去\n我不知道\n但我會努力的\n起碼好好活著9年\n活過你陪著我的時間')
   diary1text1.pack()
def diary4text():
   diary4window = tk.Toplevel()
   openend3.set(1)
   diary4window.title('日記 4')
   diary4window.geometry('300x300')
   diary4window.resizable(0,0)
   diary4text1=tk.Label(diary4window,font=('標楷體', 12),image=back,compound=CENTER,text='2009/8/15                        \n我好想你 好想你\n你回來好不好\n我好想再見你一次\n\n\n2020/8/15                        \n事情都快要解決了呢\n我好開心 好開心\n終於可以去見你了....')
   diary4text1.pack()
def audio1():
   audio1window = tk.Toplevel()
   audio1window.title('一段對話')
   audio1window.geometry('400x170')
   audio1window.resizable(0,0)
   audio1text=tk.Label(audio1window,font=('標楷體', 12),image=back,compound=CENTER,text='"他們怎麼可以做這些事!!!"\n"你查到了甚麼?"\n"當年事情的真相，他們死亡的真相......"\n"他們也太喪心病狂了!!!"\n"是呀，但知道了真相又如何"\n"你不想..."\n"想，但我不想要他捲入其中，我希望他有正常的生活"\n"可是..."\n"如果我復仇的話，小傢伙也會被連累的"')
   audio1text.pack()
def gift1text():
   giftwindow = tk.Toplevel()
   giftwindow.title('禮物')
   giftwindow.geometry('300x200')
   giftwindow.resizable(0,0)
   gifttext=tk.Label(giftwindow,font=('標楷體', 12),image=back,compound=CENTER,text='那是12歲那年\n哥哥送給我的\n哥哥看我一直做惡夢\n送給我讓我抱著睡覺\n在那之後\n也許是因為安心吧\n作惡夢的頻率就變低了...')
   gifttext.pack()
def letter_1():
   letter_1_window = tk.Toplevel()
   letter_1_window.title('信件')
   letter_1_window.geometry('300x250')
   letter_1_window.resizable(0,0)
   lettertext=tk.Label(letter_1_window,font=('標楷體', 12),image=back,compound=CENTER,text='如果你看到這封信\n你應該查到了所有的真相\n而我應該也死了\n但答應我不要做傻事\n不要復仇\n好嗎?\n好好的活下去\n過著一般的生活\n\n\n      哥哥')
   lettertext.pack()
def letter_2():
   letter_2_window = tk.Toplevel()
   letter_2_window.title('信件')
   letter_2_window.geometry('300x250')
   letter_2_window.resizable(0,0)
   lettertext=tk.Label(letter_2_window,font=('標楷體', 12),image=back,compound=CENTER,text='我知道有很多人\n會因為你的父母而對你惡言相向\n疏遠你厭惡你\n但你要相信\n那不是你的問題\n你是很好很好的\n還有很多人是喜歡你的\n不要對人失望\n\n\n     愛你的哥哥')
   lettertext.pack()
def birthday_card():
   birthday_card_window = tk.Toplevel()
   birthday_card_window.title('生日卡片')
   birthday_card_window.geometry('300x200')
   birthday_card_window.resizable(0,0)
   birthday_card_text=tk.Label(birthday_card_window,font=('標楷體', 12),image=back,compound=CENTER,text='祝你10歲生日快樂\n這是我們成為家人的第一年\n也是我第一次擁有真正意義上的家人\n我不知道我是不是一個稱職得哥哥\n但我們一起努力好不好\n成為彼此的依靠\n\n\n        哥哥')
   birthday_card_text.pack()
spliteropen=tk.PhotoImage(file='button1.gif')
def splinter1open():
   global splinter1
   splinter1 = tk.Toplevel()
   splinter1.title('崩塌')
   splinter1.geometry('300x200')
   splinter1.resizable(0,0)
   splinter1text=tk.Label(splinter1,font=('標楷體', 12),image=back,compound=CENTER,text='我的世界崩塌了\n在聽見父母死亡消息的那一刻\n除了傷心之餘\n還有震撼\n聽見一句又一句刺耳的話語傳入耳中\n聽著那些"親人"推卸著我的去處\n神情中還帶著些許的惶恐\n我感覺到不解與心寒\n為甚麼大家如此害怕\n我做錯了什麼\n為甚麼大家都不要我\n我不懂')
   splinter1text.pack()
def splinter2open():
   global splinter2
   splinter2 = tk.Toplevel()
   splinter2.title('入夢')
   splinter2.geometry('300x300')
   splinter2.resizable(0,0)
   splinter2text=tk.Label(splinter2,font=('標楷體', 12),image=back,compound=CENTER,text='從那天以後\n我就輾轉住宿在各個親戚家中\n但\n在他們眼中\n我就像是瘟神般不受待見\n這樣的日子持續了一年\n直到有一天\n一位陽光的青年\n來到了親戚家中\n說他接受父母的請託照顧我\n將我帶走\n從此之後\n他就成了我的家人\n我唯一的家人')
   splinter2text.pack()
def splinter3open():
   global splinter3
   splinter3 = tk.Toplevel()
   splinter3.title('夢境')
   splinter3.geometry('300x250')
   splinter3.resizable(0,0)
   splinter3text=tk.Label(splinter3,font=('標楷體', 12),image=back,compound=CENTER,text='他對我來說像是兄長一般\n他總是很溫柔的對我\n陪我玩樂陪我打鬧\n會帶我出外遊玩\n會在我受欺負時幫我出氣幫我處理\n也會在我受傷之時安慰我\n相較於之前忙碌的父母\n我和他之間的相處更多\n也擁有了更多珍貴的回憶\n這樣的日子真好\n真希望可以一直這樣過下去')
   splinter3text.pack()
def splinter4open():
   global splinter4
   splinter4 = tk.Toplevel()
   splinter4.title('夢碎')
   splinter4.geometry('300x350')
   splinter4.resizable(0,0)
   splinter4text=tk.Label(splinter4,font=('標楷體', 12),image=back,compound=CENTER,text='好的日子果然不會長久\n在18歲那年\n我再次的進入了地獄\n我又一次的失去了我的家人\n在我18歲那年\n而所有的調查人員皆認定他自殺\n我不相信他會如此\n我想知道事情的真相\n而在一次次的調查後真相也浮出了水面\n原來父親母親和哥哥的死亡\n都是因為知道了一些"真相"\n而那些人為了保住這些見不得光的事\n而知情者就成為犧牲品')
   splinter4text.pack()
def splinter5open():
   global splinter5
   splinter5 = tk.Toplevel()
   splinter5.title('墜落')
   splinter5.geometry('300x250')
   splinter5.resizable(0,0)
   splinter5text=tk.Label(splinter5,font=('標楷體', 12),image=back,compound=CENTER,text='為何良善之人反而殞命\n而惡貫滿盈者卻活得光鮮亮麗?\n我不甘心他們的性命消逝的毫無聲息\n更不甘心那群人如此逍遙法外\n我與其他同樣失去所愛之人者合作\n調查、設局、復仇\n十五年間\n我們用盡了所能用的一切資源\n最終\n小蝦米扳倒大鯨魚\n我們成功了\n讓他們自相殘殺\n將他們繩之以法\n雖然代價是生命\n很多人的、自願獻出的生命')
   splinter5text.pack()
def dis1():
   btn1.destroy()
   storytxt1.destroy() 
   splinter1open()
   global btn1_get
   btn1_get = tk.Button(window,image=spliteropen,text='崩塌',font=('標楷體', 12),command=splinter1open,compound='center',fg='white',bd=0)
   btn1_get.place(x=40, y=35)  
   score.set(score.get()+1)
   fin()
def dis2():
   btn2.destroy()
   storytxt2.destroy() 
   splinter2open()
   btn2_get = tk.Button(window,image=spliteropen,text='入夢',font=('標楷體', 12),command=splinter2open,compound='center',fg='white',bd=0)
   btn2_get.place(x=80, y=35)
   score.set(score.get()+1)
   fin()
def dis3():
   btn3.destroy()
   storytxt3.destroy() 
   splinter3open()
   btn3_get = tk.Button(window,image=spliteropen,text='夢境',font=('標楷體', 12),command=splinter3open,compound='center',fg='white',bd=0)
   btn3_get.place(x=120, y=35)
   score.set(score.get()+1)
   fin()
def dis4():
   btn4.destroy()
   storytxt4.destroy() 
   splinter4open()
   btn4_get = tk.Button(window,image=spliteropen,text='夢碎',font=('標楷體', 12),command=splinter4open,compound='center',fg='white',bd=0)
   btn4_get.place(x=160, y=35)
   score.set(score.get()+1)
   fin()
def dis5():
   btn5.destroy()
   storytxt5.destroy() 
   splinter5open()
   btn5_get = tk.Button(window,image=spliteropen,text='墜落',font=('標楷體', 12),command=splinter5open,compound='center',fg='white',bd=0)
   btn5_get.place(x=200, y=35)
   score.set(score.get()+1)
   fin()
back2=tk.PhotoImage(file='AnyConv.com__back2.gif')
def fin():
   if(score.get()==5):
      endbtn["state"] = ACTIVE
#
def story1():
   opendiary()
   global num1,storytxt1 ,label_guessanswer,guess,sbtn1,guessentry
   num1=random.randint(1,100)
   storytxt1 = tk.Toplevel()
   storytxt1.title('崩塌')
   storytxt1.geometry('500x350')
   storytxt1.resizable(0,0)
   labelback_guess=tk.Label(storytxt1,image=back2,compound=CENTER)
   labelback_guess.place(x=0, y=0)
   label_guess=tk.Label(storytxt1,text='猜出數字(1~100)',font=('標楷體', 14),bg='lightcyan')
   label_guess.place(x=170, y=100)
   guessentry = tk.Entry(storytxt1,text='guess')
   guessentry.place(x=170, y=150)
   label_guessanswer=tk.Label(storytxt1,font=('標楷體', 14),bg='lightcyan')
   label_guessanswer.place(x=170, y=200)
   guess = tk.Button(storytxt1,text='guess',font=('標楷體', 14),command=guess1,height = 1, width = 5)
   guess.place(x=210, y=250)
   sbtn1 = tk.Button(storytxt1,text='記憶碎片',font=('標楷體', 14),command=dis1,height = 1, width = 7,state=DISABLED)
   sbtn1.place(x=200, y=300)
   storytxt1.mainloop()
def guess1():
    guessnum=int(guessentry.get())
    if(guessnum>num1):
      label_guessanswer['text']='小一點'
    elif(guessnum<num1):
      label_guessanswer['text']='大一點'
    else:
      label_guessanswer['text']='正確'
      sbtn1["state"] = ACTIVE
      guess["state"] = DISABLED
# 
def story2():
   opendiary()
   global x,computer,storytxt2,guess2answer,sbtn2, guess2btn,count2,paperbtn,stonebtn,sissorbtn,counttext
   x=IntVar()
   count2=IntVar()
   storytxt2 = tk.Toplevel()
   storytxt2.title('入夢')
   storytxt2.geometry('500x350')
   labelback_guess=tk.Label(storytxt2,image=back2,compound=CENTER)
   labelback_guess.place(x=0, y=0)
   counttext=tk.Label(storytxt2,text='贏三次解鎖',font=('標楷體', 14),bg='lightcyan')
   counttext.place(x=50, y=50)
   computer=tk.Label(storytxt2,font=('標楷體', 14),bg='lightcyan')
   computer.place(x=250, y=50)
   paperbtn = tk.Button(storytxt2,text='布',font=('標楷體', 14),command=si)
   paperbtn.place(x=135, y=100)
   sissorbtn = tk.Button(storytxt2,text='剪刀',font=('標楷體', 14),command=st)
   sissorbtn.place(x=270, y=100)
   stonebtn = tk.Button(storytxt2,text='石頭',font=('標楷體', 14),command=pa)
   stonebtn.place(x=405, y=100)
   guess2answer=tk.Label(storytxt2,font=('標楷體', 14),bg='lightcyan')
   guess2answer.place(x=250, y=150)
   guess2btn = tk.Button(storytxt2,text='猜拳',font=('標楷體', 14),command=guess2)
   guess2btn.place(x=250, y=200)
   sbtn2 = tk.Button(storytxt2,text='記憶碎片',font=('標楷體', 14),command=dis2,state= DISABLED)
   sbtn2.place(x=250, y=300)
   storytxt2.resizable(0,0)
   storytxt2.mainloop()
def si():
   x.set(1)
   paperbtn["state"] = DISABLED
   sissorbtn["state"] = DISABLED
   stonebtn["state"] = DISABLED
def st():
   x.set(2)
   paperbtn["state"] = DISABLED
   sissorbtn["state"] = DISABLED
   stonebtn["state"] = DISABLED
def pa():
   x.set(3)
   paperbtn["state"] = DISABLED
   sissorbtn["state"] = DISABLED
   stonebtn["state"] = DISABLED
def guess2():
   y=random.randint(1,3)
   X=x.get()
   paperbtn["state"] = ACTIVE
   sissorbtn["state"] = ACTIVE
   stonebtn["state"] = ACTIVE
   if(y==1):
      computer['text']='對手:布'
   elif(y==2 ):
      computer['text']='對手:剪刀'
   else:
      computer['text']='對手:石頭'
   if(X==y):
      guess2answer['text']='平手'
   elif((X==1 and y==2) or(X==2 and y==3) or(X==3 and y==1) ):
      guess2answer['text']='輸'
   else:
      guess2answer['text']='贏'
      count2.set(count2.get()+1)
      counttext['text']=int(count2.get())
   if(count2.get()>=3):
      sbtn2["state"] = ACTIVE
      guess2btn["state"] = DISABLED
# 
def story3():
   opendiary()
   global storytxt3,count3,storytxt32,sbtn3,book1btn,book2btn,book3btn
   count3=IntVar()
   storytxt3 = tk.Toplevel()
   storytxt3.title('夢境')
   storytxt3.geometry('629x416')
   storytxt31=tk.Label(storytxt3,text='找出\n三本書',font=('標楷體', 12))
   storytxt31.place(x=10, y=10)
   storytxt32=tk.Label(storytxt3,font=('標楷體', 12))
   storytxt32.place(x=10, y=50)
   storytxt3pic1=tk.PhotoImage(file='AnyConv.com__roomfind.gif')
   storytxt3pic=tk.Label(storytxt3,image=storytxt3pic1)
   storytxt3pic.pack()
   book1=tk.PhotoImage(file='AnyConv.com__book1.gif')
   book1btn = tk.Button(storytxt3,text='',font=('標楷體', 14),command=book11,image=book1,bd=0)
   book1btn.place(x=485, y=160)
   book2=tk.PhotoImage(file='AnyConv.com__book2.gif')
   book2btn = tk.Button(storytxt3,text='',font=('標楷體', 14),command=book21,image=book2,bd=0)
   book2btn.place(x=105, y=185)
   book3=tk.PhotoImage(file='AnyConv.com__book3.gif')
   book3btn = tk.Button(storytxt3,text='',font=('標楷體', 14),command=book31,image=book3,bd=0)
   book3btn.place(x=345, y=250)
   sbtn3 = tk.Button(storytxt3,text='記憶碎片',font=('標楷體', 14),command=dis3,height = 1, width = 7,state= DISABLED)
   sbtn3.place(x=300, y=350)
   storytxt3.resizable(0,0)
   storytxt3.mainloop()
def book11():
   count3.set(count3.get()+1)
   storytxt32['text']=int(count3.get())
   if(count3.get()==3):
      sbtn3['state']=ACTIVE
   book1btn['state']=DISABLED
def book21():
   count3.set(count3.get()+1)
   storytxt32['text']=int(count3.get())
   if(count3.get()==3):
      sbtn3['state']=ACTIVE
   book2btn['state']=DISABLED
def book31():
   count3.set(count3.get()+1)
   storytxt32['text']=int(count3.get())
   if(count3.get()==3):
      sbtn3['state']=ACTIVE
   book3btn['state']=DISABLED
# 
def story4():
   opendiary()
   global storytxt4,HIT1,scoreTEXT,sbtn4,mousebtn,mousebtn2,mousebtn3,mousebtn4,mousebtn5,mousebtn6,mousepic,EMPTY,timedone,tIMETEXT2,startbtn
   HIT1=IntVar()
   timedone=IntVar()
   storytxt4 = tk.Toplevel()
   storytxt4.title('夢碎')
   storytxt4.geometry('500x450')
   labelback_hit=tk.Label(storytxt4,bg='lightcyan',height=500,width=450)
   labelback_hit.place(x=0, y=0)
   TIMETEXT1=tk.Label(storytxt4,text='打到9次就解鎖',bg='lightcyan',font=('標楷體', 12))
   TIMETEXT1.place(x=10, y=50)
   tIMETEXT2=tk.Label(storytxt4,font=('標楷體', 12),bg='lightcyan')
   tIMETEXT2.place(x=300, y=50)
   tIMETEXT3=tk.Label(storytxt4,text='秒',font=('標楷體', 12),bg='lightcyan')
   tIMETEXT3.place(x=350, y=50)
   scoreTEXT=tk.Label(storytxt4,font=('標楷體', 12),bg='lightcyan')
   scoreTEXT.place(x=400, y=50)
   tIMETEXT4=tk.Label(storytxt4,text='分',font=('標楷體', 12),bg='lightcyan')
   tIMETEXT4.place(x=420, y=50)
   mousepic=tk.PhotoImage(file='hit.gif')
   EMPTY=tk.PhotoImage(file='EMPTY.gif')
   mousebtn = tk.Button(storytxt4,text='',font=('標楷體', 14),bg='lightcyan',command=hit,bd=0,state= DISABLED)
   mousebtn.place(x=100, y=160)
   mousebtn2 = tk.Button(storytxt4,text='',font=('標楷體', 14),bg='lightcyan',command=hit,bd=0,state= DISABLED)
   mousebtn2.place(x=200, y=160)
   mousebtn3 = tk.Button(storytxt4,text='',font=('標楷體', 14),bg='lightcyan',command=hit,bd=0,state= DISABLED)
   mousebtn3.place(x=300, y=160)
   mousebtn4 = tk.Button(storytxt4,text='',font=('標楷體', 14),bg='lightcyan',command=hit,bd=0,state= DISABLED)
   mousebtn4.place(x=100, y=210)
   mousebtn5 = tk.Button(storytxt4,text='',font=('標楷體', 14),bg='lightcyan',command=hit,bd=0,state= DISABLED)
   mousebtn5.place(x=200, y=210)
   mousebtn6 = tk.Button(storytxt4,text='',font=('標楷體', 14),bg='lightcyan',command=hit,bd=0,state= DISABLED)
   mousebtn6.place(x=300, y=210)
   startbtn = tk.Button(storytxt4,text='start',font=('標楷體', 14),command=starthit)
   startbtn.place(x=210, y=260)
   sbtn4 = tk.Button(storytxt4,text='記憶碎片',font=('標楷體', 14),command=dis4,height = 1, width = 7,state= DISABLED)
   sbtn4.place(x=200, y=400)
   storytxt4.resizable(0,0)
   storytxt4.mainloop()
def hit():
   HIT1.set(HIT1.get()+1)
   scoreTEXT['text']=int(HIT1.get())
   if(HIT1.get()>=9):
      sbtn4['state']=ACTIVE
def starthit():
   HIT1.set(0)
   scoreTEXT['text']=int(HIT1.get())
   timedone.set(20)
   starthit1()
def starthit1():
   if (timedone.get()!=0):
      startbtn['state']=DISABLED
      storytxt4.after(1000, starthit1)
      timedone.set(timedone.get()-1)
      countdone()
   else:
      startbtn['state']=ACTIVE
      mousebtn['state']=DISABLED
      mousebtn2['state']=DISABLED
      mousebtn3['state']=DISABLED
      mousebtn4['state']=DISABLED
      mousebtn5['state']=DISABLED
      mousebtn6['state']=DISABLED
      mousebtn['image']=EMPTY
      mousebtn2['image']=EMPTY
      mousebtn3['image']=EMPTY
      mousebtn4['image']=EMPTY
      mousebtn5['image']=EMPTY
      mousebtn6['image']=EMPTY
def countdone():
   t=random.randint(1,6)
   tIMETEXT2['text']=int(timedone.get())
   mousebtn['state']=DISABLED
   mousebtn2['state']=DISABLED
   mousebtn3['state']=DISABLED
   mousebtn4['state']=DISABLED
   mousebtn5['state']=DISABLED
   mousebtn6['state']=DISABLED
   mousebtn['image']=EMPTY
   mousebtn2['image']=EMPTY
   mousebtn3['image']=EMPTY
   mousebtn4['image']=EMPTY
   mousebtn5['image']=EMPTY
   mousebtn6['image']=EMPTY
   if(t==1):
     mousebtn['state']=ACTIVE
     mousebtn['image']=mousepic
   if(t==2):
      mousebtn2['state']=ACTIVE
      mousebtn2['image']=mousepic
   if(t==3):
      mousebtn3['state']=ACTIVE
      mousebtn3['image']=mousepic
   if(t==4):
      mousebtn4['state']=ACTIVE
      mousebtn4['image']=mousepic
   if(t==5):
      mousebtn5['state']=ACTIVE
      mousebtn5['image']=mousepic
   if(t==6):
      mousebtn6['state']=ACTIVE
      mousebtn6['image']=mousepic
#
def story5():
   opendiary()
   global storytxt5,yearentry,yearanswer,year1,sbtn5
   storytxt5 = tk.Toplevel()
   storytxt5.title('墜落')
   storytxt5.geometry('500x350')
   labelback_guess=tk.Label(storytxt5,image=back2,compound=CENTER)
   labelback_guess.place(x=0, y=0)
   label_year=tk.Label(storytxt5,text='你還記得是幾歲和他成為家人的?',font=('標楷體', 12),bg='lightcyan')
   label_year.place(x=170, y=100)
   yearentry = tk.Entry(storytxt5)
   yearentry.place(x=170, y=150)
   yearanswer=tk.Label(storytxt5,text='',font=('標楷體', 12),bg='lightcyan')
   yearanswer.place(x=170, y=200)
   year1 = tk.Button(storytxt5,text='輸入',font=('標楷體', 12),command=year,height = 1, width = 5)
   year1.place(x=210, y=250)
   sbtn5 = tk.Button(storytxt5,text='記憶碎片',font=('標楷體', 12),command=dis5,height = 1, width = 7,state=DISABLED)
   sbtn5.place(x=200, y=300) 
   storytxt5.resizable(0,0)
   storytxt5.mainloop()
def year():
   guessnum=int(yearentry.get())
   if(guessnum==9):
      yearanswer['text']='正確'
      sbtn5["state"] = ACTIVE
      year1["state"] = DISABLED
   else:
      yearanswer['text']='錯誤\n回去房子內尋找"日記"或"生日卡片"'
#結局
def end():
   global endtext
   endtext = tk.Toplevel()
   endtext.title('抉擇')
   endtext.geometry('600x200')
   labelback_guess=tk.Label(endtext,image=back2,compound=CENTER)
   labelback_guess.place(x=0, y=-1)
   endtextlabel=tk.Label(endtext,font=('標楷體', 12),text='拿回記憶之後\n對你過去的選擇\n你後悔嗎?\n用自己的生命作為復仇的代價',bg='lightcyan')
   endtextlabel.pack()
   end1 = tk.Button(endtext,text='我不後悔，但如果再來一次，我會選擇順應哥哥的心願，好好活下去',font=('標楷體', 12),command=end1_1)
   end1.place(x=50, y=140)
   end2 = tk.Button(endtext,text='我不後悔，我想要復仇，儘管他希望我活下去',font=('標楷體', 12),command=end1_2)
   end2.place(x=120, y=170)
   endtext.mainloop()
def end1_1():
   endbtn.destroy()
   global end1_1text
   endtext.destroy()
   end1_1text = tk.Toplevel()
   end1_1text.title('結局 1')
   end1_1text.geometry('300x200')
   endtext1_1label=tk.Label(end1_1text,font=('標楷體', 12),image=back,compound=CENTER,text='我回到了我大學的時候\n像個一般人一樣地活著\n我放棄了復仇\n安穩地度過了一生\n但\n這樣子的活著\n我真的開心嗎?')
   endtext1_1label.pack()
   end1_1text.resizable(0,0)
   end1_1text.mainloop()
def end1_2():
   endbtn.destroy()
   global end1_2text,end1_2_2btn
   endtext.destroy()
   end1_2text = tk.Toplevel()
   end1_2text.title('抉擇 2')
   end1_2text.geometry('580x120')
   labelback_guess=tk.Label(end1_2text,image=back2,compound=CENTER)
   labelback_guess.place(x=0, y=0)
   endtext1_2label=tk.Label(end1_2text,font=('標楷體', 12),text='那你\n還想再一次見到他嗎?',bg='lightcyan')
   endtext1_2label.pack()
   end1_2_1btn = tk.Button(end1_2text,text='想，我真的好想再一次見到他',font=('標楷體', 12),command=end1_2_1)
   end1_2_1btn.place(x=165, y=60)
   if(openend3.get()==1):
      end1_2_2btn = tk.Button(end1_2text,text='想，但，我希望這次可以改變，我想守護他 ',font=('標楷體', 12),command=end1_2_2)#,state=DISABLED
      end1_2_2btn.place(x=120, y=90)
   end1_2text.resizable(0,0)
   end1_2text.mainloop()
def end1_2_1():
   end1_2text.destroy()
   end1_2_1text = tk.Toplevel()
   end1_2_1text.title('結局 2')
   end1_2_1text.geometry('300x350')
   end1_2_1label=tk.Label(end1_2_1text,font=('標楷體', 12),image=back,compound=CENTER,text='我回到了9歲那年\n我和他成為家人的哪一年\n在這幾年中\n我十分的珍惜和他相處的每一刻\n我也時刻注意\n希望可以挽回這一切\n守住他的生命\n但\n有些事情果然是必然的\n在相同的一天\n上演了相同的情況\n而我也在之後走向了同樣的路\n只不過這一次\n有了經驗\n犧牲的人變少了\n這也算是很好的結局對吧\n我一邊陷入如同夢境般的死亡一邊想著')
   end1_2_1label.pack()
   end1_2_1text.resizable(0,0)
   end1_2_1text.mainloop()
def end1_2_2():
   end1_2text.destroy()
   end1_2_2text = tk.Toplevel()
   end1_2_2text.title('結局 3(true end)')
   end1_2_2text.geometry('300x550')
   end1_2_2label=tk.Label(end1_2_2text,font=('標楷體', 12),image=back,compound=CENTER,text='我回到了9歲那年\n我和他成為家人的哪一年\n在這幾年中\n我十分的珍惜和他相處的每一刻\n我也時刻注意\n希望可以挽回這一切\n守住他的生命\n但\n有些事情果然是必然的\n在相同的一天\n上演了相同的情況\n而我也在之後走向了同樣的路\n只不過這一次\n有了經驗\n犧牲的人變少了\n這也算是很好的結局對吧\n我一邊陷入如同夢境般的死亡一邊想著\n"起床了!!!你要遲到了!!!"\n聽見叫喚的我從夢中甦醒\n不明所以的來到了學校\n所有的記憶也逐漸回到腦海中\n原來現在的我是一位高中生\n有著和"夢中"相似的經歷背景\n父母雙亡、被人厭棄\n但不同的是\n他\n不再是我的"哥哥"\n我失神的在校園中走著\n直到被一個人撞到\n我抬頭一看\n他\n回來了')
   end1_2_2label.pack()
   end1_2_2text.resizable(0,0)
   end1_2_2text.mainloop()
#隨機生成位置的按鈕
btn1img=tk.PhotoImage(file='AnyConv.com__letterr.gif')
letimg=tk.PhotoImage(file='letterr.gif')
birthimg=tk.PhotoImage(file='AnyConv.com__birthday.gif')
audioimg=tk.PhotoImage(file='AnyConv.com__audio.gif')
dollimg=tk.PhotoImage(file='AnyConv.com__doll.gif')
diaryimg=tk.PhotoImage(file='AnyConv.com__diary.gif')
letter1=tk.Button(window,text='',bd=0,command=letter_1,image=letimg,compound='center')
letter1.place(x=150, y=514)
letter2=tk.Button(window,text='',bd=0,command=letter_2,image=letimg,compound='center')
letter2.place(x=590, y=410)
birthday=tk.Button(window,text='',bd=0,command=birthday_card,image=birthimg,compound='center')
birthday.place(x=110, y=190)
audio=tk.Button(window,text='',bd=0,command=audio1,image=audioimg,compound='center')
audio.place(x=570, y=445)
gift1=tk.Button(window,text='',bd=0,command=gift1text,image=dollimg,compound='center')
gift1.place(x=250, y=184)
diary1=tk.Button(window,text='',bd=0,command=diary1text,image=diaryimg,compound='center',state= DISABLED)
diary1.place(x=200, y=470)
diary2=tk.Button(window,text='',bd=0,command=diary2text,image=diaryimg,compound='center',state= DISABLED)
diary2.place(x=250, y=240)
diary3=tk.Button(window,text='',bd=0,command=diary3text,image=diaryimg,compound='center',state= DISABLED)#
diary3.place(x=160, y=140)
diary4=tk.Button(window,text='',bd=0,command=diary4text,image=diaryimg,compound='center',state= DISABLED)#
diary4.place(x=590, y=360)
btn1 = tk.Button(window,text='',font=('標楷體', 14),bd=0,image=btn1img,compound='center',command=story1,state= ACTIVE)
btn1.place(x=random.randint(50,660), y=random.randint(50,120))
btn2 = tk.Button(window, text='',font=('標楷體', 14),bd=0,command=story2,image=btn1img,compound='center')
btn2.place(x=random.randint(50,660), y=random.randint(100,200))
btn3 = tk.Button(window, text='',font=('標楷體', 14),bd=0,command=story3,image=btn1img,compound='center')
btn3.place(x=random.randint(50,660), y=random.randint(200,350))
btn4 = tk.Button(window, text='',font=('標楷體', 14),bd=0,command=story4,image=btn1img,compound='center')
btn4.place(x=random.randint(50,660), y=random.randint(350,480))
btn5 = tk.Button(window, text='',font=('標楷體', 14),bd=0,command=story5,image=btn1img,compound='center')
btn5.place(x=random.randint(50,660), y=random.randint(460,550))
endbtn = tk.Button(window, text='抉擇',font=('標楷體', 14),bd=0,command=end,height = 1, width = 3,state= DISABLED)#
endbtn.place(x=650, y=565)

# 開頭
past = tk.Toplevel()
past.title('我是誰?這裡是哪裡?')
past.geometry('280x158+300+300')
paper1=tk.PhotoImage(file="paper1.gif")
pasttext=tk.Label(past,font=('標楷體', 14),image=paper1,compound='center',text='你是一位迷失之人\n你需要通過一些考驗\n找尋所有的記憶碎片\n當找完所有碎片之時\n你會恢復記憶\n同時你必須做出選擇\n')
pasttext.pack()
past.mainloop()
# 運行主程式，循環常駐主視窗
window.mainloop()
