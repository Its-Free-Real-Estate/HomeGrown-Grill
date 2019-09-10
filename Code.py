import sys
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPalette, QBrush, QIntValidator, QRegExpValidator
from PyQt5.QtCore import QSize, Qt
from decimal import Decimal


class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        # Connects the program to the Qt designer file
        loadUi('HomePage.ui', self)
        # Window title
        self.setWindowTitle('Homegrown Grill')

        # Sets background image, and size

        background = QImage("Farm3.JPG")
        background_size = background.scaled(QSize(1680,1120))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))
        self.setPalette(palette)

        self.pushButton.clicked.connect(self.on_delivery_button_clicked)
        self.pushButton_3.clicked.connect(self.on_quit_button_clicked)
        self.pushButton_2.clicked.connect(self.on_pickup_button_clicked)

        global O1
        global O2
        global O3
        global O4
        global O5
        global O6
        global O7
        global O8
        global O9
        global O10
        global O11
        global O12

        global PO1
        global PO2
        global PO3
        global PO4
        global PO5
        global PO6
        global PO7
        global PO8
        global PO9
        global PO10
        global PO11
        global PO12

        global PBag

        global PDeliveryFee

        global SmallBoxSize
        global MediumBoxSize

    # This area of code is completely customisable, you can change whats in stock and price of items plus how much can go in a box

    # O means option or item

        O1 = 'Carrot'
        O2 = 'Lettuce'
        O3 = 'Cucumber'
        O4 = 'Potatoes'
        O5 = 'Tomatoes'
        O6 = 'Chili'
        O7 = 'Nuts'
        O8 = 'Milk'
        O9 = 'Strawberries'
        O10 = 'Lemons'
        O11 = 'Apples'
        O12 = 'Banana'

    # P means price

        PO1 = 2
        PO2 = 1
        PO3 = 0.5
        PO4 = 0.2
        PO5 = 1.2
        PO6 = 1
        PO7 = 3
        PO8 = 4
        PO9 = 3
        PO10 = 0.5
        PO11 = 0.6
        PO12 = 2

        PBag = 1

        PDeliveryFee = 3

        # Up to how many items in a box
        # Large Box Size is anything bigger than a Medium box

        SmallBoxSize = 10
        MediumBoxSize = 30

    @pyqtSlot()
    # Exits the program
    def on_quit_button_clicked(self):
        self.hide()
        self.setText("Quit")

    # This the same code for every button that changes the widget throughout th code

    # Selects the new widget or page
    # Shows the new widget
    # hides the old widget

    def on_delivery_button_clicked(self):
        self.widget = Delivery()
        self.widget.show()
        self.hide()

    def on_pickup_button_clicked(self):
        self.widget = PickUp()
        self.widget.show()
        self.hide()


class Delivery(QDialog):

    def __init__(self):
        super(Delivery, self).__init__()
        loadUi('Delivery.ui', self)
        self.setWindowTitle('Information')

        background = QImage("Background.JPG")
        background_size = background.scaled(QSize(816,1300))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))

        self.setPalette(palette)

        global PDeliveryFee
        self.label_4.setText("{} dollar delivery fee".format(PDeliveryFee))

        self.nextButton.clicked.connect(self.on_next_button_clicked)
        self.cancelButton.clicked.connect(self.on_cancel_button_clicked)

        self.Name.textChanged.connect(self.on_name_clicked)
        self.Address.textChanged.connect(self.on_address_clicked)
        self.Phone.textChanged.connect(self.on_phone_clicked)

        # prevents letters for been entered
        self.onlyInt = QIntValidator()
        self.Phone.setValidator(self.onlyInt)

        # prevents numbers and other values from been entered
        regex = QtCore.QRegExp("[a-z-A-Z_ ]+")
        txt = QtGui.QRegExpValidator(regex, self.Name)
        self.Name.setValidator(txt)

    def on_cancel_button_clicked(self):
        self.widget = Home()
        self.widget.show()
        self.hide()

    def on_name_clicked(self):
        global name
        name = self.Name.text()
        return name

    def on_address_clicked(self):
        global address
        address = self.Address.text()
        return address

    def on_phone_clicked(self):
        global phone
        phone = self.Phone.text()
        return phone

    def on_next_button_clicked(self):
        check_name = self.on_name_clicked()
        check_address = self.on_address_clicked()
        check_phone = self.on_phone_clicked()
        # checks to see if a name has been entered
        if check_name != "" and check_address != "" and check_phone != "":
            self.widget = ChecklistDelivery()
            self.widget.show()
            self.hide()
        else:
            self.label.setText('Please Fill out all boxes')


