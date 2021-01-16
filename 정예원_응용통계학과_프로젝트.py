import tkinter as tk
from tkinter import *
import tkinter.messagebox as msbox
import requests
from bs4 import BeautifulSoup
from tkinter import font

root = tk.Tk()
root.title("정예원 GUI")
root.geometry("860x640")
root.resizable(False, False)

background_image = tk.PhotoImage(file = "C:/Users/ninay/Desktop/pythonworkspace/gui_project/my_project/hamburger_store12.png")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight=1)

label1 = Label(root, text = "안녕하세요^0^ 행복한 예원쓰 햄버거 입니당~ 주문 종류를 선택하세요.", bg = "skyblue", font=("Modern", 20)) 
label1.pack()


############# 주문하기 #####################

def order():
    if sum(list_file.get(0,END)) == 0:
        msbox.showwarning("경고", "주문 메뉴를 선택해주세요")
    else:
        response = msbox.askyesnocancel(title = "주문확인", message = "총 주문 금액은 {0} 원 입니다. \n 주문 하시겠습니까?".format(sum(list_file.get(0,END))))   
        
        if response == 1: # 네, ok
            print("주문확인")
            print("총 결제금액 : ", sum(list_file.get(0,END)))
            msbox.showinfo("알림", "정상적으로 주문 완료되었습니다.")
            list_file.delete(0, END)
        elif response ==0:
            print("아니오")
            msbox.showinfo("알림", "주문이 취소되었습니다.")
            list_file.delete(0, END)
        else:
            print("취소")
            list_file.delete(0, END)



############################ 주문 목록 ###############################

# 주문목록에 추가

def add_order():
    order_menu=[]
    order_menu.append(burger_var.get()+side_var.get()+drink_var.get())
    
    for menu in order_menu:
        list_file.insert(END, menu)


# 주문목록에 삭제

def del_order():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)




# 주문 버튼
btn_order = Button(root, text = "주문하기", font=25, bg = "red", command=order)
btn_order.pack(side="bottom", pady=5)

# 주문 목록에 추가 버튼
btn_add = Button(root, text = "주문 추가", font=25, bg = "yellow", command=add_order)
btn_add.pack(side="bottom", pady=5)

# 주문 목록 취소 버튼
btn_order = Button(root, text = "주문 삭제", font=25, bg = "orange", command=del_order)
btn_order.pack(side="bottom", pady=5)


############### 리스트 프레임 ####################
list_frame = LabelFrame(root, text="주문 가격", font=20, bg="yellow")
list_frame.pack(fill="both", padx=5, pady=15)  

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)







################# 햄버거 메뉴 프레임  ####################
frame_burger = LabelFrame(root, text="햄버거 메뉴를 선택해 주세요", font=10, bg="white")
frame_burger.pack(side = "left",expand = True, padx = 5)


url1 = "http://www.lotteria.com/menu/MenuList.asp?C2=4"
req = requests.get(url1)
soup = BeautifulSoup(req.text, "html.parser")
txt = soup.find("div", attrs = {"class","memu_group"}).get_text()



# 햄버거 메뉴 버튼 생성
burger_var= IntVar()

menu_burger1 = txt.split("\n")[15 : 18]
btn_burger1 = Radiobutton(frame_burger, text = menu_burger1[0]+"  "+menu_burger1[2], value=int(menu_burger1[2][0]+menu_burger1[2][2:5]), variable=burger_var)
btn_burger1.select()
btn_burger1.pack()

menu_burger2 = txt.split("\n")[36 : 39]
btn_burger2 = Radiobutton(frame_burger, text = menu_burger2[0]+"  "+menu_burger2[2], value=int(menu_burger2[2][0]+menu_burger2[2][2:5]), variable=burger_var)
btn_burger2.pack()

menu_burger3 = txt.split("\n")[57 : 60]
btn_burger3 = Radiobutton(frame_burger, text = menu_burger3[0]+"  "+menu_burger3[2], value=int(menu_burger3[2][0]+menu_burger3[2][2:5]), variable=burger_var)
btn_burger3.pack()

menu_burger4 = txt.split("\n")[78 : 81]
btn_burger4 = Radiobutton(frame_burger, text = menu_burger4[0]+"  "+menu_burger4[2], value=int(menu_burger4[2][0]+menu_burger4[2][2:5]), variable=burger_var)
btn_burger4.pack()

menu_burger5 = txt.split("\n")[119 : 122]
btn_burger5 = Radiobutton(frame_burger, text = menu_burger5[0]+"  "+menu_burger5[2], value=int(menu_burger5[2][0]+menu_burger5[2][2:5]), variable=burger_var)
btn_burger5.pack()


