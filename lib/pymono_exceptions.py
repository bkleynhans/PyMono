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
# Filename            : pymono_exceptions.py
#
###

class Error(Exception):
    pass


class OL750_NotConnected_Exception(Error):
    """Raised when there is no connection to the monochrometer"""
    pass


class OL750_ArraysAreNull_Exception(Error):
    """Raised when an input array has a NULL value"""
    pass


class OL750_InvalidArrayLengths_Exception(Error):
    """Raised when an input array doesn't have the required 3 elements"""
    pass


class OL750_GratingWavelengthsInvalid_Exception(Error):
    """Raised when one of the grating wavelengths has an invalid value"""
    pass


class OL750_GratingEntranceSlitIndicesInvalid_Exception(Error):
    """Raised when one of the grating entrance slit indices are invalid"""
    pass


class OL750_GratingExitSlitIndicesInvalid_Exception(Error):
    """Raised when one of the grating exit slit indices are invlid"""
    pass


class OL750_FailedToConnect_Exception(Error):
    """Raised when we are unable to connecto to the monochrometer using the supplied port"""
    pass


class OL750_InvalidPortNumber_Exception(Error):
    """Raised when the supplied port has nothing connected to it"""
    pass


class OL750_InvalidWavelengthPosition_Exception(Error):
    """Raised when the specified wavelength position is invalid"""
    pass