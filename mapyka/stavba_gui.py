import tkinter
import tkinter.messagebox
from PIL import ImageTk, Image
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("maPyka.py")
        self.geometry(f"{1200}x{600}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Settings", font=customtkinter.CTkFont(size=16, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #appearance mode options
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=0, padx=20, pady=(10, 10))
       
       
        #image insertion
        
        logo_img = ImageTk.PhotoImage(file="assets/logo.png")
        logo_widget = tkinter.Label(self.sidebar_frame, image = logo_img, bg="#2B2B2B")
        logo_widget.image = logo_img
        logo_widget.grid(row=3, column=0, padx=20, pady=10)

        # create textbox - types of assignments
        # self.textbox2 = customtkinter.CTkTextbox(self, width=450,font=("Helvetica", 20))
        # self.textbox2.grid(row=0, column=2, columnspan=2, rowspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        # create types of assignments with checkbutton instead

        # label_typy_uloh = customtkinter.CTkLabel(self, text="Vyberte typy úloh", font=customtkinter.CTkFont(size=16, weight="bold"),anchor="w")
        # label_typy_uloh.grid(row=0, column=2, pady=20, padx=20, sticky="n")
        # self.checkbox_01 = customtkinter.CTkCheckBox(self, text="Finanční příjem čtyřčlenné rodiny za 1. pololetí roku je {} Kč.\n Jaký je průměrný měsíční příjem?\n\n")
        # self.checkbox_01.grid(row=1, column=2, pady=(20, 10), padx=20, sticky='ns')
        self.checkbox_01 = customtkinter.CTkCheckBox(self)
        self.checkbox_01.grid(row=1, column=2, pady=10, padx=20, sticky='ns')
        self.text_label = tkinter.Label(self, text="Finanční příjem čtyřčlenné rodiny za 1. pololetí roku je {} Kč.\n Jaký je průměrný měsíční příjem?\n\n")
        self.text_label.grid(row=1, column=3, pady=10, padx=20, sticky='ns')
        


        #create generate pdf button

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color=customtkinter.set_default_color_theme("green"), border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=2, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        

        # create textbox - how to app
        self.textbox = customtkinter.CTkTextbox(self, font=("Helvetica", 20))
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
       
         # create slider and progressbar frame
        #self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        #self.slider_progressbar_frame.grid(row=0, column=3, rowspan=3 ,padx=(20, 0), pady=(20, 0), sticky="nsew")
        #self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        #self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        
        #number of assignments
        
        label_pocet_uloh = customtkinter.CTkLabel(self, text="Vyberte množství zadání", font=customtkinter.CTkFont(size=16, weight="bold"))
        label_pocet_uloh.grid(row=2, column=1, pady=10, padx=10)
        self.slider_1 = customtkinter.CTkSlider(self, from_=0, to=1, number_of_steps=30)
        self.slider_1.grid(row=3, column=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        # future
        """
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        """
        
        self.checkbox_slider_frame = customtkinter.CTkFrame(self, width=350)
        self.checkbox_slider_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        label_typ_ulohy = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text="Vyberte typy úloh", font=customtkinter.CTkFont(size=16, weight="bold"),anchor="w")
        label_typ_ulohy.grid(row=0, column=0, pady=10, padx=10)
        
        self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame, text="tady text")
        self.checkbox_1.grid(row=1, column=0, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=10, padx=20, sticky="n")

        self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=1, column=2, pady=(20, 10), padx=20, sticky="n")
        self.checkbox_4 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_4.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.checkbox_5 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        self.checkbox_5.grid(row=3, column=0, pady=10, padx=20, sticky="n")
        # self.checkbox_6 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_6.grid(row=4, column=0, pady=10, padx=20, sticky="n")
        # self.checkbox_7 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_7.grid(row=4, column=1, pady=10, padx=20, sticky="n")
     
      
        #scaling options
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0", "Jak pracovat s aplikací\n\n" + """Zaškrtni, co chceš, zvol počet zadání, vygeneruj, vytiskni. Trestej...""")
        #self.textbox2.insert("0.0", "Typové úlohy\n\n" + """Finanční příjem čtyřčlenné rodiny za 1. pololetí roku je {} Kč. Jaký je průměrný měsíční příjem?\n\n""" * 5)
        self.checkbox_1.select()
        self.checkbox_2.select()
        self.checkbox_3.select()
        self.checkbox_4.select()
        # self.checkbox_5.select()
        # self.checkbox_6.select()
        #self.main_button_1.set("dark")
    
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()