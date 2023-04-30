import sys

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QComboBox, QMessageBox, QVBoxLayout


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance")
        self.distance_input = QLineEdit()

        time_label = QLabel("Time")
        self.time_input = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.result_label = QLabel("")

        # Add the widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_input, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_input, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

        # Increase the minimum height of the main widget
        self.setMinimumSize(QSize(500, 300))

        # Increase the minimum height of the QVBoxLayout
        vbox = QVBoxLayout()
        vbox.setContentsMargins(10, 10, 10, 10)  # set margins to create some spacing
        self.setLayout(vbox)

        # Set the size of the widget containing the layout
        self.setGeometry(100, 100, 300, 400)

    def calculate(self):
        # Get distance and time as input
        distance_str = self.distance_input.text()
        time_str = self.time_input.text()

        # Validate input
        if not distance_str or not time_str:
            # Show error message if distance or time is empty
            QMessageBox.critical(self, "Error", "Please enter values for distance and time.")
            return
        try:
            distance = float(distance_str)
            time = float(time_str)
        except ValueError:
            # Show error message if distance or time is not a valid number
            QMessageBox.critical(self, "Error", "Please enter valid values for distance and time.")
            return
        if distance < 0 or time <= 0:
            # Show error message if distance is negative or time is zero or negative
            QMessageBox.critical(self, "Error", "Please enter positive values for distance and time.")
            return

        # Check whether distance in imperial system or metric
        if self.unit_combo.currentText() == 'Metric (km)':
            distance_km = distance
            speed_unit = 'km/h'
        else:
            distance_km = distance / 1.609344# convert miles to km
            speed_unit = 'mph'

        # Calculate speed
        speed = distance_km / time
        speed_str = f"Average Speed is {round(speed, 2)} {speed_unit}"

        # Display the result
        self.result_label.setText(speed_str)


app = QApplication(sys.argv)
calculator = SpeedCalculator()
calculator.show()
sys.exit(app.exec())
