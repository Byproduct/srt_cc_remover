from subtitle_CC_remover_defs import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from tkinter import scrolledtext
import os
import sys
import webbrowser

# GUI layout - row numbers for GUI elements
row_title = 0
row_cleansinglefilebutton = row_title + 1
row_openinputfolderbutton = row_cleansinglefilebutton + 1
row_processfolderbutton = row_openinputfolderbutton + 1
row_openoutputfolderbutton = row_processfolderbutton + 1

# size of GUI buttons
buttonwidth = 25
buttonheight = 4
buttonpadding = 4

menu_main = tk.Tk()
menu_main.title("SRT subtitle CC remover")

# fonts
normal_font = tkFont.Font(family="Calibri", size=10)
bold_font = tkFont.Font(family="Calibri", size=12, weight="bold")
large_font = tkFont.Font(family="Calibri", size=22, weight="bold")

# starting text in the text box
textbox_content = "This program will remove [CLOSED CAPTIONS] from .srt subtitle files.\n\nYou can clean a single file or multiple files in the input folder at once.\n\n"

srtfilenames = list_input_directory()
if len(srtfilenames) == 0:
    textbox_content = textbox_content + "No .srt files detected in the input folder."
if len(srtfilenames) == 1:
    textbox_content = textbox_content + "One .srt file found in the input folder:"
    textbox_content = textbox_content + "\n" + str(srtfilenames[0])
if len(srtfilenames) > 1:
    textbox_content = textbox_content + str(len(srtfilenames)) + " .srt files found in the input folder:"
    for filename in srtfilenames:
        textbox_content = textbox_content + "\n" + str(filename)


def textbox_refresh(string):
    textbox.config(state='normal')
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.END, string)
    textbox.config(state='disabled')


label_title = tk.Label(menu_main, width=25, font=large_font, text="     .srt CC remover", height=2)
label_title.grid(row=row_title, column=0, pady=buttonpadding)


# clean single file
def clean_file():
    filetypes = (('text files', '*.srt'),)

    filename = tk.filedialog.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes
    )
    if filename:
        textbox_content = clean_single_file(filename)
        textbox_refresh(textbox_content)

# clean single file button
process_file_button = tk.Button(menu_main, font=normal_font, width=buttonwidth, height=buttonheight, text='Clean single file', command=clean_file)
process_file_button.grid(row=row_cleansinglefilebutton, column=0, pady=buttonpadding, sticky="")


def open_input_folder():
    path = "input"
    webbrowser.open(os.path.realpath(path))

# open input folder button
process_folder_button = tk.Button(menu_main, font=normal_font, width=buttonwidth, height=buttonheight, text='Open input folder', command=open_input_folder)
process_folder_button.grid(row=row_openinputfolderbutton, column=0, pady=buttonpadding, sticky="")


# clean input folder
def clean_input_folder():
    textbox_content = clean_multiple_files(srtfilenames)
    textbox_refresh(textbox_content)

# clean input folder button
process_folder_button = tk.Button(menu_main, font=normal_font, width=buttonwidth, height=buttonheight, text='Clean all files in input folder', command=clean_input_folder)
process_folder_button.grid(row=row_processfolderbutton, column=0, pady=buttonpadding, sticky="")


def open_output_folder():
    path = "output"
    webbrowser.open(os.path.realpath(path))


openfolderbutton = tk.Button(menu_main, font=normal_font, width=buttonwidth, height=buttonheight, text='Open output folder', command=open_output_folder)
openfolderbutton.grid(row=row_openoutputfolderbutton, column=0, pady=buttonpadding, sticky="")

def refresh():
    os.execl(sys.executable, sys.executable, *sys.argv)

refreshbutton = tk.Button(menu_main, font=normal_font, width=10, height=2, text='refresh ↻', command=refresh)
refreshbutton.grid(row=0, column=1, sticky="SE", padx=20, pady=10)

textbox = tk.scrolledtext.ScrolledText(menu_main, width=80, padx=10, pady=10)
textbox.grid(row=1, rowspan=4, column=1, pady=23)
textbox_refresh(textbox_content)

menu_main.mainloop()