class PickUp(QDialog):
    def __init__(self):
        super(PickUp, self).__init__()
        loadUi('Pickup.ui', self)
        self.setWindowTitle('Pickup')

        background = QImage("Background.JPG")
        background_size = background.scaled(QSize(816,1300))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))

        self.setPalette(palette)

        self.nextButton.clicked.connect(self.on_next_button_clicked)
        self.cancelButton.clicked.connect(self.on_cancel_button_clicked)
        self.Name.textChanged.connect(self.on_name_clicked)
        self.Phone.textChanged.connect(self.on_phone_clicked)

        # prevents letters for been entered
        self.onlyInt = QIntValidator()
        self.Phone.setValidator(self.onlyInt)

        # prevents numbers and other values from been entered

        regex = QtCore.QRegExp("[a-z-A-Z_ ]+")
        txt = QtGui.QRegExpValidator(regex, self.Name)
        self.Name.setValidator(txt)

    def on_next_button_clicked(self):
        check_name = self.on_name_clicked()
        check_phone = self.on_phone_clicked()
        # checks to see if a name has been entered
        if check_name != "" and check_phone != "":
            self.widget = ChecklistPickup()
            self.widget.show()
            self.hide()
        else:
            self.label.setText('Please Fill out all boxes')

    def on_name_clicked(self):
        global name
        name = self.Name.text()
        return name

    def on_phone_clicked(self):
        global phone
        phone = self.Phone.text()
        return phone

    def on_cancel_button_clicked(self):
        self.widget = Home()
        self.widget.show()
        self.hide()


