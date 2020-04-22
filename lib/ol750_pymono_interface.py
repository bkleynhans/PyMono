###
#
#
#
# Program Description :
# Created By          : Benjamin Kleynhans
# Creation Date       : March 19, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : March 19, 2020
# Filename            : ol750_pymono_interface.py
#
###

import pdb
import time

from lib.ol750_420_python_api import OL750_420_Python_Api
import lib.pymono_exceptions as pymono_exceptions

class OL750_PyMono_Interface():

    def __init__(self, root, master, args):

        self.root = root
        self.master = master
        self.args = args

        self._build_lists()

        self.ol750 = OL750_420_Python_Api(args)


    def update_lists(self):

        self._build_lists()

    # Launch the local function that opens the connection to the OL750
    def open_connection(self):

        return self._serial_open()

    # Launch the local function that closes the connection to the OL750
    def close_connection(self):

        return self._close_comm()

    # Launch the local function that starts collecting sample data from the OL750
    def start_sampling(self):

        try:
            # self._reset()
            # self._setup_gratings()
            self._run_sample()

        except:
            raise
        else:
            return 0


    def _build_lists(self):

        self.grating_lower_wavelength = []
        self.grating_upper_wavelength = []
        self.grating_grooves = []
        self.grating_skew = []

        # The OL750 in use at RIT CIS only has one turret, therefore we only
        # perform the setup for the first turret.
        turret = self.root.preferences['gratings']['turret_1']

        for grating in turret:
            self.grating_lower_wavelength.append(float(turret[grating]['lower_effective_wavelength']))
            self.grating_upper_wavelength.append(float(turret[grating]['upper_effective_wavelength']))
            self.grating_grooves.append(float(turret[grating]['grooves_per_millimeter']))
            self.grating_skew.append(float(turret[grating]['grating_alignment_angle']))

        # The following values are predefined, because the OL750 in use at RIT CIS
        # does not have the "automated entrance and exit slit" features.  These values
        # were provided by Chris Gordon, Product Scientist from Optronic Laboratories.
        #
        # Chris Gordon <Chris.Gordon@optroniclabs.com>
        # 4632 36th Street, Orlando Florida, 32811, USA
        #
        self.grating_entrance = [-1, -1, -1]
        self.grating_exit = [-1, -1, -1]
        self.entrance_home_offset = 0
        self.exit_home_offset = 0

    # Get the preferences and attempt to open the connection to the OL750
    def _serial_open(self):

        status = 0

        try:
            # We connect to the OL750 with the number of the serial port only eg. 07
            com_port = int(self.root.preferences['connection']['port'][-2:])
            result = self.ol750.SerialOpen(com_port)

            if result == 1:
                raise pymono_exceptions.OL750_FailedToConnect_Exception
            elif result == 31:
                raise pymono_exceptions.OL750_InvalidPortNumber_Exception
            else:
                raise

        except pymono_exceptions.OL750_FailedToConnect_Exception:
            print('Unable to connect.  Please check the cable connection')
            status = 1
        except pymono_exceptions.OL750_InvalidPortNumber_Exception:
            status = 31


        return status

    # Attempt to close the connection to the OL750
    def _close_comm(self):

        status = 0

        try:
            self.ol750.CloseComm()
        except:
            status = 1
            raise

        return status

    # Reset the monochrometer and provide feedback based on result received.
    def _reset(self):

        status = 0

        try:
            result = self.ol750.Reset()

            if result == 1:
                raise pymono_exceptions.OL750_NotConnected_Exception

        except pymono_exceptions.OL750_NotConnected_Exception:
            status = 1

        return status

    # Perform grating setup with communication to monochrometer and provide
    # feedback based on result received.
    def _setup_gratings(self):

        status = 0

        try:
            result = self.ol750.SendGratingAndAutoSlitSetupInfo(
                self.grating_lower_wavelength,
                self.grating_upper_wavelength,
                self.grating_grooves,
                self.grating_skew,
                self.grating_entrance,
                self.grating_exit,
                self.entrance_home_offset,
                self.exit_home_offset
            )

            if result == 1:
                raise pymono_exceptions.OL750_NotConnected_Exception
            elif result == 4:
                raise pymono_exceptions.OL750_ArraysAreNull_Exception
            elif result == 5:
                raise pymono_exceptions.OL750_InvalidArrayLengths_Exception
            elif result == 6:
                raise pymono_exceptions.OL750_GratingWavelengthsInvalid_Exception
            elif result == 7:
                raise pymono_exceptions.OL750_GratingEntranceSlitIndicesInvalid_Exception
            elif result == 8:
                raise pymono_exceptions.OL750_GratingExitSlitIndicesInvalid_Exception
            else:
                raise

        except pymono_exceptions.OL750_NotConnected_Exception:
            status = 1
        except pymono_exceptions.OL750_ArraysAreNull_Exception:
            status = 4
        except pymono_exceptions.OL750_InvalidArrayLengths_Exception:
            status = 5
        except pymono_exceptions.OL750_GratingWavelengthsInvalid_Exception:
            status = 6
        except pymono_exceptions.OL750_GratingEntranceSlitIndicesInvalid_Exception:
            status = 7
        except pymono_exceptions.OL750_GratingExitSlitIndicesInvalid_Exception:
            status = 8

        return status

    def _run_sample(self):

        status = 0

        starting_nm = int(self.root.user_options['sample_definition']['starting_wavelength'])
        ending_nm = int(self.root.user_options['sample_definition']['ending_wavelengths'])
        delta_nm = int(self.root.user_options['sample_definition']['change_in_wavelength'])
        delta_t = float(self.root.user_options['sample_definition']['time_between_wavelengths'])

        try:
            for wavelength in range(starting_nm, (ending_nm + delta_nm), delta_nm):
                if self.root.preferences['sample_status'] == "running":
                    print("Setting to " + str(wavelength) + "nm")
                    # result = self.ol750.ManualSetWavelengthPosition(wavelength, 1)
                    time.sleep(delta_t)

            self.root.preferences['sample_status'] = "stopped"
            self.root.frames['sample_frame'].widgets['process_button']['text'] = "Start"
            self.root.frames['sample_frame'].widgets['process_button']['state'] = "enable"
        except:
            pass

        return status