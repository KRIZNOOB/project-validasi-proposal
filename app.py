from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.font import Font
import os
import fitz 
from PIL import Image, ImageTk
from nfa import run_nfa

current_state = "q1"
review_notes = []
note_entry = None
review_results_text = ""

def add_note():
    global review_notes
    if note_entry:
        note = note_entry.get()
        if note:
            review_notes.append(note)
            note_entry.delete(0, 'end')
            
def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("Docx files", "*.docx"),("image file","*.png")])
    if file_path:
        file_name = os.path.basename(file_path)
        selected_file_label.config(text=f"{file_name}")
        upload_button.pack(pady=20) 

def upload_file():
    global current_state
    if file_path:
        upload_status_label.config(text=f"File {os.path.basename(file_path)} sudah terupload!")
        upload_button.pack_forget()
        current_state = run_nfa(current_state, "complete")
        checker_ui()

def checker_ui():
    global checker_window, canvas, pdf_image_container, myfont
    checker_window = Toplevel()
    checker_window.title("Pemeriksaan Proposal")
    checker_window.geometry("950x600")
    checker_window["bg"] = "white"
    checker_window.resizable(None, None)
    myfont = Font(family="Poppins", size=20)
    
    checker_label = Label(checker_window, text="Pemeriksaan Proposal", bg="white", font=myfont)
    checker_label.pack(pady=20, anchor="center")
    
    button_frame = Frame(checker_window, bg="white")
    button_frame.pack(side=TOP, pady=10)
    
    lengkap_button = Button(button_frame, text="Lengkap", command=judul_ui, font=myfont, width=10, height=1, padx=10)
    lengkap_button.pack(side=LEFT, padx=10)
    
    tidak_lengkap_button = Button(button_frame, text="Tidak Lengkap", command=return_to_upload, font=myfont, width=10, height=1, padx=10)
    tidak_lengkap_button.pack(side=LEFT, padx=10)
    
    pdf_frame = Frame(checker_window, bg="white")
    pdf_frame.pack(side=LEFT, fill=BOTH, expand=True)
    
    pdf_canvas = Canvas(pdf_frame, bg="white")
    pdf_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(pdf_frame, orient=VERTICAL, command=pdf_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    pdf_canvas.configure(yscrollcommand=scrollbar.set)
    pdf_canvas.bind('<Configure>', lambda e: pdf_canvas.configure(scrollregion=pdf_canvas.bbox("all")))
    
    pdf_image_container = Frame(pdf_canvas, bg="white")
    pdf_canvas.create_window((0, 0), window=pdf_image_container, anchor="nw")
    
    display_pdf()

def judul_ui():
    global checker_window, note_entry, myfont, current_state, pdf_image_container
    if 'note_entry' in globals():
        add_note()
    current_state = run_nfa(current_state, "complete")
    checker_window.destroy()
    checker_window = Toplevel()
    checker_window.title("Pemeriksaan Judul")
    checker_window.geometry("950x600")
    checker_window["bg"] = "white"
    checker_window.resizable(None, None)
    
    title_label = Label(checker_window, text="Pemeriksaan Judul", bg="white", font=myfont)
    title_label.pack(pady=20, anchor="center")
    
    note_label = Label(checker_window, text="Catatan untuk Judul:", bg="white", font=myfont)
    note_label.pack(pady=10, anchor="center")
    
    note_entry = Entry(checker_window, font=myfont)
    note_entry.pack(pady=10, anchor="center")
    
    button_frame = Frame(checker_window, bg="white")
    button_frame.pack(side=TOP, pady=10)
    
    next_button = Button(button_frame, text="Next", command=pendahuluan_ui, font=myfont, width=10, height=1)
    next_button.pack(side=LEFT, padx=10)
    
    pdf_frame = Frame(checker_window, bg="white")
    pdf_frame.pack(side=LEFT, fill=BOTH, expand=True)
    
    pdf_canvas = Canvas(pdf_frame, bg="white")
    pdf_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(pdf_frame, orient=VERTICAL, command=pdf_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    pdf_canvas.configure(yscrollcommand=scrollbar.set)
    pdf_canvas.bind('<Configure>', lambda e: pdf_canvas.configure(scrollregion=pdf_canvas.bbox("all")))
    
    pdf_image_container = Frame(pdf_canvas, bg="white")
    pdf_canvas.create_window((0, 0), window=pdf_image_container, anchor="nw")
    
    display_pdf()

def pendahuluan_ui():
    global checker_window, note_entry, myfont, current_state, pdf_image_container
    add_note()
    current_state = run_nfa(current_state, "introduction")
    checker_window.destroy()
    checker_window = Toplevel()
    checker_window.title("Pemeriksaan Pendahuluan")
    checker_window.geometry("950x600")
    checker_window["bg"] = "white"
    checker_window.resizable(None, None)
    
    title_label = Label(checker_window, text="Pemeriksaan Pendahuluan", bg="white", font=myfont)
    title_label.pack(pady=20, anchor="center")
    
    note_label = Label(checker_window, text="Catatan untuk Pendahuluan:", bg="white", font=myfont)
    note_label.pack(pady=10, anchor="center")
    
    note_entry = Entry(checker_window, font=myfont)
    note_entry.pack(pady=10, anchor="center")
    
    button_frame = Frame(checker_window, bg="white")
    button_frame.pack(side=TOP, pady=10)
    
    next_button = Button(button_frame, text="Next", command=tinjauan_ui, font=myfont, width=10, height=1)
    next_button.pack(side=LEFT, padx=10)
    
    pdf_frame = Frame(checker_window, bg="white")
    pdf_frame.pack(side=LEFT, fill=BOTH, expand=True)
    
    pdf_canvas = Canvas(pdf_frame, bg="white")
    pdf_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(pdf_frame, orient=VERTICAL, command=pdf_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    pdf_canvas.configure(yscrollcommand=scrollbar.set)
    pdf_canvas.bind('<Configure>', lambda e: pdf_canvas.configure(scrollregion=pdf_canvas.bbox("all")))
    
    pdf_image_container = Frame(pdf_canvas, bg="white")
    pdf_canvas.create_window((0, 0), window=pdf_image_container, anchor="nw")
    
    display_pdf()

def tinjauan_ui():
    global checker_window, note_entry, myfont, current_state, pdf_image_container
    add_note()
    current_state = run_nfa(current_state, "literature_review")
    checker_window.destroy()
    checker_window = Toplevel()
    checker_window.title("Pemeriksaan Tinjauan Pustaka")
    checker_window.geometry("950x600")
    checker_window["bg"] = "white"
    checker_window.resizable(None, None)
    
    title_label = Label(checker_window, text="Pemeriksaan Tinjauan Pustaka", bg="white", font=myfont)
    title_label.pack(pady=20, anchor="center")
    
    note_label = Label(checker_window, text="Catatan untuk Tinjauan Pustaka:", bg="white", font=myfont)
    note_label.pack(pady=10, anchor="center")
    
    note_entry = Entry(checker_window, font=myfont)
    note_entry.pack(pady=10, anchor="center")
    
    button_frame = Frame(checker_window, bg="white")
    button_frame.pack(side=TOP, pady=10)
    
    next_button = Button(button_frame, text="Next", command=metode_ui, font=myfont, width=10, height=1)
    next_button.pack(side=LEFT, padx=10)
    
    pdf_frame = Frame(checker_window, bg="white")
    pdf_frame.pack(side=LEFT, fill=BOTH, expand=True)
    
    pdf_canvas = Canvas(pdf_frame, bg="white")
    pdf_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(pdf_frame, orient=VERTICAL, command=pdf_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    pdf_canvas.configure(yscrollcommand=scrollbar.set)
    pdf_canvas.bind('<Configure>', lambda e: pdf_canvas.configure(scrollregion=pdf_canvas.bbox("all")))
    
    pdf_image_container = Frame(pdf_canvas, bg="white")
    pdf_canvas.create_window((0, 0), window=pdf_image_container, anchor="nw")
    
    display_pdf()

def metode_ui():
    global checker_window, note_entry, myfont, current_state, pdf_image_container
    add_note()
    current_state = run_nfa(current_state, "methodology")
    checker_window.destroy()
    checker_window = Toplevel()
    checker_window.title("Pemeriksaan Metode Penelitian")
    checker_window.geometry("950x600")
    checker_window["bg"] = "white"
    checker_window.resizable(None, None)
    
    title_label = Label(checker_window, text="Pemeriksaan Metode Penelitian", bg="white", font=myfont)
    title_label.pack(pady=20, anchor="center")
    
    note_label = Label(checker_window, text="Catatan untuk Metode Penelitian:", bg="white", font=myfont)
    note_label.pack(pady=10, anchor="center")
    
    note_entry = Entry(checker_window, font=myfont)
    note_entry.pack(pady=10, anchor="center")
    
    button_frame = Frame(checker_window, bg="white")
    button_frame.pack(side=TOP, pady=10)
    
    next_button = Button(button_frame, text="Next", command=format_ui, font=myfont, width=10, height=1)
    next_button.pack(side=LEFT, padx=10)
    
    pdf_frame = Frame(checker_window, bg="white")
    pdf_frame.pack(side=LEFT, fill=BOTH, expand=True)
    
    pdf_canvas = Canvas(pdf_frame, bg="white")
    pdf_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(pdf_frame, orient=VERTICAL, command=pdf_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    pdf_canvas.configure(yscrollcommand=scrollbar.set)
    pdf_canvas.bind('<Configure>', lambda e: pdf_canvas.configure(scrollregion=pdf_canvas.bbox("all")))
    
    pdf_image_container = Frame(pdf_canvas, bg="white")
    pdf_canvas.create_window((0, 0), window=pdf_image_container, anchor="nw")
    
    display_pdf()

def format_ui():
    global checker_window, note_entry, myfont, current_state, pdf_image_container
    add_note()
    current_state = run_nfa(current_state, "format")
    checker_window.destroy()
    checker_window = Toplevel()
    checker_window.title("Pemeriksaan Format Proposal")
    checker_window.geometry("950x600")
    checker_window["bg"] = "white"
    checker_window.resizable(None, None)
    
    title_label = Label(checker_window, text="Pemeriksaan Format Proposal", bg="white", font=myfont)
    title_label.pack(pady=20, anchor="center")
    
    note_label = Label(checker_window, text="Catatan untuk Format Proposal:", bg="white", font=myfont)
    note_label.pack(pady=10, anchor="center")
    
    note_entry = Entry(checker_window, font=myfont)
    note_entry.pack(pady=10, anchor="center")
    
    button_frame = Frame(checker_window, bg="white")
    button_frame.pack(side=TOP, pady=10)
    
    send_button = Button(button_frame, text="Kirim Review", command=after_send_review, font=myfont, width=10, height=1)
    send_button.pack(side = LEFT, padx = 10)
    
    pdf_frame = Frame(checker_window, bg="white")
    pdf_frame.pack(side=LEFT, fill=BOTH, expand=True)
    
    pdf_canvas = Canvas(pdf_frame, bg="white")
    pdf_canvas.pack(side=LEFT, fill=BOTH, expand=True)
    
    scrollbar = Scrollbar(pdf_frame, orient=VERTICAL, command=pdf_canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    pdf_canvas.configure(yscrollcommand=scrollbar.set)
    pdf_canvas.bind('<Configure>', lambda e: pdf_canvas.configure(scrollregion=pdf_canvas.bbox("all")))
    
    pdf_image_container = Frame(pdf_canvas, bg="white")
    pdf_canvas.create_window((0, 0), window=pdf_image_container, anchor="nw")
    
    display_pdf()

def display_pdf():
    global pdf_image_container, file_path
    if file_path:
        for widget in pdf_image_container.winfo_children():
            widget.destroy()
        doc = fitz.open(file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img_tk = ImageTk.PhotoImage(img)
            img_label = Label(pdf_image_container, image=img_tk)
            img_label.image = img_tk
            img_label.pack()

def send_review():
    global review_notes, review_results_text
    add_note()
    
    review_results_text = (
        f"Judul: {review_notes[0]}\n\n"
        f"Pendahuluan: {review_notes[1]}\n\n"
        f"Tinjauan Pustaka: {review_notes[2]}\n\n"
        f"Metode Penelitian: {review_notes[3]}\n\n"
        f"Format Proposal: {review_notes[4]}"
    )

    messagebox.showinfo("Info", "Hasil Review Terkirim")

def show_review_notes():
    global review_results_text
    if review_results_text:
        result_window = Toplevel(window)
        result_window.title("Hasil Review")
        result_window.geometry("800x600")
        result_label = Label(result_window, text="Hasil Review", font=myfont)
        result_label.pack(pady=20, anchor="center")
        
        review_text = Text(result_window, wrap=WORD, font=myfont)
        review_text.insert(END, review_results_text)
        review_text.config(state=DISABLED)  
        review_text.pack(pady=10, padx=10, fill=BOTH, expand=True)
    else:
        messagebox.showinfo("Info", "Belum ada hasil review yang tersedia.")

def return_to_upload():
    global checker_window, upload_status_label
    checker_window.destroy()
    upload_status_label.config(text="File tidak lengkap, silahkan upload ulang.")

def after_send_review():
    global checker_window, upload_status_label
    send_review()
    checker_window.destroy()
    upload_status_label.config(text="Hasil review sudah diterima.")

def ui():
    global selected_file_label, upload_button, upload_status_label, file_path, window, myfont
    file_path = None
    window = Tk()
    window.title("Program Pengecekkan Proposal")
    window.geometry("800x600")
    window.configure(bg="white")

    myfont = Font(family="Poppins", size=15)

    intro_label = Label(window, text="Program Pengecekkan Proposal", bg="white", font=myfont)
    intro_label.pack(pady=20, anchor="center")
    
    button = Button(window, text="Pilih file", command=select_file, font=Font(family="Poppins", size=15), width=10, height=1)
    button.pack(pady=30, anchor="center")
    
    selected_file_label = Label(window, text="Tidak ada file", bg="white", font=myfont)
    selected_file_label.pack(pady=10, anchor="center")
    
    upload_button = Button(window, text="Upload", command=upload_file, font=Font(family="Poppins", size=15), width=10, height=1)
    upload_button.pack(pady=10, anchor="center")
    upload_button.pack_forget()
    
    upload_status_label = Label(window, text="", bg="white", font=myfont)
    upload_status_label.pack(pady=20, anchor="center")
    
    review_notes_button = Button(window, text="Review Notes", command=show_review_notes, font=Font(family="Poppins", size=15), width=10, height=1)
    review_notes_button.pack(pady=10, anchor="center")
    
    window.mainloop()

if __name__ == "__main__":
    ui()