class ChecklistDelivery(QDialog):
    def __init__(self):
        super(ChecklistDelivery, self).__init__()
        loadUi('Checklist.ui', self)
        self.setWindowTitle('Checklist Delivery')
        background = QImage("Background2.JPG")
        background_size = background.scaled(QSize(816,1154))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))
        self.setPalette(palette)

        global O1
        global O2
        global O3
        global O4
        global O5
        global O6
        global O7
        global O8
        global O9
        global O10
        global O11
        global O12

        global PDeliveryFee

        global PBag

        global total

        total = 0

        # sets the initial total since it's delivery it will start as $3

        self.Total.setText("${}.00".format(PDeliveryFee))

        # sets the text of the text boxes to what the owner says they are
        # sets the text alignment to center

        self.T1.setText("{}".format(O1))
        self.T1.setAlignment(Qt.AlignCenter)

        self.T2.setText("{}".format(O2))
        self.T2.setAlignment(Qt.AlignCenter)

        self.T3.setText("{}".format(O3))
        self.T3.setAlignment(Qt.AlignCenter)

        self.T4.setText("{}".format(O4))
        self.T4.setAlignment(Qt.AlignCenter)

        self.T5.setText("{}".format(O5))
        self.T5.setAlignment(Qt.AlignCenter)

        self.T6.setText("{}".format(O6))
        self.T6.setAlignment(Qt.AlignCenter)

        self.T7.setText("{}".format(O7))
        self.T7.setAlignment(Qt.AlignCenter)

        self.T8.setText("{}".format(O8))
        self.T8.setAlignment(Qt.AlignCenter)

        self.T9.setText("{}".format(O9))
        self.T9.setAlignment(Qt.AlignCenter)

        self.T10.setText("{}".format(O10))
        self.T10.setAlignment(Qt.AlignCenter)

        self.T11.setText("{}".format(O11))
        self.T11.setAlignment(Qt.AlignCenter)

        self.T12.setText("{}".format(O12))
        self.T12.setAlignment(Qt.AlignCenter)

        self.BagBox.setText("Do you want a bag for an extra ${}".format(PBag))
        self.BagBox.setAlignment(Qt.AlignCenter)

        # Connects the amount of an item to the cost
        # Sets the minimum to 0

        self.O1.valueChanged.connect(self.total_price)
        self.O1.setMinimum(0)

        self.O2.valueChanged.connect(self.total_price)
        self.O2.setMinimum(0)

        self.O3.valueChanged.connect(self.total_price)
        self.O3.setMinimum(0)

        self.O4.valueChanged.connect(self.total_price)
        self.O4.setMinimum(0)

        self.O5.valueChanged.connect(self.total_price)
        self.O5.setMinimum(0)

        self.O6.valueChanged.connect(self.total_price)
        self.O6.setMinimum(0)

        self.O7.valueChanged.connect(self.total_price)
        self.O7.setMinimum(0)

        self.O8.valueChanged.connect(self.total_price)
        self.O8.setMinimum(0)

        self.O9.valueChanged.connect(self.total_price)
        self.O9.setMinimum(0)

        self.O10.valueChanged.connect(self.total_price)
        self.O10.setMinimum(0)

        self.O11.valueChanged.connect(self.total_price)
        self.O11.setMinimum(0)

        self.O12.valueChanged.connect(self.total_price)
        self.O12.setMinimum(0)

        self.Bag.stateChanged.connect(self.total_price)

        self.Cancel.clicked.connect(self.on_cancel_clicked)
        self.Back.clicked.connect(self.on_back_clicked)
        self.Submit.clicked.connect(self.on_submit_clicked)

    def on_cancel_clicked(self):
        self.widget = Home()
        self.widget.show()
        self.hide()

    def on_back_clicked(self):
        self.widget = Delivery()
        self.widget.show()
        self.hide()

    def on_submit_clicked(self):
        global total
        if total <= 3:
            self.label.setText('Please select an item')
        else:
            self.widget = FinalDeliveryPrice()
            self.widget.show()
            self.hide()

    def total_price(self):

        global PO1
        global PO2
        global PO3
        global PO4
        global PO5
        global PO6
        global PO7
        global PO8
        global PO9
        global PO10
        global PO11
        global PO12

        global PBag

        global PDeliveryFee

        global total

        global AO1
        global TO1

        global AO2
        global TO2

        global AO3
        global TO3

        global AO4
        global TO4

        global AO5
        global TO5

        global AO6
        global TO6

        global AO7
        global TO7

        global AO8
        global TO8

        global AO9
        global TO9

        global AO10
        global TO10

        global AO11
        global TO11

        global AO12
        global TO12

        global bagPrice

        # A means Amount

        # T means total price

        AO1 = self.O1.value()
        TO1 = AO1 * PO1
        TO1 = round(TO1,2)

        AO2 = self.O2.value()
        TO2 = AO2 * PO2
        TO2 = round(TO2,2)

        AO3 = self.O3.value()
        TO3 = AO3 * PO3
        TO3 = round(TO3,2)

        AO4 = self.O4.value()
        TO4 = AO4 * PO4
        TO4 = round(TO4,2)

        AO5 = self.O5.value()
        TO5 = AO5 * PO5
        TO5 = round(TO5,2)

        AO6 = self.O6.value()
        TO6 = AO6 * PO6
        TO6 = round(TO6,2)

        AO7 = self.O7.value()
        TO7 = AO7 * PO7
        TO7 = round(TO7,2)

        AO8 = self.O8.value()
        TO8 = AO8 * PO8
        TO8 = round(TO8,2)

        AO9 = self.O9.value()
        TO9 = AO9 * PO9
        TO9 = round(TO9,2)

        AO10 = self.O10.value()
        TO10 = AO10 * PO10
        TO10 = round(TO10,2)

        AO11 = self.O11.value()
        TO11 = AO11 * PO11
        TO11 = round(TO11,2)

        AO12 = self.O12.value()
        TO12 = AO12 * PO12
        TO12 = round(TO12,2)

        if self.Bag.isChecked():
            bagPrice = PBag
        else:
            bagPrice = 0

        # Calculates the total price

        total = Decimal(TO1 + TO2 + TO3 + TO4 + TO5 + TO6 + TO7 + TO8 + TO9 + TO10 + TO11 + TO12 + bagPrice + PDeliveryFee)
        # Rounds it to prevent a glitch
        total = round(total,2)
        # Displays the total price
        self.Total.setText("${}".format(total))


