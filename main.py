##################################################################################
##### video suporte   https://www.youtube.com/watch?v=rC6uR9gR6w4&list=PLrrsc4A0SSmw9csqiv8toMOBv2gOUNf1s&index=20
##################################################################################
#######################################################################################
####   IMPORTS
#######################################################################################
#
import sys
import os
from PySide2 import *
from PySide2 import QtCore
from PySide2 import QtGui

#######################################################################################
####   IMPORT GUI FILE
from ui_interface import *
#######################################################################################

#######################################################################################
####   MAIN WINDOW CLASS
#######################################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #######################################################################################
        ####   REMOVE WINDOW TITLE BAR
        #######################################################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #######################################################################################
        ####   SET MAIN BACKGROUND TO TRANSPARENT
        #######################################################################################
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #######################################################################################
        ####   SET MAIN BACKGROUND TO TRANSPARENT
        #######################################################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        #######################################################################################
        ####   APPY SHOW TO CENTRAL WIDGET
        #######################################################################################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        #######################################################################################
        ####   SET WINDOW ICON
        ####    THIS ICON AND TITLE WILL NOT APPEAR ON OUR APP MAIN WINDOW BECAUSE WE REMOVED THE TITLE BAR
        #######################################################################################
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/github.svg"))
        # Set window title
        self.setWindowTitle("MODERN UI")

        #######################################################################################
        ####   Window Size grip to resize window
        #######################################################################################
        QSizeGrip(self.ui.size_grip)

        #######################################################################################
        #Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        #######################################################################################
        #Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        self.ui.exit_button.clicked.connect(lambda: self.close())
        #######################################################################################
        #Restore window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        #######################################################################################
        ####   Function to Move window on mouse drag event on the title bar
        #######################################################################################
        def moveWindow(e):
            #Detect if the window is normal size
            ##################################################################################
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size
                ##############################################################################
                #if left mouse button is clicked (Only accpt left mouse button clicks)
                if e.buttons() == Qt.LeftButton:
                    #Move window
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        ######################################################################################

        #######################################################################################
        # Add click evnt/Mouse move event/drag event to the top header to move the window
        #######################################################################################
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #######################################################################################

       #######################################################################################
       ## Left Menu toggle button 
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        self.show()
    #######################################################################################
    ## Slide left menu function
    #######################################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.slide_menu_container.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-left.svg"))
        
        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth") #Animate minimumWidth
        self.animation.setDuration(250)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    #######################################################################################
    ## Add mouse events to the windoiw
    #######################################################################################
    def mousePressEvent(self, event):
        # ######################################################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        #We will use this value to move the window


    #######################################################################################
    ####   Update restore button icon on msximizing or minimizing window
    #######################################################################################
    def restore_or_maximize_window(self):
        #If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))

    

#######################################################################################
####   EXECUTE APP
#######################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

#######################################################################################
####   END ===>
##
#
#######################################################################################


