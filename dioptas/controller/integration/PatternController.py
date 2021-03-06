# -*- coding: utf8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray data
# Copyright (C) 2015  Clemens Prescher (clemens.prescher@gmail.com)
# Institute for Geology and Mineralogy, University of Cologne
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

import numpy as np
import pyFAI
from PyQt4 import QtGui, QtCore


# imports for type hinting in PyCharm -- DO NOT DELETE


class PatternController(object):
    """
    IntegrationSpectrumController handles all the interaction from the IntegrationView with the spectrum data.
    It manages the auto integration of image files to spectra in addition to spectrum browsing and changing of units
    (2 Theta, Q, A)
    """

    def __init__(self, working_dir, widget, img_model, mask_model, calibration_model, spectrum_model):
        """
        :param working_dir: dictionary of working directories
        :param widget: Reference to an IntegrationWidget
        :param img_model: reference to ImgModel object
        :param mask_model: reference to MaskModel object
        :param calibration_model: reference to CalibrationModel object
        :param spectrum_model: reference to SpectrumModel object

        :type widget: IntegrationWidget
        :type img_model: ImgModel
        :type mask_model: MaskModel
        :type calibration_model: CalibrationModel
        :type spectrum_model: PatternModel
        """

        self.working_dir = working_dir
        self.widget = widget
        self.img_model = img_model
        self.mask_model = mask_model
        self.calibration_model = calibration_model
        self.spectrum_model = spectrum_model

        self.integration_unit = '2th_deg'
        self.autocreate_pattern = False
        self.unit = pyFAI.units.TTH_DEG

        self.create_subscriptions()
        self.create_gui_signals()

    def create_subscriptions(self):
        # Data subscriptions
        self.img_model.img_changed.connect(self.image_changed)
        self.spectrum_model.pattern_changed.connect(self.plot_pattern)
        self.spectrum_model.pattern_changed.connect(self.autocreate_spectrum)

        # Gui subscriptions
        self.widget.img_widget.roi.sigRegionChangeFinished.connect(self.image_changed)
        self.widget.pattern_widget.mouse_left_clicked.connect(self.pattern_left_click)
        self.widget.pattern_widget.mouse_moved.connect(self.show_pattern_mouse_position)

    def create_gui_signals(self):
        """
        creating callbacks for the ui controls
        """

        # file callbacks
        self.connect_click_function(self.widget.spec_autocreate_cb, self.autocreate_cb_changed)
        self.connect_click_function(self.widget.spec_load_btn, self.load)
        self.connect_click_function(self.widget.spec_previous_btn, self.load_previous)
        self.connect_click_function(self.widget.spec_next_btn, self.load_next)
        self.widget.spec_filename_txt.editingFinished.connect(self.filename_txt_changed)

        self.connect_click_function(self.widget.spec_directory_btn, self.spec_directory_btn_click)
        self.connect_click_function(self.widget.spec_browse_by_name_rb, self.set_iteration_mode_number)
        self.connect_click_function(self.widget.spec_browse_by_time_rb, self.set_iteration_mode_time)

        self.widget.connect(self.widget.spec_directory_txt,
                            QtCore.SIGNAL('editingFinished()'),
                            self.spec_directory_txt_changed)

        # unit callbacks
        self.connect_click_function(self.widget.spec_tth_btn, self.set_unit_tth)
        self.connect_click_function(self.widget.spec_q_btn, self.set_unit_q)
        self.connect_click_function(self.widget.spec_d_btn, self.set_unit_d)

        # quick actions
        self.connect_click_function(self.widget.qa_save_spectrum_btn, self.save_pattern)

        # integration controls
        self.widget.automatic_binning_cb.stateChanged.connect(self.automatic_binning_cb_changed)
        self.widget.bin_count_txt.editingFinished.connect(self.image_changed)
        self.widget.supersampling_sb.valueChanged.connect(self.supersampling_changed)

        # spectrum_plot interaction
        self.widget.keyPressEvent = self.key_press_event

        # spectrum_plot auto range functions
        self.connect_click_function(self.widget.spec_auto_range_btn, self.spec_auto_range_btn_click_callback)
        self.widget.pattern_widget.auto_range_status_changed.connect(self.widget.spec_auto_range_btn.setChecked)

        # spectrum_plot antialias
        self.widget.antialias_btn.toggled.connect(self.widget.pattern_widget.set_antialias)

    def connect_click_function(self, emitter, function):
        self.widget.connect(emitter, QtCore.SIGNAL('clicked()'), function)

    def image_changed(self):
        self.widget.img_widget.roi.blockSignals(True)
        if self.calibration_model.is_calibrated:
            if self.widget.img_mask_btn.isChecked():
                if self.mask_model.supersampling_factor != self.img_model.supersampling_factor:
                    self.mask_model.set_supersampling(self.img_model.supersampling_factor)
                mask = self.mask_model.get_mask()
            else:
                mask = None

            if self.widget.img_roi_btn.isChecked():
                roi_mask = self.widget.img_widget.roi.getRoiMask(self.img_model.img_data.shape)
            else:
                roi_mask = None

            if roi_mask is None and mask is None:
                mask = None
            elif roi_mask is None and mask is not None:
                mask = mask
            elif roi_mask is not None and mask is None:
                mask = roi_mask
            elif roi_mask is not None and mask is not None:
                mask = np.logical_or(mask, roi_mask)

            if not self.widget.automatic_binning_cb.isChecked():
                num_points = int(str(self.widget.bin_count_txt.text()))
            else:
                num_points = None

            x, y = self.calibration_model.integrate_1d(mask=mask, unit=self.integration_unit, num_points=num_points)
            self.widget.bin_count_txt.setText(str(self.calibration_model.num_points))

            self.spectrum_model.set_pattern(x, y, self.img_model.filename, unit=self.integration_unit)

            if self.autocreate_pattern:
                filename = self.img_model.filename
                file_endings = self.get_spectrum_file_endings()
                for file_ending in file_endings:
                    if filename is not '':
                        filename = os.path.join(
                            self.working_dir['spectrum'],
                            os.path.basename(
                                str(self.img_model.filename)).split('.')[:-1][0] + file_ending)
                    self.save_pattern(filename)
                self.widget.spec_next_btn.setEnabled(True)
                self.widget.spec_previous_btn.setEnabled(True)
                self.widget.spec_filename_txt.setText(os.path.basename(filename))
                self.widget.spec_directory_txt.setText(os.path.dirname(filename))
            else:
                self.widget.spec_next_btn.setEnabled(False)
                self.widget.spec_previous_btn.setEnabled(False)
                self.widget.spec_filename_txt.setText(
                    'No File saved or selected')
        self.widget.img_widget.roi.blockSignals(False)

    def get_spectrum_file_endings(self):
        res = []
        if self.widget.spectrum_header_xy_cb.isChecked():
            res.append('.xy')
        if self.widget.spectrum_header_chi_cb.isChecked():
            res.append('.chi')
        if self.widget.spectrum_header_dat_cb.isChecked():
            res.append('.dat')
        return res

    def plot_pattern(self):
        if self.widget.bkg_spectrum_inspect_btn.isChecked():
            self.widget.pattern_widget.plot_data(
                *self.spectrum_model.pattern.auto_background_before_subtraction_spectrum.data,
                name=self.spectrum_model.pattern.name)
            self.widget.pattern_widget.plot_bkg(*self.spectrum_model.pattern.auto_background_pattern.data)
        else:
            self.widget.pattern_widget.plot_data(
                *self.spectrum_model.pattern.data, name=self.spectrum_model.pattern.name)
            self.widget.pattern_widget.plot_bkg([], [])

        # update the bkg_name
        if self.spectrum_model.bkg_ind is not -1:
            self.widget.bkg_name_lbl.setText('Bkg: ' + self.spectrum_model.overlays[self.spectrum_model.bkg_ind].name)
        else:
            self.widget.bkg_name_lbl.setText('')

    def reset_background(self, popup=True):
        self.widget.overlay_show_cb_set_checked(self.spectrum_model.bkg_ind, True)  # show the old overlay again
        self.spectrum_model.bkg_ind = -1
        self.spectrum_model.pattern.unset_background_spectrum()
        self.widget.overlay_set_as_bkg_btn.setChecked(False)

    def automatic_binning_cb_changed(self):
        current_value = self.widget.automatic_binning_cb.isChecked()
        self.widget.bin_count_txt.setEnabled(not current_value)
        if current_value:
            self.image_changed()

    def supersampling_changed(self, value):
        self.calibration_model.set_supersampling(value)
        self.img_model.set_supersampling(value)
        self.image_changed()

    def autocreate_spectrum(self):
        if self.spectrum_model.pattern.has_background():
            if self.autocreate_pattern is True:
                file_endings = self.get_spectrum_file_endings()
                for file_ending in file_endings:
                    directory = os.path.join(
                        self.working_dir['spectrum'], 'bkg_subtracted')
                    if not os.path.exists(directory):
                        os.mkdir(directory)
                    filename = os.path.join(
                        directory,
                        self.spectrum_model.pattern.name + file_ending)
                    self.save_pattern(filename, subtract_background=True)

    def save_pattern(self, filename=None, subtract_background=False):
        if filename is None:
            img_filename, _ = os.path.splitext(os.path.basename(self.img_model.filename))
            filename = str(QtGui.QFileDialog.getSaveFileName(self.widget, "Save Spectrum Data.",
                                                             os.path.join(self.working_dir['spectrum'],
                                                                          img_filename + '.xy'),
                                                             ('Data (*.xy);;Data (*.chi);;Data (*.dat);;png (*.png);;svg (*.svg)')))
            subtract_background = True  # when manually saving the spectrum the background will be automatically

        if filename is not '':
            print(filename)
            if filename.endswith('.xy'):
                header = self.calibration_model.create_file_header()
                if subtract_background:
                    if self.spectrum_model.bkg_ind is not -1:
                        header += "\n# \n# BackgroundFile: " + self.spectrum_model.overlays[
                            self.spectrum_model.bkg_ind].name
                header = header.replace('\r\n', '\n')
                header += '\n#\n# ' + self.integration_unit + '\t I'

                self.spectrum_model.save_pattern(filename, header, subtract_background)
            elif filename.endswith('.chi'):
                self.spectrum_model.save_pattern(filename, subtract_background=subtract_background)
            elif filename.endswith('.dat'):
                self.spectrum_model.save_pattern(filename, subtract_background=subtract_background)
            elif filename.endswith('.png'):
                self.widget.pattern_widget.save_png(filename)
            elif filename.endswith('.svg'):
                self.widget.pattern_widget.save_svg(filename)

    def load(self, filename=None):
        if filename is None:
            filename = str(QtGui.QFileDialog.getOpenFileName(
                self.widget, caption="Load Spectrum",
                directory=self.working_dir['spectrum']))
        if filename is not '':
            self.working_dir['spectrum'] = os.path.dirname(filename)
            self.widget.spec_filename_txt.setText(os.path.basename(filename))
            self.widget.spec_directory_txt.setText(os.path.dirname(filename))
            self.spectrum_model.load_pattern(filename)
            self.widget.spec_next_btn.setEnabled(True)
            self.widget.spec_previous_btn.setEnabled(True)

    def load_previous(self):
        step = int(str(self.widget.spec_browse_step_txt.text()))
        self.spectrum_model.load_previous_file(step=step)
        self.widget.spec_filename_txt.setText(
            os.path.basename(self.spectrum_model.pattern_filename))

    def load_next(self):
        step = int(str(self.widget.spec_browse_step_txt.text()))
        self.spectrum_model.load_next_file(step=step)
        self.widget.spec_filename_txt.setText(
            os.path.basename(self.spectrum_model.pattern_filename))

    def autocreate_cb_changed(self):
        self.autocreate_pattern = self.widget.spec_autocreate_cb.isChecked()

    def filename_txt_changed(self):
        current_filename = os.path.basename(self.spectrum_model.pattern_filename)
        current_directory = str(self.widget.spec_directory_txt.text())
        new_filename = str(self.widget.spec_filename_txt.text())
        if os.path.isfile(os.path.join(current_directory, new_filename)):
            try:
                self.load(os.path.join(current_directory, new_filename))
            except TypeError:
                self.widget.spec_filename_txt.setText(current_filename)
        else:
            self.widget.spec_filename_txt.setText(current_filename)

    def spec_directory_btn_click(self):
        directory = QtGui.QFileDialog.getExistingDirectory(
            self.widget,
            "Please choose the default directory for autosaved spectra.",
            self.working_dir['spectrum'])
        if directory is not '':
            self.working_dir['spectrum'] = str(directory)
            self.widget.spec_directory_txt.setText(directory)

    def spec_directory_txt_changed(self):
        if os.path.exists(self.widget.spec_directory_txt.text()):
            self.working_dir['spectrum'] = str(self.widget.spec_directory_txt.text())
        else:
            self.widget.spec_directory_txt.setText(self.working_dir['spectrum'])

    def set_iteration_mode_number(self):
        self.spectrum_model.set_file_iteration_mode('number')

    def set_iteration_mode_time(self):
        self.spectrum_model.set_file_iteration_mode('time')

    def set_unit_tth(self):
        self.widget.spec_tth_btn.setChecked(True)
        self.widget.spec_q_btn.setChecked(False)
        self.widget.spec_d_btn.setChecked(False)
        previous_unit = self.integration_unit
        if previous_unit == '2th_deg':
            return
        self.integration_unit = '2th_deg'
        self.widget.pattern_widget.spectrum_plot.setLabel('bottom', u'2θ', '°')
        self.widget.pattern_widget.spectrum_plot.invertX(False)
        if self.calibration_model.is_calibrated:
            self.update_x_range(previous_unit, self.integration_unit)
            self.image_changed()
            self.update_line_position(previous_unit, self.integration_unit)

    def set_unit_q(self):
        self.widget.spec_tth_btn.setChecked(False)
        self.widget.spec_q_btn.setChecked(True)
        self.widget.spec_d_btn.setChecked(False)
        previous_unit = self.integration_unit
        if previous_unit == 'q_A^-1':
            return
        self.integration_unit = "q_A^-1"

        self.widget.pattern_widget.spectrum_plot.invertX(False)
        self.widget.pattern_widget.spectrum_plot.setLabel(
            'bottom', 'Q', 'A<sup>-1</sup>')
        if self.calibration_model.is_calibrated:
            self.update_x_range(previous_unit, self.integration_unit)
            self.image_changed()
            self.update_line_position(previous_unit, self.integration_unit)

    def set_unit_d(self):
        self.widget.spec_tth_btn.setChecked(False)
        self.widget.spec_q_btn.setChecked(False)
        self.widget.spec_d_btn.setChecked(True)
        previous_unit = self.integration_unit
        if previous_unit == 'd_A':
            return

        self.widget.pattern_widget.spectrum_plot.setLabel(
            'bottom', 'd', 'A'
        )
        self.widget.pattern_widget.spectrum_plot.invertX(True)
        self.integration_unit = 'd_A'
        if self.calibration_model.is_calibrated:
            self.update_x_range(previous_unit, self.integration_unit)
            self.image_changed()
            self.update_line_position(previous_unit, self.integration_unit)

    def update_x_range(self, previous_unit, new_unit):
        old_x_axis_range = self.widget.pattern_widget.spectrum_plot.viewRange()[0]
        spectrum_x = self.spectrum_model.pattern.data[0]
        if np.min(spectrum_x) < old_x_axis_range[0] or np.max(spectrum_x) > old_x_axis_range[1]:
            new_x_axis_range = self.convert_x_value(np.array(old_x_axis_range), previous_unit, new_unit)
            self.widget.pattern_widget.spectrum_plot.setRange(xRange=new_x_axis_range, padding=0)

    def spec_auto_range_btn_click_callback(self):
        self.widget.pattern_widget.auto_range = self.widget.spec_auto_range_btn.isChecked()

    def update_line_position(self, previous_unit, new_unit):
        cur_line_pos = self.widget.pattern_widget.pos_line.getPos()[0]
        if cur_line_pos == 0 and new_unit == 'd_A':
            cur_line_pos = 0.01
        try:
            new_line_pos = self.convert_x_value(cur_line_pos, previous_unit, new_unit)
        except RuntimeWarning:  # no calibration available
            new_line_pos = cur_line_pos
        self.widget.pattern_widget.set_pos_line(new_line_pos)

    def convert_x_value(self, value, previous_unit, new_unit):
        wavelength = self.calibration_model.wavelength
        if previous_unit == '2th_deg':
            tth = value
        elif previous_unit == 'q_A^-1':
            tth = np.arcsin(
                value * 1e10 * wavelength / (4 * np.pi)) * 360 / np.pi
        elif previous_unit == 'd_A':
            tth = 2 * np.arcsin(wavelength / (2 * value * 1e-10)) * 180 / np.pi
        else:
            tth = 0

        if new_unit == '2th_deg':
            res = tth
        elif new_unit == 'q_A^-1':
            res = 4 * np.pi * \
                  np.sin(tth / 360 * np.pi) / \
                  wavelength / 1e10
        elif new_unit == 'd_A':
            res = wavelength / (2 * np.sin(tth / 360 * np.pi)) * 1e10
        else:
            res = 0
        return res

    def pattern_left_click(self, x, y):
        self.set_line_position(x)

        self.widget.click_tth_lbl.setText(self.widget.mouse_tth_lbl.text())
        self.widget.click_d_lbl.setText(self.widget.mouse_d_lbl.text())
        self.widget.click_q_lbl.setText(self.widget.mouse_q_lbl.text())
        self.widget.click_azi_lbl.setText(self.widget.mouse_azi_lbl.text())

    def set_line_position(self, x):
        self.widget.pattern_widget.set_pos_line(x)
        if self.calibration_model.is_calibrated:
            self.update_image_widget_line_position()

    def get_line_tth(self):
        x = self.widget.pattern_widget.get_pos_line()
        if self.integration_unit == 'q_A^-1':
            x = self.convert_x_value(x, 'q_A^-1', '2th_deg')
        elif self.integration_unit == 'd_A':
            x = self.convert_x_value(x, 'd_A', '2th_deg')
        return x

    def update_image_widget_line_position(self):
        tth = self.get_line_tth()
        if self.widget.img_mode_btn.text() == 'Image':  # cake mode, button shows always opposite
            self.set_cake_line_position(tth)
        else:  # image mode
            self.set_image_line_position(tth)

    def set_cake_line_position(self, tth):
        upper_ind = np.where(self.calibration_model.cake_tth > tth)
        lower_ind = np.where(self.calibration_model.cake_tth < tth)
        spacing = self.calibration_model.cake_tth[upper_ind[0][0]] - self.calibration_model.cake_tth[lower_ind[-1][-1]]
        new_pos = lower_ind[-1][-1] + (tth - self.calibration_model.cake_tth[lower_ind[-1][-1]]) / spacing + 0.5
        self.widget.img_widget.vertical_line.setValue(new_pos)

    def set_image_line_position(self, tth):
        if self.calibration_model.is_calibrated:
            self.widget.img_widget.set_circle_line(
                self.calibration_model.get_two_theta_array(), tth / 180 * np.pi)

    def show_pattern_mouse_position(self, x, _):
        tth_str, d_str, q_str, azi_str = self.get_position_strings(x)
        self.widget.mouse_tth_lbl.setText(tth_str)
        self.widget.mouse_d_lbl.setText(d_str)
        self.widget.mouse_q_lbl.setText(q_str)
        self.widget.mouse_azi_lbl.setText(azi_str)

    def get_position_strings(self, x):
        if self.calibration_model.is_calibrated:
            if self.integration_unit == '2th_deg':
                tth = x
                q_value = self.convert_x_value(tth, '2th_deg', 'q_A^-1')
                d_value = self.convert_x_value(tth, '2th_deg', 'd_A')
            elif self.integration_unit == 'q_A^-1':
                q_value = x
                tth = self.convert_x_value(q_value, 'q_A^-1', '2th_deg')
                d_value = self.convert_x_value(q_value, 'q_A^-1', 'd_A')
            elif self.integration_unit == 'd_A':
                d_value = x
                q_value = self.convert_x_value(d_value, 'd_A', 'q_A^-1')
                tth = self.convert_x_value(d_value, 'd_A', '2th_deg')

            tth_str = u'2θ:%9.3f  ' % tth
            d_str = 'd:%9.3f  ' % d_value
            q_str = 'Q:%9.3f  ' % q_value
        else:
            tth_str = u'2θ: -'
            d_str = 'd: -'
            q_str = 'Q: -'
            if self.integration_unit == '2th_deg':
                tth_str = u'2θ:%9.3f  ' % x
            elif self.integration_unit == 'q_A^-1':
                q_str = 'Q:%9.3f  ' % x
            elif self.integration_unit == 'd_A':
                d_str = 'd:%9.3f  ' % x
        azi_str = 'X: -'
        return tth_str, d_str, q_str, azi_str

    def key_press_event(self, ev):
        if (ev.key() == QtCore.Qt.Key_Left) or (ev.key() == QtCore.Qt.Key_Right):
            pos = self.widget.pattern_widget.get_pos_line()
            step = np.min(np.diff(self.spectrum_model.pattern.data[0]))
            if ev.modifiers() & QtCore.Qt.ControlModifier:
                step /= 20.
            elif ev.modifiers() & QtCore.Qt.ShiftModifier:
                step *= 10
            if self.integration_unit == 'd_A':
                step *= -1
            if ev.key() == QtCore.Qt.Key_Left:
                new_pos = pos - step
            elif ev.key() == QtCore.Qt.Key_Right:
                new_pos = pos + step
            self.set_line_position(new_pos)
            self.update_image_widget_line_position()

            tth_str, d_str, q_str, azi_str = self.get_position_strings(new_pos)
            self.widget.click_tth_lbl.setText(tth_str)
            self.widget.click_d_lbl.setText(d_str)
            self.widget.click_q_lbl.setText(q_str)
            self.widget.click_azi_lbl.setText(azi_str)
