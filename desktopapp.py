import csv
import tkinter as tk
from tkinter import filedialog

def convert_text_to_csv():
    input_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not input_file:
        return

    output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])

    with open(input_file, 'r') as text_file, open(output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=readable_to_value.get((selected_option.get())))
        
        for line in text_file:
            parts = line.strip().split()
            country = ' '.join(parts[:-12])
            numbers = parts[-12:]
            csv_writer.writerow([country] + numbers)

    result_label.config(text=f'Данные успешно конвертированы в файл {output_file}')

# Create a Tkinter window
window = tk.Tk()
window.title("Конвертер")

# Replace 'icon.ico' with the path to your icon file
window.iconbitmap('C:\PythonProjects\HugeTable\MrBadger.ico')

button_label = tk.Label(window, text="Выбрать разделитель:")

#This line creates a StringVar object named selected_option
selected_option = tk.StringVar()
#Define a dictionary that maps human-readable delimiter names("keys":) to their actual values
readable_to_value = {
"столбик": "|",
"запятая": ",",
"точка с запятой": ";",
"пробел": "\t"
}
#This line creates a list named options by extracting the keys (human-readable delimiter names) from the readable_to_value dictionary
options = list((readable_to_value.keys()))
selected_option.set(options[0])

#This line creates an OptionMenu widget and associates it with the window. An OptionMenu is a dropdown menu that allows the user to select from a list of options
option_menu = tk.OptionMenu(window, selected_option, *options)


# Create a Button widget with a label (name) and associate it with a function
convert_button = tk.Button(window, text="Конвертировать", command=convert_text_to_csv)

# Create a Label widget to add a name or description to the button
result_label = tk.Label(window, text="")

button_label.pack()
option_menu.pack()
convert_button.pack()
result_label.pack()

window.mainloop()
