from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsSceneMouseEvent, QGraphicsPixmapItem, QVBoxLayout, QGraphicsTextItem
from PySide2.QtGui import QPixmap, QMatrix
from PySide2.QtCore import QRect, QRectF
from PySide2.QtCore import Qt
import sys
from UI_MainWindow import Ui_MainWindow
from MyGraphicsStuff import MyGraphicsScene


# pyside2-uic MainWindow.ui > UI_MainWindow.py

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

def main(argv):
    app = QApplication(argv)  # Initialize the QApplication object. This is necessary to run any Qt Applications
    mainWindow = MainWindow()  # Create the main application window
    mainWindow.show()  # Lets show the window
    app.exec_()  # Lets start the application event loop


if __name__ == "__main__":
    main(sys.argv)

    # def mouseMoveEvent(self, event):
    #     super().mouseMoveEvent(event) #I spent over 4 hours realizing this had to be called and called first
    #
    #     x = self.x() #Get location in parent coordinates
    #     y = self.y()
    #     newPos = self.pos() #this will be my new possible constrained location
    #
    #     maxX = self.parentItem().boundingRect().width() #Get bounding rect of parent (rink) so I can limit dragging
    #     maxY = self.parentItem().boundingRect().height()
    #
    #     if x <= 0: #Limit x dragging
    #         newPos.setX(0)
    #     elif x >= maxX-self.boundingRect().width():
    #         newPos.setX(maxX-self.boundingRect().width())
    #
    #     if y <= 0: #Limit Y dragging
    #         newPos.setY(0)
    #     elif y >= maxY-self.boundingRect().height():
    #         newPos.setY(maxY-self.boundingRect().height())
    #
    #     #self.setPos(newPos)
    #     print('---')
    #     print(x,y)
    #     scenerect = self.mapToScene(event.pos())
    #     print(scenerect.x(), scenerect.y())
