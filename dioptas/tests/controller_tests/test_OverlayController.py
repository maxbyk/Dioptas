# -*- coding: utf8 -*-

from tests.utility import QtTest
import os
import gc

import numpy as np
from PyQt4 import QtGui, QtCore
from PyQt4.QtTest import QTest

from controller.integration import OverlayController
from model import PatternModel
from widgets.integration import IntegrationWidget

unittest_path = os.path.dirname(__file__)
data_path = os.path.join(unittest_path, '../data')


class OverlayControllerTest(QtTest):

    def setUp(self):
        self.widget = IntegrationWidget()
        self.spectrum_model = PatternModel()
        self.overlay_controller = OverlayController({}, self.widget, self.spectrum_model)
        self.overlay_tw = self.widget.overlay_tw

    def tearDown(self):
        del self.widget
        del self.spectrum_model
        del self.overlay_tw
        del self.overlay_controller
        gc.collect()

    def test_manual_deleting_overlays(self):
        self.load_overlays()

        self.assertEqual(self.overlay_tw.rowCount(), 6)
        self.assertEqual(len(self.spectrum_model.overlays), 6)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 6)
        self.assertEqual(self.overlay_tw.currentRow(), 5)

        self.overlay_controller.remove_overlay_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 5)
        self.assertEqual(len(self.spectrum_model.overlays), 5)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 5)
        self.assertEqual(self.overlay_tw.currentRow(), 4)

        self.widget.select_overlay(1)
        self.overlay_controller.remove_overlay_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 4)
        self.assertEqual(len(self.spectrum_model.overlays), 4)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 4)
        self.assertEqual(self.overlay_tw.currentRow(), 1)

        self.widget.select_overlay(0)
        self.overlay_controller.remove_overlay_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 3)
        self.assertEqual(len(self.spectrum_model.overlays), 3)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 3)
        self.assertEqual(self.overlay_tw.currentRow(), 0)

        self.overlay_controller.remove_overlay_btn_click_callback()
        self.overlay_controller.remove_overlay_btn_click_callback()
        self.overlay_controller.remove_overlay_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 0)
        self.assertEqual(len(self.spectrum_model.overlays), 0)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 0)
        self.assertEqual(self.overlay_tw.currentRow(), -1)

        self.overlay_controller.remove_overlay_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 0)
        self.assertEqual(self.overlay_tw.currentRow(), -1)

    def test_automatic_deleting_overlays(self):
        self.load_overlays()
        self.load_overlays()
        QtGui.QApplication.processEvents()
        QtGui.QApplication.processEvents()
        self.assertEqual(self.overlay_tw.rowCount(), 12)
        self.assertEqual(len(self.spectrum_model.overlays), 12)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 12)

        self.overlay_controller.clear_overlays_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 0)
        self.assertEqual(len(self.spectrum_model.overlays), 0)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 0)
        self.assertEqual(self.overlay_tw.currentRow(), -1)

        multiplier = 1
        for dummy_index in range(multiplier):
            self.load_overlays()

        self.assertEqual(self.overlay_tw.rowCount(), multiplier * 6)
        self.overlay_controller.clear_overlays_btn_click_callback()
        self.assertEqual(self.overlay_tw.rowCount(), 0)
        self.assertEqual(len(self.spectrum_model.overlays), 0)
        self.assertEqual(len(self.widget.pattern_widget.overlays), 0)
        self.assertEqual(self.overlay_tw.currentRow(), -1)

    def test_change_scaling_in_view(self):
        self.load_overlays()
        self.widget.select_overlay(2)

        self.widget.overlay_scale_sb.setValue(2.0)
        self.app.processEvents()
        self.assertEqual(self.spectrum_model.get_overlay_scaling(2), 2)

        # tests if overlay is updated in spectrum
        x, y = self.spectrum_model.overlays[2].data
        x_spec, y_spec = self.widget.pattern_widget.overlays[2].getData()

        self.assertAlmostEqual(np.sum(y - y_spec), 0)

    def test_change_offset_in_view(self):
        self.load_overlays()
        self.widget.select_overlay(3)

        self.widget.overlay_offset_sb.setValue(100)
        self.assertEqual(self.spectrum_model.get_overlay_offset(3), 100)

        x, y = self.spectrum_model.overlays[3].data
        x_spec, y_spec = self.widget.pattern_widget.overlays[3].getData()

        self.assertAlmostEqual(np.sum(y - y_spec), 0)

    def test_setting_overlay_as_bkg(self):
        self.load_overlays()
        self.spectrum_model.load_pattern(os.path.join(data_path, 'spectrum_001.xy'))
        self.widget.select_overlay(0)
        QTest.mouseClick(self.widget.overlay_set_as_bkg_btn, QtCore.Qt.LeftButton)

        self.assertTrue(self.widget.overlay_set_as_bkg_btn.isChecked())

        self.assertEqual(self.spectrum_model.bkg_ind, 0)
        x, y = self.spectrum_model.pattern.data
        self.assertEqual(np.sum(y), 0)

    def test_setting_overlay_as_bkg_and_changing_scale(self):
        self.load_overlays()
        self.spectrum_model.load_pattern(os.path.join(data_path, 'spectrum_001.xy'))
        self.widget.select_overlay(0)
        QTest.mouseClick(self.widget.overlay_set_as_bkg_btn, QtCore.Qt.LeftButton)

        self.widget.overlay_scale_sb.setValue(2)
        _, y = self.spectrum_model.pattern.data
        _, y_original = self.spectrum_model.pattern.data
        self.assertEqual(np.sum(y - y_original), 0)

    def test_setting_overlay_as_bkg_and_changing_offset(self):
        self.load_overlays()
        self.spectrum_model.load_pattern(os.path.join(data_path, 'spectrum_001.xy'))
        self.widget.select_overlay(0)
        QTest.mouseClick(self.widget.overlay_set_as_bkg_btn, QtCore.Qt.LeftButton)

        self.widget.overlay_offset_sb.setValue(100)
        _, y = self.spectrum_model.pattern.data
        self.assertEqual(np.sum(y), -100 * y.size)

    def test_setting_overlay_as_bkg_and_then_change_to_new_overlay_as_bkg(self):
        self.load_overlays()
        self.spectrum_model.load_pattern(os.path.join(data_path, 'spectrum_001.xy'))
        self.widget.select_overlay(0)
        QTest.mouseClick(self.widget.overlay_set_as_bkg_btn, QtCore.Qt.LeftButton)

        _, y = self.spectrum_model.pattern.data
        self.assertEqual(np.sum(y), 0)

        self.widget.select_overlay(1)
        self.widget.overlay_scale_sb.setValue(2)
        QTest.mouseClick(self.widget.overlay_set_as_bkg_btn, QtCore.Qt.LeftButton)

        _, y = self.spectrum_model.pattern.data
        self.assertNotEqual(np.sum(y), 0)

    def test_setting_spectrum_as_bkg(self):
        self.spectrum_model.load_pattern(os.path.join(data_path, 'spectrum_001.xy'))
        QTest.mouseClick(self.widget.qa_set_as_background_btn, QtCore.Qt.LeftButton)
        QtGui.QApplication.processEvents()

        self.assertTrue(self.widget.overlay_set_as_bkg_btn.isChecked())

        _, y = self.spectrum_model.pattern.data
        self.assertEqual(np.sum(y), 0)

    def test_having_overlay_as_bkg_and_deleting_it(self):
        self.spectrum_model.load_pattern(os.path.join(data_path, 'spectrum_001.xy'))
        QTest.mouseClick(self.widget.qa_set_as_background_btn, QtCore.Qt.LeftButton)

        QTest.mouseClick(self.widget.overlay_del_btn, QtCore.Qt.LeftButton)

        self.assertFalse(self.widget.overlay_set_as_bkg_btn.isChecked())
        self.assertEqual(self.widget.overlay_tw.rowCount(), 0)

        _, y = self.spectrum_model.pattern.data
        self.assertNotEqual(np.sum(y), 0)

    def test_overlay_waterfall(self):
        self.load_overlays()
        self.widget.waterfall_separation_txt.setText("10")
        QTest.mouseClick(self.widget.waterfall_btn, QtCore.Qt.LeftButton)

        self.assertEqual(self.spectrum_model.overlays[5].offset, -10)
        self.assertEqual(self.spectrum_model.overlays[4].offset, -20)

        QTest.mouseClick(self.widget.reset_waterfall_btn, QtCore.Qt.LeftButton)

        self.assertEqual(self.spectrum_model.overlays[5].offset, 0)
        self.assertEqual(self.spectrum_model.overlays[5].offset, 0)

    def load_overlays(self):
        self.load_overlay('spectrum_001.xy')
        self.load_overlay('spectrum_001.xy')
        self.load_overlay('spectrum_001.xy')
        self.load_overlay('spectrum_001.xy')
        self.load_overlay('spectrum_001.xy')
        self.load_overlay('spectrum_001.xy')

    def load_overlay(self, filename):
        self.overlay_controller.add_overlay_btn_click_callback(os.path.join(data_path, filename))


if __name__ == '__main__':
    unittest.main()