btn_burger7 = Radiobutton(frame_burger, text = "주문안함", value=0, variable=burger_var)
btn_burger7.pack()




################# 사이드 메뉴 프레임  ####################

frame_side = LabelFrame(root, text="사이드 메뉴를 선택해 주세요", font=10, bg="white")
frame_side.pack(side = "left",  expand = True, padx = 5)


url2 = "http://www.lotteria.com/menu/MenuList.asp?C2=6"
req = requests.get(url2)
soup = BeautifulSoup(req.text, "html.parser")
txt = soup.find("div", attrs = {"class","memu_group"}).get_text()

# 사이드 메뉴 버튼 생성
side_var= IntVar()

menu_side1 = txt.split("\n")[15 : 18]
btn_side1 = Radiobutton(frame_side, text = menu_side1[0]+"  "+menu_side1[2], value=int(menu_side1[2][0]+menu_side1[2][2:5]), variable=side_var)
btn_side1.select()
btn_side1.pack()

menu_side2 = txt.split("\n")[36 : 39]
btn_side2 = Radiobutton(frame_side, text = menu_side2[0]+"  "+menu_side2[2], value=int(menu_side2[2][0]+menu_side2[2][2:5]), variable=side_var)
btn_side2.pack()

menu_side3 = txt.split("\n")[57 : 60]
btn_side3 = Radiobutton(frame_side, text = menu_side3[0]+"  "+menu_side3[2], value=int(menu_side3[2][0]+menu_side3[2][2:5]), variable=side_var)
btn_side3.pack()

menu_side4 = txt.split("\n")[78 : 81]
btn_side4 = Radiobutton(frame_side, text = menu_side4[0]+"  "+menu_side4[2], value=int(menu_side4[2][0]+menu_side4[2][2:5]), variable=side_var)
btn_side4.pack()

menu_side5 = txt.split("\n")[98 : 101]
btn_side5 = Radiobutton(frame_side, text = menu_side5[0]+"  "+menu_side5[2], value=int(menu_side5[2][0]+menu_side5[2][2:5]), variable=side_var)
btn_side5.pack()

menu_side6 = txt.split("\n")[118 : 121]
btn_side6 = Radiobutton(frame_side, text = menu_side6[0]+"  "+menu_side6[2], value=int(menu_side6[2][0]+menu_side6[2][2:5]), variable=side_var)
btn_side6.pack()

btn_side7 = Radiobutton(frame_side, text = "주문안함", value=0, variable=side_var)
btn_side7.pack()




################# 드링크 메뉴 프레임  ####################

frame_drink = LabelFrame(root, text="드링크 메뉴를 선택해 주세요", font=10, bg="white")
frame_drink.pack(side = "left",  expand = True, padx = 5)


url3 = "http://www.lotteria.com/menu/MenuList.asp?C2=7"
req = requests.get(url3)
soup = BeautifulSoup(req.text, "html.parser")
txt = soup.find("div", attrs = {"class","memu_group"}).get_text()

# 사이드 메뉴 버튼 생성
drink_var= IntVar()

menu_drink1 = txt.split("\n")[15 : 18]
btn_drink1 = Radiobutton(frame_drink, text = menu_drink1[0]+"  "+menu_drink1[2], value=int(menu_drink1[2][0]+menu_drink1[2][2:5]), variable=drink_var)
btn_drink1.select()
btn_drink1.pack()

menu_drink2 = txt.split("\n")[35 : 38]
btn_drink2 = Radiobutton(frame_drink, text = menu_drink2[0]+"  "+menu_drink2[2], value=int(menu_drink2[2][0]+menu_drink2[2][2:5]), variable=drink_var)
btn_drink2.pack()

menu_drink3 = txt.split("\n")[55 : 58]
btn_drink3 = Radiobutton(frame_drink, text = menu_drink3[0]+"  "+menu_drink3[2], value=int(menu_drink3[2][0]+menu_drink3[2][2:5]), variable=drink_var)
btn_drink3.pack()

menu_drink5 = txt.split("\n")[95 : 98]
btn_drink5 = Radiobutton(frame_drink, text = menu_drink5[0]+"  "+menu_drink5[2], value=int(menu_drink5[2][0]+menu_drink5[2][2:5]), variable=drink_var)
btn_drink5.pack()

menu_drink6 = txt.split("\n")[115 : 118]
btn_drink6 = Radiobutton(frame_drink, text = menu_drink6[0]+"  "+menu_drink6[2], value=int(menu_drink6[2][0]+menu_drink6[2][2:5]), variable=drink_var)
btn_drink6.pack()


btn_drink7 = Radiobutton(frame_drink, text = "주문안함", value=0, variable=drink_var)
btn_drink7.pack()




root.mainloop()




#############################3

