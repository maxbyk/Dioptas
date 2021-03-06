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

import logging

from copy import copy
from PyQt4 import QtCore
import numpy as np

from model.util.HelperModule import FileNameIterator, get_base_name
from model.util import Pattern

logger = logging.getLogger(__name__)


class PatternModel(QtCore.QObject):
    """
    Main Pattern handling class. Supporting several features:
      - loading spectra from any tabular source (readable by numpy)
      - having overlays
      - setting overlays as background
      - spectra and overlays can be scaled and have offset values

    all changes to the internal data throw pyqtSignals.
    """
    pattern_changed = QtCore.pyqtSignal()
    overlay_changed = QtCore.pyqtSignal(int)  # changed index
    overlay_added = QtCore.pyqtSignal()
    overlay_removed = QtCore.pyqtSignal(int)  # removed index
    overlay_set_as_bkg = QtCore.pyqtSignal(int)  # index set as background
    overlay_unset_as_bkg = QtCore.pyqtSignal(int)  # index unset os background

    def __init__(self):
        super(PatternModel, self).__init__()
        self.pattern = Pattern()
        self.overlays = []
        self.phases = []

        self.file_iteration_mode = 'number'
        self.file_name_iterator = FileNameIterator()

        self.bkg_ind = -1
        self.pattern_filename = ''

    def set_pattern(self, x, y, filename='', unit=''):
        """
        set the current data spectrum.
        :param x: x-values
        :param y: y-values
        :param filename: name for the spectrum, defaults to ''
        :param unit: unit for the x values
        """
        self.pattern_filename = filename
        self.pattern.data = (x, y)
        self.pattern.name = get_base_name(filename)
        self.unit = unit
        self.pattern_changed.emit()

    def load_pattern(self, filename):
        """
        Loads a spectrum from a tabular spectrum file (2 column txt file)
        :param filename: filename of the data file
        """
        logger.info("Load spectrum: {0}".format(filename))
        self.pattern_filename = filename

        skiprows = 0
        if filename.endswith('.chi'):
            skiprows = 4
        self.pattern.load(filename, skiprows)
        self.file_name_iterator.update_filename(filename)
        self.pattern_changed.emit()

    def save_pattern(self, filename, header=None, subtract_background=False):
        """
        Saves the current data spectrum.
        :param filename: where to save
        :param header: you can specify any specific header
        :param subtract_background: whether or not the background set will be used for saving or not
        """
        if subtract_background:
            x, y = self.pattern.data
        else:
            x, y = self.pattern._original_x, self.pattern._original_y

        file_handle = open(filename, 'w')
        num_points = len(x)

        if filename.endswith('.chi'):
            if header is None or header == '':
                file_handle.write(filename + '\n')
                file_handle.write(self.unit + '\n\n')
                file_handle.write("       {0}\n".format(num_points))
            else:
                file_handle.write(header)
            for ind in range(num_points):
                file_handle.write(' {0:.7E}  {1:.7E}\n'.format(x[ind], y[ind]))
        else:
            if header is not None:
                file_handle.write(header)
                file_handle.write('\n')
            for ind in range(num_points):
                file_handle.write('{0:.9E}  {1:.9E}\n'.format(x[ind], y[ind]))
        file_handle.close()

    def get_spectrum(self):
        return self.pattern

    def load_next_file(self, step=1):
        """
        Loads the next file from a sequel of filenames (e.g. *_001.xy --> *_002.xy)
        It assumes that the file numbers are at the end of the filename
        """
        next_file_name = self.file_name_iterator.get_next_filename(mode=self.file_iteration_mode, step=step)
        if next_file_name is not None:
            self.load_pattern(next_file_name)
            return True
        return False

    def load_previous_file(self, step=1):
        """
        Loads the previous file from a sequel of filenames (e.g. *_002.xy --> *_001.xy)
        It assumes that the file numbers are at the end of the filename
        """
        next_file_name = self.file_name_iterator.get_previous_filename(mode=self.file_iteration_mode, step=step)
        if next_file_name is not None:
            self.load_pattern(next_file_name)
            return True
        return False

    def set_file_iteration_mode(self, mode):
        if mode == 'number':
            self.file_iteration_mode = 'number'
            self.file_name_iterator.create_timed_file_list = False
        elif mode == 'time':
            self.file_iteration_mode = 'time'
            self.file_name_iterator.create_timed_file_list = True
            self.file_name_iterator.update_filename(self.filename)

    def add_overlay(self, x, y, name=''):
        """
        Adds an overlay to the list of overlays
        :param x: x-values
        :param y: y-values
        :param name: name of overlay to be used for displaying etc.
        """
        self.overlays.append(Pattern(x, y, name))
        self.overlay_added.emit()

    def remove_overlay(self, ind):
        """
        Removes an overlay from the list of overlays
        :param ind: index of the overlay
        """
        if ind >= 0:
            del self.overlays[ind]
            if self.bkg_ind > ind:
                self.bkg_ind -= 1
            elif self.bkg_ind == ind:
                self.pattern.unset_background_spectrum()
                self.bkg_ind = -1
                self.pattern_changed.emit()
            self.overlay_removed.emit(ind)

    def get_overlay(self, ind):
        """
        :param ind: overlay ind
        :return: returns overlay if existent or None if it does not exist
        :type return: Pattern
        """
        try:
            return self.overlays[ind]
        except IndexError:
            return None

    def add_spectrum_as_overlay(self):
        """
        Adds the current data spectrum as overlay to the list of overlays
        """
        overlay_spectrum = Pattern(np.copy(self.pattern.x),
                                   np.copy(self.pattern.y),
                                   copy(self.pattern.name))
        self.overlays.append(overlay_spectrum)
        self.overlay_added.emit()

    def add_overlay_file(self, filename):
        """
        Reads a 2-column (x,y) text file and adds it as overlay to the list of overlays
        :param filename: path of the file to be loaded
        """
        self.overlays.append(Pattern())
        self.overlays[-1].load(filename)
        self.overlay_added.emit()

    def get_overlay_name(self, ind):
        """
        :param ind: overlay index
        """
        return self.overlays[-1].name

    def set_overlay_scaling(self, ind, scaling):
        """
        Sets the scaling of the specified overlay
        :param ind: index of the overlay
        :param scaling: new scaling value
        """
        self.overlays[ind].scaling = scaling
        self.overlay_changed.emit(ind)
        if self.bkg_ind == ind:
            self.pattern_changed.emit()

    def get_overlay_scaling(self, ind):
        """
        Returns the scaling of the specified overlay
        :param ind: index of the overlay
        :return: scaling value
        """
        return self.overlays[ind].scaling

    def set_overlay_offset(self, ind, offset):
        """
        Sets the offset of the specified overlay
        :param ind: index of the overlay
        :param offset: new offset value
        """
        self.overlays[ind].offset = offset
        self.overlay_changed.emit(ind)
        if self.bkg_ind == ind:
            self.pattern_changed.emit()

    def get_overlay_offset(self, ind):
        """
        Return the offset of the specified overlay
        :param ind: index of the overlay
        :return: overlay value
        """
        return self.overlays[ind].offset

    def set_overlay_as_bkg(self, ind):
        """
        Sets an overlay as background for the data spectrum, and unsets any previously used background
        :param ind: index of the overlay
        """
        if self.bkg_ind >= 0:
            self.unset_overlay_as_bkg()
        self.bkg_ind = ind
        self.pattern.background_pattern = self.overlays[ind]
        self.pattern_changed.emit()
        self.overlay_set_as_bkg.emit(ind)

    def set_spectrum_as_bkg(self):
        """
        Adds the current spectrum as Overlay and sets it as background spectrum and unsets any previously used
        background.
        """
        self.add_spectrum_as_overlay()
        self.set_overlay_as_bkg(len(self.overlays) - 1)

    def unset_overlay_as_bkg(self):
        """
        Unsets the currently used background overlay.
        """
        previous_bkg_ind = self.bkg_ind
        self.bkg_ind = -1
        self.pattern.unset_background_spectrum()
        self.pattern_changed.emit()
        self.overlay_unset_as_bkg.emit(previous_bkg_ind)

    def overlay_is_bkg(self, ind):
        """
        :param ind: overlay ind
        """
        return ind == self.bkg_ind and self.bkg_ind != -1

    def set_auto_background_subtraction(self, parameters, roi=None):
        """
        Enables auto background extraction and removal from the data spectrum
        :param parameters: array of parameters with [window_width, iterations, polynomial_order]
        :param roi: array of size two with [xmin, xmax] specifying the range for which the background subtraction
        will be performed
        """
        self.pattern.set_auto_background_subtraction(parameters, roi)
        self.pattern_changed.emit()

    def unset_auto_background_subtraction(self):
        """
        Disables auto background extraction and removal.
        """
        self.pattern.unset_auto_background_subtraction()
        self.pattern_changed.emit()

    def overlay_waterfall(self, separation):
        offset = 0
        for ind in range(len(self.overlays)):
            if ind != self.bkg_ind:
                offset -= separation
                self.overlays[-(ind + 1)].offset = offset
                self.overlay_changed.emit(len(self.overlays) - (ind + 1))

    def reset_overlay_offsets(self):
        for ind, overlay in enumerate(self.overlays):
            overlay.offset = 0
            self.overlay_changed.emit(ind)