class ChecklistPickup(QDialog):
    def __init__(self):
        super(ChecklistPickup, self).__init__()
        loadUi('Checklist.ui', self)
        self.setWindowTitle('Checklist Pickup')

        background = QImage("Background2.JPG")
        background_size = background.scaled(QSize(867,1154))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))

        self.setPalette(palette)

        global total

        total = 0

        global O1
        global O2
        global O3
        global O4
        global O5
        global O6
        global O7
        global O8
        global O9
        global O10
        global O11
        global O12

        global PDeliveryFee

        global PBag

        self.Total.setText("$0.00")

        self.T1.setText("{}".format(O1))
        self.T1.setAlignment(Qt.AlignCenter)

        self.T2.setText("{}".format(O2))
        self.T2.setAlignment(Qt.AlignCenter)

        self.T3.setText("{}".format(O3))
        self.T3.setAlignment(Qt.AlignCenter)

        self.T4.setText("{}".format(O4))
        self.T4.setAlignment(Qt.AlignCenter)

        self.T5.setText("{}".format(O5))
        self.T5.setAlignment(Qt.AlignCenter)

        self.T6.setText("{}".format(O6))
        self.T6.setAlignment(Qt.AlignCenter)

        self.T7.setText("{}".format(O7))
        self.T7.setAlignment(Qt.AlignCenter)

        self.T8.setText("{}".format(O8))
        self.T8.setAlignment(Qt.AlignCenter)

        self.T9.setText("{}".format(O9))
        self.T9.setAlignment(Qt.AlignCenter)

        self.T10.setText("{}".format(O10))
        self.T10.setAlignment(Qt.AlignCenter)

        self.T11.setText("{}".format(O11))
        self.T11.setAlignment(Qt.AlignCenter)

        self.T12.setText("{}".format(O12))
        self.T12.setAlignment(Qt.AlignCenter)

        self.BagBox.setText("Do you want a bag for an extra ${}".format(PBag))
        self.BagBox.setAlignment(Qt.AlignCenter)

        self.O1.valueChanged.connect(self.total_price)
        self.O1.setMinimum(0)

        self.O2.valueChanged.connect(self.total_price)
        self.O2.setMinimum(0)

        self.O3.valueChanged.connect(self.total_price)
        self.O3.setMinimum(0)

        self.O4.valueChanged.connect(self.total_price)
        self.O4.setMinimum(0)

        self.O5.valueChanged.connect(self.total_price)
        self.O5.setMinimum(0)

        self.O6.valueChanged.connect(self.total_price)
        self.O6.setMinimum(0)

        self.O7.valueChanged.connect(self.total_price)
        self.O7.setMinimum(0)

        self.O8.valueChanged.connect(self.total_price)
        self.O8.setMinimum(0)

        self.O9.valueChanged.connect(self.total_price)
        self.O9.setMinimum(0)

        self.O10.valueChanged.connect(self.total_price)
        self.O10.setMinimum(0)

        self.O11.valueChanged.connect(self.total_price)
        self.O11.setMinimum(0)

        self.O12.valueChanged.connect(self.total_price)
        self.O12.setMinimum(0)

        self.Bag.stateChanged.connect(self.total_price)

        self.Cancel.clicked.connect(self.on_cancel_clicked)
        self.Back.clicked.connect(self.on_back_clicked)
        self.Submit.clicked.connect(self.on_submit_clicked)

    def on_cancel_clicked(self):
        self.widget = Home()
        self.widget.show()
        self.hide()

    def on_back_clicked(self):
        self.widget = PickUp()
        self.widget.show()
        self.hide()

    def on_submit_clicked(self):
        global total
        if total == 0:
            self.label.setText('Please select an item')
        else:
            self.widget = FinalPickupPrice()
            self.widget.show()
            self.hide()

    def total_price(self):

        global PO1
        global PO2
        global PO3
        global PO4
        global PO5
        global PO6
        global PO7
        global PO8
        global PO9
        global PO10
        global PO11
        global PO12

        global PBag

        global total

        global AO1
        global TO1

        global AO2
        global TO2

        global AO3
        global TO3

        global AO4
        global TO4

        global AO5
        global TO5

        global AO6
        global TO6

        global AO7
        global TO7

        global AO8
        global TO8

        global AO9
        global TO9

        global AO10
        global TO10

        global AO11
        global TO11

        global AO12
        global TO12

        global bagPrice

        # A means Amount

        # T means total price

        AO1 = self.O1.value()
        TO1 = AO1 * PO1

        # Rounds the value

        TO1 = round(TO1,2)

        AO2 = self.O2.value()
        TO2 = AO2 * PO2
        TO2 = round(TO2,2)

        AO3 = self.O3.value()
        TO3 = AO3 * PO3
        TO3 = round(TO3,2)

        AO4 = self.O4.value()
        TO4 = AO4 * PO4
        TO4 = round(TO4,2)

        AO5 = self.O5.value()
        TO5 = AO5 * PO5
        TO5 = round(TO5,2)

        AO6 = self.O6.value()
        TO6 = AO6 * PO6
        TO6 = round(TO6,2)

        AO7 = self.O7.value()
        TO7 = AO7 * PO7
        TO7 = round(TO7,2)

        AO8 = self.O8.value()
        TO8 = AO8 * PO8
        TO8 = round(TO8,2)

        AO9 = self.O9.value()
        TO9 = AO9 * PO9
        TO9 = round(TO9,2)

        AO10 = self.O10.value()
        TO10 = AO10 * PO10
        TO10 = round(TO10,2)

        AO11 = self.O11.value()
        TO11 = AO11 * PO11
        TO11 = round(TO11,2)

        AO12 = self.O12.value()
        TO12 = AO12 * PO12
        TO12 = round(TO12,2)

        if self.Bag.isChecked():
            bagPrice = PBag
        else:
            bagPrice = 0

        total = Decimal(TO1 + TO2 + TO3 + TO4 + TO5 + TO6 + TO7 + TO8 + TO9 + TO10 + TO11 + TO12 + bagPrice)
        total = round(total,2)
        self.Total.setText("${}".format(total))


