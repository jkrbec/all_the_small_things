import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        # create a button to select an image file
        self.select_button = tk.Button(self, text='Select Image', command=self.select_image)
        self.select_button.pack(side='top')
        
        # create a button to revert changes to the image
        self.revert_button = tk.Button(self, text='Revert Changes', command=self.revert_changes, state='disabled')
        self.revert_button.pack(side='top')
        
        # create a button to apply a blur filter to the image
        self.blur_button = tk.Button(self, text='Blur', command=lambda: self.apply_filter(ImageFilter.BLUR), state='disabled')
        self.blur_button.pack(side='top')
        
        # create a button to apply a contour filter to the image
        self.contour_button = tk.Button(self, text='Contour', command=lambda: self.apply_filter(ImageFilter.CONTOUR), state='disabled')
        self.contour_button.pack(side='top')
        
        # create a button to apply a black and white filter to the image
        self.black_and_white_button = tk.Button(self, text='Black and White', command=lambda: self.apply_convert("L"), state='disabled')
        self.black_and_white_button.pack(side='top')
        
        # create a button to apply an edge enhance filter to the image
        self.edge_enhance_button = tk.Button(self, text='Edge Enhance', command=lambda: self.apply_filter(ImageFilter.EDGE_ENHANCE), state='disabled')
        self.edge_enhance_button.pack(side='top')
        
        # create a button to download the filtered image
        self.download_button = tk.Button(self, text='Download Filtered Image', command=self.download_image, state='disabled')
        self.download_button.pack(side='top')
    
    def select_image(self):
        self.enable_widgets()
        # open a file dialog to select an image file
        file_path = filedialog.askopenfilename()
        
        # open the image file
        self.image = Image.open(file_path)
        
        # store a copy of the original image
        self.original_image = self.image.copy()
        
        # convert the image to a PhotoImage object
        self.photo_image = ImageTk.PhotoImage(self.image)
        
        # create a label to display the image
        self.image_label = tk.Label(image=self.photo_image)
        self.image_label.pack(side='bottom')
        
        # make the filter frame and download button visible
        self.filter_frame.pack(side='top')
        self.download_button.pack(side='top')


    def enable_widgets(self):
        widgets = [self.revert_button, self.blur_button, self.contour_button, self.black_and_white_button, self.edge_enhance_button, self.download_button]
        for widget in widgets:
            widget.configure(state='normal')

    def revert_changes(self):
        # revert the image to the original image
        self.image = self.original_image
        
        # convert the image to a PhotoImage object
        self.photo_image = ImageTk.PhotoImage(self.image)
        
        # update the image label to display the original image
        self.image_label.configure(image=self.photo_image)
        self.image_label.image = self.photo_image
    
    def apply_filter(self, filter_type):
        # apply a filter to the image
        self.filtered_image = self.image.filter(filter_type)
        
        # convert the filtered image to a PhotoImage object
        self.filtered_photo_image = ImageTk.PhotoImage(self.filtered_image)
        
        # update the image label to display the filtered image
        self.image_label.configure(image=self.filtered_photo_image)
        self.image_label.image = self.filtered_photo_image
    def apply_convert(self, filter_type):
        # apply a filter to the image
        self.filtered_image = self.image.convert(filter_type)
        
        # convert the filtered image to a PhotoImage object
        self.filtered_photo_image = ImageTk.PhotoImage(self.filtered_image)
        
        # update the image label to display the filtered image
        self.image_label.configure(image=self.filtered_photo_image)
        self.image_label.image = self.filtered_photo_image
    
    def download_image(self):
        # open a file dialog to select a location to save the filtered image
        file_path = filedialog.asksaveasfilename()
        
        # save the filtered image to the selected location
        self.filtered_image.save(file_path)

root = tk.Tk()
app = Application(master=root)
app.mainloop()