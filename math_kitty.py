import tkinter as tk
import random

root = tk.Tk()
root.title("Математика і котики")
root.geometry("880x810")
root.resizable(False, False)

# Розміщення вікна в центрі екрану
root.update_idletasks()
window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)
root.geometry(f"880x810+{x_coordinate}+{y_coordinate}")

icon_path = "icon_img.png"
background_path = "background_img.png"
logo_path = "logo_cat.png"

icon_image = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon_image)

background_image = tk.PhotoImage(file=background_path)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0)

logo_image = tk.PhotoImage(file=logo_path)
logo_label = tk.Label(root, image=logo_image)
logo_label.place(x=680, y=450)


# Рамки для операцій додавання, віднімання, множення та результатів
def create_frame(root, bg_color, x, y, text, font="Times 16"):
    frame = tk.Frame(root, bg=bg_color, bd=2)
    frame.place(x=x, y=y)
    label = tk.Label(frame, text=text, fg="yellow", bg="salmon", font=font)
    label.pack()
    return frame


frame_addition = create_frame(
    root, "orange", 240, 10, "Додавання, натисни 'Далі ==>', щоб розпочати"
)
frame_subtraction = create_frame(
    root, "orange", 240, 160, "Віднімання, натисни 'Далі ==>', щоб розпочати"
)
frame_multiplication = create_frame(
    root, "orange", 240, 310, "Множення, натисни 'Далі ==>', щоб розпочати"
)
frame_results_text = create_frame(
    root, "orange", 95, 450, "Результати відповідей:", font="Times 16"
)

# Рамка для результатів(score)
result_frame = tk.Frame(root, bg="orange", bd=2)
result_frame.place(x=320, y=450)
result_label = tk.Label(result_frame, fg="yellow", bg="salmon", font="Times 16")
result_label.pack()

score = 0


# Функції для додавання
def check_addition():
    addition_result_label["text"] = verify_addition()


def verify_addition():
    expected_result = number_a + number_b
    user_result = int(addition_entry.get())
    return "ВІРНО" if user_result == expected_result else "НЕ ВІРНО"


def start_addition():
    global number_a, number_b, score

    if addition_result_label["text"] == "ВІРНО":
        score += 1
    elif addition_result_label["text"] == "НЕ ВІРНО":
        score -= 1

    update_display()
    number_a = random.randint(100, 1000)
    number_b = random.randint(10, 100)
    addition_label["text"] = f"{number_a} + {number_b} = "


# Функції для віднімання
def check_subtraction():
    subtraction_result_label["text"] = verify_subtraction()


def verify_subtraction():
    expected_result = (
        number_a - number_b if number_a > number_b else number_b - number_a
    )
    user_result = int(subtraction_entry.get())
    return "ВІРНО" if user_result == expected_result else "НЕ ВІРНО"


def start_subtraction():
    global number_a, number_b, score

    if subtraction_result_label["text"] == "ВІРНО":
        score += 1
    elif subtraction_result_label["text"] == "НЕ ВІРНО":
        score -= 1

    update_display()
    number_a = random.randint(100, 1000)
    number_b = random.randint(10, 100)
    subtraction_label["text"] = (
        f"{number_a} - {number_b} = "
        if number_a > number_b
        else f"{number_b} - {number_a} = "
    )


# Функції для множення
def check_multiplication():
    multiplication_result_label["text"] = verify_multiplication()


def verify_multiplication():
    expected_result = number_a * number_b
    user_result = int(multiplication_entry.get())
    return "ВІРНО" if user_result == expected_result else "НЕ ВІРНО"


def start_multiplication():
    global number_a, number_b, score

    if multiplication_result_label["text"] == "ВІРНО":
        score += 1
    elif multiplication_result_label["text"] == "НЕ ВІРНО":
        score -= 1

    update_display()
    number_a = random.randint(2, 10)
    number_b = random.randint(2, 10)
    multiplication_label["text"] = f"{number_a} * {number_b} = "


# Оновлення дисплею та скидання полів
def update_display():
    result_label["text"] = score
    addition_entry.delete(0, tk.END)
    subtraction_entry.delete(0, tk.END)
    multiplication_entry.delete(0, tk.END)
    addition_label["text"] = "(^_^)"
    subtraction_label["text"] = "(^_^)"
    multiplication_label["text"] = "(^_^)"
    addition_result_label["text"] = ""
    subtraction_result_label["text"] = ""
    multiplication_result_label["text"] = ""


# Створення елементів для додавання
addition_frame = tk.Frame(root, bg="deep sky blue", bd=5)
addition_frame.place(x=95, y=50)
addition_label = tk.Label(
    addition_frame, text="(^_^)", fg="white", bg="hotpink3", font="Times 22"
)
addition_label.pack()