class FinalDeliveryPrice(QDialog):
    def __init__(self):
        super(FinalDeliveryPrice, self).__init__()
        loadUi('Price.ui', self)
        self.setWindowTitle('FinalPrice')

        background = QImage("Background3.JPG")
        background_size = background.scaled(QSize(975,1300))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))

        self.setPalette(palette)

        global name

        global address

        global phone

        global total

        global AO1
        global TO1

        global AO2
        global TO2

        global AO3
        global TO3

        global AO4
        global TO4

        global AO5
        global TO5

        global AO6
        global TO6

        global AO7
        global TO7

        global AO8
        global TO8

        global AO9
        global TO9

        global AO10
        global TO10

        global AO11
        global TO11

        global AO12
        global TO12

        global O1
        global O2
        global O3
        global O4
        global O5
        global O6
        global O7
        global O8
        global O9
        global O10
        global O11
        global O12

        global bagPrice

        global PDeliveryFee

        global SmallBoxSize
        global MediumBoxSize

        number_of_items = AO1 + AO2 + AO3 + AO4 + AO5 + AO6 + AO7 + AO8 + AO9 + AO10 + AO11 + AO12

        self.Info.setText("This order is for {}".format(name,))
        self.Adress.setText("at the address of {}".format(address))
        self.Phone.setText("Who has the phone number of {}.".format(phone))

        self.Items.setText("Items Ordered")
        self.D1.setText("Number of {} {} with the cost of ${}.".format(O1, AO1, TO1 ))
        self.D2.setText("Number of {} {} with the cost of ${}.".format(O2, AO2, TO2))
        self.D3.setText("Number of {} {} with the cost of ${}.".format(O3, AO3, TO3))
        self.D4.setText("Number of {} {} with the cost of ${}.".format(O4, AO4, TO4))
        self.D5.setText("Number of {} {} with the cost of ${}.".format(O5, AO5, TO5))
        self.D6.setText("Number of {} {} with the cost of ${}.".format(O6, AO6, TO6))
        self.D7.setText("Number of {} {} with the cost of ${}.".format(O7, AO7, TO7))
        self.D8.setText("Number of {} {} with the cost of ${}.".format(O8, AO8, TO8))
        self.D9.setText("Number of {} {} with the cost of ${}.".format(O9, AO9, TO9))
        self.D10.setText("Number of {} {} with the cost of ${}.".format(O10, AO10, TO10))
        self.D11.setText("Number of {} {} with the cost of ${}.".format(O11, AO11, TO11))
        self.D12.setText("Number of {} {} with the cost of ${}.".format(O12, AO12, TO12))

        if bagPrice == 0:
            if number_of_items <= SmallBoxSize:
                self.Box.setText("You need a small box to fit all the items in.")

            if number_of_items > SmallBoxSize:
                if number_of_items <= MediumBoxSize:
                    self.Box.setText("You need a medium box to fit all the items in.")

            if number_of_items > MediumBoxSize:
                self.Box.setText("You need a large box to fit all the items in.")
        if bagPrice >= 1:
            self.Box.setText("You have chosen a bag instead for ${}".format(bagPrice))

        self.Total.setText("Total price of ${}.".format(total))
        self.Total_2.setText("with a ${} delivery fee.".format(PDeliveryFee))

        self.Confirm.clicked.connect(self.on_confirm_clicked)
        self.Back.clicked.connect(self.on_back_clicked)

    def on_confirm_clicked(self):
        self.widget = Home()
        self.widget.show()
        self.hide()

    def on_back_clicked(self):
        self.widget = ChecklistDelivery()
        self.widget.show()
        self.hide()


