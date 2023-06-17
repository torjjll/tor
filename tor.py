import customtkinter

app = customtkinter.CTk()
app.title('พรี่ต้องยอดนักเซกกกก')
app.geometry('500x500')

#ข้อความแสดงงผล
label = customtkinter.CTkLabel(app, text="อ้ายต้องยอดชาย", fg_color='transparent', font=('Aris' , 40))
label.pack(pady=(20, 0))

#แสดงคำตอบ
answer_text = customtkinter.StringVar()
answer_label = customtkinter.CTkLabel(app, textvariable = answer_text, font=('Aria' , 20))
answer_label.pack(pady=(30, 0))

#กล่องรับค่า input
entry = customtkinter.CTkEntry(app, placeholder_text="ใส่ชื่อมึงตรงนี้")
entry.pack(pady=(15, 0))

#ปุ่มกดโง่ๆ
def button_event():
    user_input = entry.get()
    if user_input == ('ต้อง'):
        answer = str(user_input), "คนเชี้ยไรเซ้กตัวเอง"
    elif user_input == ('ไอซ์'):
        answer = str(user_input), "น่าเกลียดเกินไม่อยากเซ้ก"
    elif user_input == ('ข้าวปั้น'):
        answer = str(user_input), "ไอต้องโดนสวนตูดเพราะข้าวปั้นเกเกิน"
    else:
        answer = str(user_input), "มึงโดนไอต้องจ้องจะเซ้กก"
    answer_text.set(answer)
    print(user_input, answer)


button = customtkinter.CTkButton(app, text="กดกูดิ" , command =button_event ,fg_color='blue')
button.pack(pady=(20, 0))

app.mainloop()
