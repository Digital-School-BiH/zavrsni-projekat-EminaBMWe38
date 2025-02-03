from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random


def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    user_type = user_type_var.get()
    if user_type == "Teacher" and username == "teacher" and password == "password123":
        open_classroom(user_type)
    elif user_type == "Student" and username == "student" and password == "password123":
        open_classroom(user_type)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password!")


def open_classroom(user_type):
    global class_list
    login_window.destroy()
    classroom_window = tk.Tk()
    classroom_window.title("Google Classroom")
    classroom_window.geometry("800x600")

    def sign_out():
        classroom_window.destroy()
        main()

    def open_games():
        classroom_window.withdraw()
        show_games(classroom_window)

    menu_bar = Menu(classroom_window)
    classroom_window.config(menu=menu_bar)
    classroom_window.configure(bg="#cdd6f4")

    account_menu = Menu(menu_bar)
    account_menu.add_command(label="Sign Out", command=sign_out)
    account_menu.add_command(label="Games", command=open_games)
    menu_bar.add_cascade(label="Account", menu=account_menu)

    header_label = tk.Label(
        classroom_window,
        text=f"Welcome to Google Classroom ({user_type})",
        font=("Courier New", 25)
    )
    header_label.pack(pady=20)
    header_label.configure(bg="#cdd6f4")

    class_list= [
        {"title": "Math 101", "teacher": "Profesor matematike"},
        {"title": "Science 102", "teacher": "Profesorica hemije"},
        {"title": "P.E. 001", "teacher": "Profa tjelesnog"},
        {"title": "Programming 204", "teacher": "Profesorica programiranja"},
        {"title": "Religion 205", "teacher": "Profesorica vjeronauke"},
        {"title": "Bosnian 305", "teacher": "Profesor Bosanskog jezika"},
        {"title": "Physics 100", "teacher": "Profesorica fizike"},
        {"title": "English 212", "teacher": "Profesorica engleskog"},
        {"title": "German 210", "teacher": "Profesor njemačkog jezika"},
    ]

    colors = ["#8058aa", "#d7a0db", "#493ca6", "#a17dc7", "#e2bae5", "#6a5fbc", "#bc9fdb", "#ecd4ee", "#8f83e5"]

    class_label=tk.Label(classroom_window,
                           text="Classes:",
                           font=("Courier New", 16, "bold"),
                           bg="#cdd6f4")
    
    class_label.pack(pady=5)

    classes_frame=tk.Frame(classroom_window)
    classes_frame.pack(pady=10)
    classes_frame.configure(bg="#cdd6f4")

