import unittest
from mock import MagicMock
import sys
import os
import gc

import numpy as np

from PyQt4 import QtGui, QtCore

from controller import MainController

unittest_path = os.path.dirname(__file__)
data_path = os.path.join(unittest_path, os.pardir, 'data')

app = QtGui.QApplication([])


class UserInterFaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QtGui.QApplication([])

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()
        cls.app.deleteLater()

    def setUp(self):
        self.controller = MainController(use_settings=False)
        self.img_model = self.controller.img_model
        self.mask_model = self.controller.mask_model
        self.spectrum_model = self.controller.spectrum_model
        self.calibration_model = self.controller.calibration_model
        self.calibration_model.integrate_1d = MagicMock(return_value=(self.calibration_model.tth,
                                                                      self.calibration_model.int))
        self.phase_model = self.controller.phase_model

        self.calibration_widget = self.controller.widget.calibration_widget
        self.mask_widget = self.controller.widget.mask_widget
        self.integration_widget = self.controller.widget.integration_widget

        self.integration_controller = self.controller.integration_controller
        self.calibration_model.load(os.path.join(data_path, 'CeO2_Pilatus1M.poni'))
        self.img_model.load(os.path.join(data_path, 'CeO2_Pilatus1M.tif'))

        self.integration_spectrum_controller = self.integration_controller.spectrum_controller
        self.integration_image_controller = self.integration_controller.image_controller

    def tearDown(self):
        del self.integration_spectrum_controller
        del self.mask_model
        del self.img_model
        del self.calibration_model.cake_geometry
        del self.calibration_model.spectrum_geometry
        del self.calibration_model
        del self.integration_widget
        del self.integration_controller
        gc.collect()

    def test_synchronization_of_view_range(self):
        # calibration and mask view
        self.calibration_widget.img_widget.img_view_box.setRange(QtCore.QRectF(-10, -10, 20, 20))
        self.controller.widget.tabWidget.setCurrentIndex(1)

        self.assertAlmostEqual(np.sum(np.array(self.calibration_widget.img_widget.img_view_box.targetRange()) - \
                                      np.array(self.mask_widget.img_widget.img_view_box.targetRange())), 0)

        self.mask_widget.img_widget.img_view_box.setRange(QtCore.QRectF(100, 100, 300, 300))
        self.controller.widget.tabWidget.setCurrentIndex(0)

        self.assertAlmostEqual(np.sum(np.array(self.calibration_widget.img_widget.img_view_box.targetRange()) - \
                                      np.array(self.mask_widget.img_widget.img_view_box.targetRange())), 0)
