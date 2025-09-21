import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Template") # Заголовок вікна
        self.root.geometry("1366x768")  # Розмір вікна (ширина x висота)
        #self.root.resizable(False, False) # Блокування зміни розміру вікна
        self.root.configure(bg="#222526") # Колір фону вікна
        
        # ----------------------------------------------------------------------------------------#
        # Початок програми:
        # ----------------------------------------------------------------------------------------#
        self.label1 = tk.Label(root, text="Привіт, друже!", fg="#E0E0E0", bg="#222526", font=("Arial", 11))
        self.label1.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.label2 = tk.Label(root, text="Цей шаблон зібрано для зручного початку створення твого першого \nзастосунку мовою Python.", fg="#BFBFBF", bg="#222526", font=("Arial", 6), justify="left")
        self.label2.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        
def main():
    window = tk.Tk()
    app = App(window)
    window.mainloop()
    
if __name__ == "__main__":
    main()