def open_classroom(user_type):
    global class_list
    login_window.destroy()
    classroom_window = tk.Tk()
    classroom_window.title("Google Classroom")
    classroom_window.geometry("800x600")

    def sign_out():
        classroom_window.destroy()
        main()

    def open_games():
        classroom_window.withdraw()
        show_games(classroom_window)

    menu_bar = Menu(classroom_window)
    classroom_window.config(menu=menu_bar)
    classroom_window.configure(bg="#cdd6f4")

    account_menu = Menu(menu_bar)
    account_menu.add_command(label="Sign Out", command=sign_out)
    account_menu.add_command(label="Games", command=open_games)
    menu_bar.add_cascade(label="Account", menu=account_menu)

    header_label = tk.Label(
        classroom_window, text=f"Welcome to Google Classroom ({user_type})", font=("Courier New", 25)
    )
    header_label.pack(pady=20)
    header_label.configure(bg="#cdd6f4")

    class_list=[
        {"title": "Math 101", "teacher": "Profesor matematike", "tasks": []},
        {"title": "Science 102", "teacher": "Profesorica hemije", "tasks": []},
        {"title": "P.E. 001", "teacher": "Profa tjelesnog", "tasks": []},
        {"title": "Programming 204", "teacher": "Profesorica programiranja", "tasks": []},
        {"title": "Religion 205", "teacher": "Profesorica vjeronauke", "tasks": []},
        {"title": "Bosnian 305", "teacher": "Profesor Bosanskog jezika", "tasks": []},
        {"title": "Physics 100", "teacher": "Profesorica fizike", "tasks": []},
        {"title": "English 212", "teacher": "Profesorica engleskog", "tasks": []},
        {"title": "German 210", "teacher": "Profesor njemačkog jezika", "tasks": []},
    ]

    colors =["#8058aa", "#d7a0db", "#493ca6", "#a17dc7", "#e2bae5", "#6a5fbc", "#bc9fdb", "#ecd4ee", "#8f83e5"]

    class_label=tk.Label(classroom_window,
                         text="Classes:",
                         font=("Courier New", 16, "bold"),
                         bg="#cdd6f4")
    class_label.pack(pady=5)

    classes_frame=tk.Frame(classroom_window)
    classes_frame.pack(pady=10)
    classes_frame.configure(bg="#cdd6f4")

    def open_class_window(class_info):
        class_window=tk.Toplevel(classroom_window)
        class_window.title(class_info["title"])
        class_window.geometry("400x400")

        class_title_label= tk.Label(
            class_window,
            text=class_info["title"],
            font=("Courier New", 30, "bold"),
            bg="#cdd6f4"
        )
        class_title_label.pack(pady=20)

        teacher_label=tk.Label(
            class_window, text=f"Teacher: {class_info['teacher']}", font=("Courier New", 16), bg="#cdd6f4"
        )
        teacher_label.pack(pady=10)


        if user_type=="Teacher":
            def add_task():
                task_window = tk.Toplevel(class_window)
                task_window.title("Add New Task")
                task_window.geometry("400x300")

                task_label = tk.Label(
                    task_window,
                    text="Enter Task Description:",
                    font=("Courier New", 16),
                    bg="#cdd6f4"
                )
                task_label.pack(pady=20)

                task_entry =tk.Entry(task_window,
                                      font=("Courier New", 16),
                                      width=30)
                task_entry.pack(pady=10)

                def save_task():
                    task_description=task_entry.get()
                    if task_description:
                        class_info["tasks"].append(task_description)
                        update_task_list(class_info)
                        task_window.destroy()
                    else:
                        messagebox.showerror("Error", "Fill in the description!")

                save_button=tk.Button(
                    task_window, text="Save Task", font=("Courier New", 14), command=save_task
                )
                save_button.pack(pady=10)

            add_task_button= tk.Button(
                class_window, text="Add Task", font=("Courier New", 14), command=add_task
            )
            add_task_button.pack(pady=10)


        task_label=tk.Label(
            class_window, text="Tasks:", font=("Courier New",16), bg="#cdd6f4"
        )
        task_label.pack(pady=10)

        task_listbox =tk.Listbox(
            class_window, font=("Courier New", 14), height=6, width=40, selectmode="single"
        )
        task_listbox.pack(pady=10)

        def update_task_list(class_info):

            task_listbox.delete(0, tk.END)
            for task in class_info["tasks"]:
                task_listbox.insert(tk.END, task)

        update_task_list(class_info)

    for index, class_info in enumerate(class_list):
        color = colors[index % len(colors)]

        class_frame = tk.Frame(
            classes_frame,
            borderwidth=0,
            relief="flat",
            padx=20,
            pady=10,
            bg=color
        )
        class_frame.grid(row=index // 3, column=index % 3, padx=15, pady=15)

        class_title = tk.Label(
            class_frame,
            text=class_info["title"],
            font=("Courier New", 20, "bold"),
            bg=color
        )
        class_title.pack()

        class_teacher = tk.Label(
            class_frame,
            text=f"Teacher: {class_info['teacher']}",
            font=("Courier New", 15),
            bg=color
        )
        class_teacher.pack()

        open_button = tk.Button(
            class_frame,
            text=" ",
            command=lambda ci=class_info: open_class_window(ci),
            width=50,
            height=3,
            font=("Arial", 10),
            relief='flat',
            borderwidth=3,
            bg="white",
            fg="white"
        )
        open_button.pack(pady=5)

    classroom_window.mainloop()






    
def show_games(parent_window):
    games_window = tk.Toplevel()
    games_window.title("Games")
    games_window.geometry("800x600")
    games_window.configure(bg="#cdd6f4")

    header_label = tk.Label(
        games_window, text="Choose a Game to Play", font=("Courier New", 25), bg="#cdd6f4"
    )
    header_label.pack(pady=20)


    def play_game(game_name):
        if game_name == "Snake Game":
            start_snake_game()
        elif game_name == "Tic Tac Toe":
            start_tic_tac_toe()

    def start_tic_tac_toe():
        ttt_window= tk.Toplevel()
        ttt_window.title("Tic Tac Toe")
        ttt_window.geometry("400x400")
        ttt_window.configure(bg="#cdd6f4")

        ttt_frame = tk.Frame(ttt_window, bg="#cdd6f4")
        ttt_frame.pack(expand=True)

        board = ["" for _ in range(9)]
        current_player = ["X"]    

        def check_winner():
            winning_combinations = [
                (0, 1, 2), (3, 4, 5), (6, 7, 8),  
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                (0, 4, 8), (2, 4, 6)             
            ]
            for combo in winning_combinations:
                if board[combo[0]]==board[combo[1]]== board[combo[2]]!="":
                    return board[combo[0]]
            if "" not in board:
                return "Draw"
            return None

        def button_click(index):
            if board[index]== "" and check_winner() is None:
                board[index]=current_player[0]
                buttons[index].config(text=current_player[0])
                winner=check_winner()
                if winner:
                    result_label.config(text=f"Winner: {winner}" if winner!= "Draw" else "It's a Draw!")
                else:
                    current_player[0] = "O" if current_player[0] == "X" else "X"

        buttons= []
        for i in range(9):
            btn=tk.Button(ttt_frame,
                          text="",
                          font=("Courier New", 20),
                          width=5,
                          height=2,
                            command=lambda i=i: button_click(i),
                          bg="#f0f0f0",
                          relief="groove")

            
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            buttons.append(btn)

        result_label = tk.Label(ttt_frame, text="", font=("Courier New", 16), bg="#cdd6f4")
        result_label.grid(row=3, column=0, columnspan=3, pady=10)




    games_frame= tk.Frame(games_window, bg="#cdd6f4")
    games_frame.pack(pady=20)

    games =[
        {"name": "Tic Tac Toe", "image": "tic.png"},
    ]

    for game in games:
        frame = tk.Frame(games_frame,
                         bg="#e6e6fa",
                         padx=10, pady=10,
                         relief="groove",
                         borderwidth=2)
        frame.pack(pady=10, padx=10)

        image = Image.open(game["image"])
        image =image.resize((200, 200))
        img= ImageTk.PhotoImage(image)
        img_label = tk.Label(frame, image=img, bg="#e6e6fa")
        img_label.image =img
        img_label.pack(side="left", padx=10)

        details_frame=tk.Frame(frame, bg="#e6e6fa")
        details_frame.pack(side="left",
                           padx=10,
                           fill="x",
                           expand=True)

        title_label=tk.Label(details_frame,
                               text=game["name"],
                               font=("Courier New", 18, "bold"),
                               bg="#e6e6fa")
        title_label.pack(anchor="w")

        play_button= tk.Button(
            details_frame,
            text="Play",
            font=("Courier New", 14),
            command=lambda g=game["name"]: play_game(g)
        )
        play_button.pack(anchor="w", pady=5)





    def back_to_classroom():
        games_window.destroy()
        parent_window.deiconify()

    back_button = tk.Button(
        games_window,
        text="Back",
        font=("Courier New", 14),
        command=back_to_classroom
    )
    back_button.pack(pady=10)

def main():
    global login_window, username_entry, password_entry, user_type_var

    login_window= tk.Tk()
    login_window.title("Login - Google Classroom")
    login_window.geometry("1920x1200")

    image=Image.open("bg6.png")
    image = image.resize((1800, 1100))
    background_image =ImageTk.PhotoImage(image)

    background_label = tk.Label(login_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    header_label = tk.Label(
        login_window,
        text="Google Classroom Login",
        font=("Courier New", 40, "bold"),
        bg="#82b4f9",
        fg="#372c70"
    )
    header_label.pack(pady=100)

    username_label = tk.Label(login_window, text="Username:",
                              font=("Courier New", 20),
                              bg="#9cb5f6",
                              fg="#372c70")


    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window,
                              font=("Courier New", 20))

    
    username_entry.pack(pady=5)

    password_label = tk.Label(login_window,
                              text="Password:",
                              font=("Courier New", 20),
                              bg="#ccd7fd", fg="#372c70")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window,
                              show="*",
                              font=("Courier New", 20))

    
    password_entry.pack(pady=5)

    user_type_var=tk.StringVar(value="Student")

    student_radio =tk.Radiobutton(
        login_window,
        text="Student",
        variable=user_type_var,
        value="Student",
        font=("Courier New", 20),
        bg="#f6f5fb",
        fg="#372c70",
        indicatoron=False
    )
    student_radio.pack(pady=5)

    teacher_radio= tk.Radiobutton(
        login_window,
        text="Teacher",
        variable=user_type_var,
        value="Teacher",
        font=("Courier New", 20),
        bg="#f6f5fb",
        fg="#372c70",
        indicatoron=False
    )
    teacher_radio.pack()

    def on_enter(e):
        login_button['background']= "#ce8fd7"

    def on_leave(e):
        login_button['background']='SystemButtonFace'

    login_button= tk.Button(
        login_window,
        text="SIGN IN",
        font=("Courier New", 18),
        height=1,
        width=9,
        relief="groove",
        borderwidth=2,
        command=validate_login
    )
    
    login_button.bind("<Enter>", on_enter)
    login_button.bind("<Leave>", on_leave)
    login_button.pack(pady=20)

    login_window.mainloop()


main()
