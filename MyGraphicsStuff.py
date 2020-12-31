from PySide2.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsSceneMouseEvent, QGraphicsPixmapItem, QVBoxLayout, QGraphicsTextItem
from PySide2.QtGui import QPixmap, QMatrix, QTransform
from PySide2.QtCore import QRect, QRectF
from PySide2.QtCore import Qt

class MyGraphicsScene(QGraphicsScene):
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow=mainWindow
        self.changed.connect(self.sig_changed)
        self.focusItemChanged.connect(self.sig_focusItemChanged)
        self.sceneRectChanged.connect(self.sig_sceneRectChanged)
        self.selectionChanged.connect(self.sig_selectionChanged)

    def sig_changed(self, region):
        pass

    def sig_focusItemChanged (self, newFocus, oldFocus, reason):
        print('GraphicsScene - focusItemChanged')

    def sig_sceneRectChanged (self, rect):
        print('GraphicsScene - sceneRectChanged')

    def sig_selectionChanged(self):
        print('GraphicsScene - selectionChanged')

class MyGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainWindow = self.parent().parent()
        self.scene: QGraphicsScene = MyGraphicsScene(self)
        self.setScene(self.scene)
        self.dZone = DZoneItem()  # Translate the pixmap into a GraphicsPixMapItem which is a type of QGraphicsItem
        self.scene.addItem(self.dZone)  # Add the modified and converted dzone to the scene (which will ultimately be shown by the view
        self.puck = PuckItem(self.dZone)
        self.mainWindow.scaleSlider.valueChanged.connect(self.sliderChanged)
        _ = QGraphicsTextItem(f'DZoneTextItem', self.dZone)

    def sliderChanged(self, value):
        self.dZone.transform(value/100)

    def populateSizes(self):
        self.mainWindow.dzoneSize.setText(f'DZone Size: {self.dZone.boundingRect().height()},{self.dZone.boundingRect().width()}')
        self.mainWindow.viewSize.setText(f'gView Size: {self.rect().height()},{self.rect().width()}')
        self.mainWindow.viewSceneRect.setText(f'gView Scene Size: {self.sceneRect().height()},{self.sceneRect().width()}')
        self.mainWindow.sceneSize.setText(f'Scene Size: {self.sceneRect().height()},{self.sceneRect().width()}')

    def resizeEvent(self, event) -> None:
        self.populateSizes()

    def mouseEvent(self, event):
        self.mainWindow.viewPos.setText(f'GView Pos: {event.pos().x()},{event.pos().y()}')
        pos = self.mapToScene(event.pos())
        self.mainWindow.scenePos.setText(f'Scene Pos: {pos.x()},{pos.y()}')

        items = self.items(event.pos())
        if self.dZone in items:
            pos = self.dZone.mapFromScene(self.mapToScene(event.pos()))
            self.mainWindow.dzonePos.setText(f'DZone Pos: {pos.x()},{pos.y()}')
        else:
            self.mainWindow.dzonePos.setText(f'DZone Pos: <not in DZone>')

        if self.puck in items:
            pos = self.puck.mapFromScene(self.mapToScene(event.pos()))
            self.mainWindow.puckPos.setText(f'Puck Pos: {pos.x()},{pos.y()}')
        else:
            self.mainWindow.puckPos.setText(f'')

        self.populateSizes()

    def mouseMoveEvent(self, event):
        self.mouseEvent(event)

    def mousePressEvent(self, event):
        self.mouseEvent(event)

    def mouseReleaseEvent(self, event):
        self.mouseEvent(event)

    def rubberBandChanged(viewportRect, fromScenePoint, toScenePoint):
        print('GraphicsView - rubberBandChanged')

class DZoneItem(QGraphicsPixmapItem):
    DZONE_SCALE: float = 0

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setZValue(-1)  # This tells this dzone graphic item to be at the bottom of all other items in the scene
        self.setTransformationMode(Qt.TransformationMode.SmoothTransformation)  # Draw in hightest quality at the expense of speed. One image is not going to have a huge effect.
        self.pm = QPixmap('halfice.gif')  # load my dzone image into a PixMap - A pixmap is how Qt Handles pictures in an agnostic way.
        #pm = pm.scaled(pm.rect().width()*self.DZONE_SCALE, pm.rect().height()*self.DZONE_SCALE, Qt.KeepAspectRatio)  # I need to scale the picture down to the size of the view. The original picture is huge (5918x5009 pixels)
        self.setPixmap(self.pm)
        self.transform(self.DZONE_SCALE)
        self.setEnabled(True)

    def transform(self, scale):
        dZoneMatrix = QMatrix()
        dZoneMatrix.rotate(90)
        dZoneMatrix.scale(scale/100, scale/100)
        self.deviceTransform(QTransform(dZoneMatrix))  # Apply the matrix to the pixmap. This creates a new rotated pixmap

class PuckItem(QGraphicsPixmapItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.puck = QPixmap('puck.svg')  # Read the puck picture
        self.setPixmap(self.puck)  # Set the pixmap this object
        self.setFlags(self.GraphicsItemFlag.ItemIsMovable | self.GraphicsItemFlag.ItemIsSelectable | self.GraphicsItemFlag.ItemSendsScenePositionChanges)  # Set appropriate flags for hte item
        self.setTransformationMode(Qt.TransformationMode.SmoothTransformation)
        self.setPos(self.scene().width()/2, self.scene().height()/2)
        self.setEnabled(True)
