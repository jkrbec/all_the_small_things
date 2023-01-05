import sys
from PyQt5.QtGui import QImage, QPixmap, QColor
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QMenu, QMenuBar, QAction
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window properties
        self.setWindowTitle('Pylter')
        self.setGeometry(100, 100, 800, 600)

        # Add a label to display the image
        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 780, 580)

        # Create a menu bar and add a File menu
        self.menu_bar = QMenuBar(self)
        self.file_menu = QMenu('File', self)
        self.menu_bar.addMenu(self.file_menu)

        # Add a Open action to the File menu
        self.open_action = QAction('Open', self)
        self.open_action.triggered.connect(self.open_image)
        self.file_menu.addAction(self.open_action)

        # Add a Filter menu
        self.filter_menu = QMenu('Filter', self)
        self.menu_bar.addMenu(self.filter_menu)

        # Add three filter actions to the Filter menu
        self.black_and_white_action = QAction('Black and White', self)
        self.black_and_white_action.triggered.connect(self.apply_black_and_white_filter)
        self.filter_menu.addAction(self.black_and_white_action)

        self.cyan_filter_action = QAction('Cyan', self)
        self.cyan_filter_action.triggered.connect(self.apply_cyan_filter)
        self.filter_menu.addAction(self.cyan_filter_action)

        self.magenta_filter_action = QAction('Magenta', self)
        self.magenta_filter_action.triggered.connect(self.apply_magenta_filter)
        self.filter_menu.addAction(self.magenta_filter_action)

        # Set the menu bar
        self.setMenuBar(self.menu_bar)

        # Load the initial image
        self.image = QImage('photo.jpg')
        self.display_image()

    def open_image(self):
        # Open a file dialog to select an image
        options = QFileDialog.Options()
        #The options variable is used to specify the options for the 
        #file dialog. The QFileDialog.ReadOnly option specifies that 
        #the file dialog should only allow the user to select a file 
        #for reading, not for writing. 
        #The |= operator is used to set this option in the options 
        #variable.
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.jpg *.jpeg *.png);;All Files (*)', options=options)
        if file_name:
            # Load the image
            self.image = QImage(file_name)
            self.display_image()

    def apply_black_and_white_filter(self):
    # Create a copy of the image
        filtered_image = self.image.copy()

    # Iterate over all pixels in the image
        for x in range(filtered_image.width()):
            for y in range(filtered_image.height()):
                # Get the pixel at (x, y)
                pixel = filtered_image.pixel(x, y)

            # # Get the RGB values of the pixel
                color = QColor(pixel)
                red = color.red()
                green = color.green()
                blue = color.blue()
                alpha = color.alpha()
            
            # Convert the pixel to grayscale
                gray = (red + green + blue) // 3

            # Set the pixel value
                filtered_image.setPixel(x, y, QColor(gray, gray, gray, alpha).rgba())

    # Display the filtered image
        self.display_image(filtered_image)


    def apply_cyan_filter(self):
        # Create a copy of the image
        filtered_image = self.image.copy()

        # Iterate over all pixels in the image
        for x in range(filtered_image.width()):
            for y in range(filtered_image.height()):
                # Get the pixel at (x, y)
                pixel = filtered_image.pixel(x, y)

                # Get the RGB values of the pixel
                color = QColor(pixel)
                red = color.red()
                green = color.green()
                blue = color.blue()
                alpha = color.alpha()

                # Set the red and green channels to 0
                red = 0
                green = 0

                # Set the pixel value
                filtered_image.setPixel(x, y, QColor(red, green, blue, alpha).rgba())

        # Display the filtered image
        self.display_image(filtered_image)

    def apply_magenta_filter(self):
        # Create a copy of the image
        filtered_image = self.image.copy()

        # Iterate over all pixels in the image
        for x in range(filtered_image.width()):
            for y in range(filtered_image.height()):
                # Get the pixel at (x, y)
                pixel = filtered_image.pixel(x, y)

                # Get the RGB values of the pixel
                color = QColor(pixel)
                red = color.red()
                green = color.green()
                blue = color.blue()
                alpha = color.alpha()

                # Set the green and blue channels to 0
                green = 0
                blue = 0

                # Set the pixel value
                filtered_image.setPixel(x, y, QColor(red, green, blue, alpha).rgba())

        # Display the filtered image
        self.display_image(filtered_image)

    def display_image(self, image=None):
        if image is None:
            image = self.image
        # Create a pixmap from the image
        pixmap = QPixmap.fromImage(image)
        # Set the pixmap as the label's image
        self.label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