class FinalPickupPrice(QDialog):
    def __init__(self):
        super(FinalPickupPrice, self).__init__()
        loadUi('Price.ui', self)
        self.setWindowTitle('FinalPrice')
        background = QImage("Background3.JPG")
        background_size = background.scaled(QSize(975,1300))
        palette = QPalette()
        palette.setBrush(10, QBrush(background_size))

        self.setPalette(palette)

        global name

        global phone

        global total

        global AO1
        global TO1

        global AO2
        global TO2

        global AO3
        global TO3

        global AO4
        global TO4

        global AO5
        global TO5

        global AO6
        global TO6

        global AO7
        global TO7

        global AO8
        global TO8

        global AO9
        global TO9

        global AO10
        global TO10

        global AO11
        global TO11

        global AO12
        global TO12

        global O1
        global O2
        global O3
        global O4
        global O5
        global O6
        global O7
        global O8
        global O9
        global O10
        global O11
        global O12

        global bagPrice

        global SmallBoxSize
        global MediumBoxSize

        number_of_items = AO1 + AO2 + AO3 + AO4 + AO5 + AO6 + AO7 + AO8 + AO9 + AO10 + AO11 + AO12

        self.Info.setText("This order is for {}".format(name,))
        self.Phone.setText("Who has the phone number of {}.".format(phone))

        self.Items.setText("Items Ordered")
        self.D1.setText("Number of {} {} with the cost of ${}.".format(O1, AO1, TO1 ))
        self.D2.setText("Number of {} {} with the cost of ${}.".format(O2, AO2, TO2))
        self.D3.setText("Number of {} {} with the cost of ${}.".format(O3, AO3, TO3))
        self.D4.setText("Number of {} {} with the cost of ${}.".format(O4, AO4, TO4))
        self.D5.setText("Number of {} {} with the cost of ${}.".format(O5, AO5, TO5))
        self.D6.setText("Number of {} {} with the cost of ${}.".format(O6, AO6, TO6))
        self.D7.setText("Number of {} {} with the cost of ${}.".format(O7, AO7, TO7))
        self.D8.setText("Number of {} {} with the cost of ${}.".format(O8, AO8, TO8))
        self.D9.setText("Number of {} {} with the cost of ${}.".format(O9, AO9, TO9))
        self.D10.setText("Number of {} {} with the cost of ${}.".format(O10, AO10, TO10))
        self.D11.setText("Number of {} {} with the cost of ${}.".format(O11, AO11, TO11))
        self.D12.setText("Number of {} {} with the cost of ${}.".format(O12, AO12, TO12))

        if bagPrice == 0:
            if number_of_items <= SmallBoxSize:
                self.Box.setText("You need a small box to fit all the items in.")

            if number_of_items > SmallBoxSize:
                if number_of_items <= MediumBoxSize:
                    self.Box.setText("You need a medium box to fit all the items in.")

            if number_of_items > MediumBoxSize:
                self.Box.setText("You need a large box to fit all the items in.")
        if bagPrice >= 1:
            self.Box.setText("You have chosen a bag instead for ${} ".format(bagPrice))

        self.Total.setText("Total price of ${}.".format(total))

        self.Confirm.clicked.connect(self.on_confirm_clicked)
        self.Back.clicked.connect(self.on_back_clicked)

    def on_confirm_clicked(self):
        self.widget = Home()
        self.widget.show()
        self.hide()

    def on_back_clicked(self):
        self.widget = ChecklistPickup()
        self.widget.show()
        self.hide()


if __name__== '__main__':
    app = QApplication(sys.argv)
    widget = Home()
    widget.show()
    sys.exit(app.exec_())