addition_entry_frame = tk.Frame(root, bg="deep sky blue", bd=5)
addition_entry_frame.place(x=240, y=50)
addition_entry = tk.Entry(
    addition_entry_frame, width=3, fg="white", bg="hotpink3", font="Times 23"
)
addition_entry.pack()

addition_button_frame = tk.Frame(root, bg="deep sky blue", bd=5)
addition_button_frame.place(x=310, y=50)
addition_button = tk.Button(
    addition_button_frame,
    text="Відповідь",
    bg="hotpink1",
    fg="white",
    font="Times 16",
    command=check_addition,
)
addition_button.pack()

addition_result_frame = tk.Frame(root, bg="deep sky blue", bd=5)
addition_result_frame.place(x=450, y=50)
addition_result_label = tk.Label(
    addition_result_frame, fg="white", bg="hotpink3", font="Times 22"
)
addition_result_label.pack()

addition_next_button_frame = tk.Frame(root, bg="light pink", bd=6)
addition_next_button_frame.place(x=610, y=50)
addition_next_button = tk.Button(
    addition_next_button_frame,
    text="Далі ==>",
    bg="hotpink1",
    fg="white",
    font="Times 16",
    command=start_addition,
)
addition_next_button.pack()

# Створення елементів для віднімання
subtraction_frame = tk.Frame(root, bg="deep sky blue", bd=5)
subtraction_frame.place(x=95, y=200)
subtraction_label = tk.Label(
    subtraction_frame, text="(^_^)", fg="white", bg="hotpink3", font="Times 22"
)
subtraction_label.pack()

subtraction_entry_frame = tk.Frame(root, bg="deep sky blue", bd=5)
subtraction_entry_frame.place(x=240, y=200)
subtraction_entry = tk.Entry(
    subtraction_entry_frame, width=3, fg="white", bg="hotpink3", font="Times 23"
)
subtraction_entry.pack()

subtraction_button_frame = tk.Frame(root, bg="deep sky blue", bd=5)
subtraction_button_frame.place(x=310, y=200)
subtraction_button = tk.Button(
    subtraction_button_frame,
    text="Відповідь",
    bg="hotpink1",
    fg="white",
    font="Times 16",
    command=check_subtraction,
)
subtraction_button.pack()

subtraction_result_frame = tk.Frame(root, bg="deep sky blue", bd=5)
subtraction_result_frame.place(x=450, y=200)
subtraction_result_label = tk.Label(
    subtraction_result_frame, fg="white", bg="hotpink3", font="Times 22"
)
subtraction_result_label.pack()

subtraction_next_button_frame = tk.Frame(root, bg="light pink", bd=6)
subtraction_next_button_frame.place(x=610, y=200)
subtraction_next_button = tk.Button(
    subtraction_next_button_frame,
    text="Далі ==>",
    bg="hotpink1",
    fg="white",
    font="Times 16",
    command=start_subtraction,
)
subtraction_next_button.pack()

# Створення елементів для множення
multiplication_frame = tk.Frame(root, bg="deep sky blue", bd=5)
multiplication_frame.place(x=95, y=350)
multiplication_label = tk.Label(
    multiplication_frame, text="(^_^)", fg="white", bg="hotpink3", font="Times 22"
)
multiplication_label.pack()

multiplication_entry_frame = tk.Frame(root, bg="deep sky blue", bd=5)
multiplication_entry_frame.place(x=240, y=350)
multiplication_entry = tk.Entry(
    multiplication_entry_frame, width=3, fg="white", bg="hotpink3", font="Times 23"
)
multiplication_entry.pack()

multiplication_button_frame = tk.Frame(root, bg="deep sky blue", bd=5)
multiplication_button_frame.place(x=310, y=350)
multiplication_button = tk.Button(
    multiplication_button_frame,
    text="Відповідь",
    bg="hotpink1",
    fg="white",
    font="Times 16",
    command=check_multiplication,
)
multiplication_button.pack()

multiplication_result_frame = tk.Frame(root, bg="deep sky blue", bd=5)
multiplication_result_frame.place(x=450, y=350)
multiplication_result_label = tk.Label(
    multiplication_result_frame, fg="white", bg="hotpink3", font="Times 22"
)
multiplication_result_label.pack()

multiplication_next_button_frame = tk.Frame(root, bg="light pink", bd=6)
multiplication_next_button_frame.place(x=610, y=350)
multiplication_next_button = tk.Button(
    multiplication_next_button_frame,
    text="Далі ==>",
    bg="hotpink1",
    fg="white",
    font="Times 16",
    command=start_multiplication,
)
multiplication_next_button.pack()

root.mainloop()
