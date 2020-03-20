###
#
# Python Translation module for Gooch & Housego OL750-420 SDK
#
# Program Description : This program aims to provide a Python-based
#   programming interface to the Gooch & Housego dll for the OL750-420
#
# For detailed documentation about the functions contained in this file, please
#   refer to the file "2015 750-420 SDK.NET DLL.M000274.RevF.pdf" in the
#   project root directory.
#
# Created By          : Benjamin Kleynhans
# Creation Date       : January 27, 2020
# Authors             : Benjamin Kleynhans
#
# Last Modified By    : Benjamin Kleynhans
# Last Modified Date  : January 29, 2020
# Filename            : ol750_sdk_library_python.py
#
# mapping instructions : https://stackoverflow.com/questions/252417/how-can-i-use-a-dll-file-from-python
# https://stackoverflow.com/questions/49942487/python-for-net-how-to-explicitly-create-instances-of-c-sharp-classes-using-dif
###

# System Imports
import os
import ctypes
import pdb

# DLL Requirements
import clr
import System

class OL750_420_Python_Api():

    # Constructor
    def __init__(self, args):

        self.args = args
        self.args['dll_path'] = os.path.join(args['project_root'], 'lib', 'OL750SDKLibrary.dll')

        # Function definitions
        self.func_defs = {}

        # Create reference to DLL
        dll_ref = System.Reflection.Assembly.LoadFile(self.args['dll_path'])

        # Create reference to object inside DLL
        self.args['class_type'] = dll_ref.GetType('OL750SDKLibrary.OL750SDKLibrary')

        # Create instance of class
        self.ol750Api = System.Activator.CreateInstance(self.args['class_type'])


    def IntegratedSignal(self):
        return self.ol750Api.IntegratedSignal

    def Status(self):
        return self.ol750Api.Status

    def IsConnected(self):
        return self.ol750Api.IsConnected

    def GetErrorMessageFromErrorCode(self, dErrorCode):
        return self.ol750Api.GetErrorMessageFromErrorCode(dErrorCode)

    def CloseComm(self):
        return self.ol750Api.CloseComm()

    def ConfigureNDFilterWheel(self, lfWavelength, spectralTransmittance):
        return self.ol750Api.ConfigureNDFilterWheel(lfWavelength, spectralTransmittance)

    def GetChopperFrequency(self, chopperFrequency):
        return self.ol750Api.GetChopperFrequency(chopperFrequency)

    def GetFilterWheelPosition(self, filterPos, ndFilterWheelPosition):
    	return self.ol750Api.GetFilterWheelPosition(filterPos, ndFilterWheelPosition)

    def GetWavelengthPosition(self, wavelength):
    	return self.ol750Api.GetWavelengthPosition(wavelength)

    def GoToWavelengthAndReturnSignal(self, wavelength, portNumber, gainIndex, lfData, rangeLevelReturned):
    	return self.ol750Api.GoToWavelengthAndReturnSignal(wavelength, portNumber, gainIndex, lfData, rangeLevelReturned)

    def GpibOpen(self, dBoardNum, address):
    	return self.ol750Api.GpibOpen(dBoardNum, address)

    def ManualHomeDetectorSlideDrive(self):
    	return self.ol750Api.ManualHomeDetectorSlideDrive()

    def ManualHomeFilterWheelDrive(self):
    	return self.ol750Api.ManualHomeFilterWheelDrive()

    def ManualHomeWavelengthDrive(self):
    	return self.ol750Api.ManualHomeWavelengthDrive()

    # The ManualSet75MAPositions method is an overloaded method which Python doesn't
    # support, as such the two methods have been renamed accordingly
    #
    # -> ManualSet75MAPositions requiring yaw, pitch and translation    => ManualSet75MAPositionsYPT
    # -> ManualSet75MAPositions requiring degrees                       => ManualSet75MAPositionsD
    #
#->
    def ManualSet75MAPositionsYPT(self, yaw, pitch, translation, yawOffset, pitchOffset, translationOffset):
    	return self.ol750Api.ManualSet75MAPositions(yaw, pitch, translation, yawOffset, pitchOffset, translationOffset)

#->
    def ManualSet75MAPositionsD(self, sampleAngleInDegrees, detectorAngleInDegrees, sampleOffsetInDegrees, detectorOffsetInDegrees):
    	return self.ol750Api.ManualSet75MAPositions(sampleAngleInDegrees, detectorAngleInDegrees, sampleOffsetInDegrees, detectorOffsetInDegrees)

    def ManualSetAutoLightSource(self, position):
    	return self.ol750Api.ManualSetAutoLightSource(position)

    def ManualSetAutoSlitsPositions(self, entrancePosition, exitPosition, entranceOffset, exitOffset):
    	return self.ol750Api.ManualSetAutoSlitsPositions(entrancePosition, exitPosition, entranceOffset, exitOffset)

    def ManualSetChopperFrequency(self, frequencyInHertz):
    	return self.ol750Api.ManualSetChopperFrequency(frequencyInHertz)

    def ManualSetChopperPositionClosed(self):
    	return self.ol750Api.ManualSetChopperPositionClosed()

    def ManualSetChopperPositionOpen(self):
    	return self.ol750Api.ManualSetChopperPositionOpen()

    def ManualSetDetectorSlidePosition(self, detectorPort):
    	return self.ol750Api.ManualSetDetectorSlidePosition(detectorPort)

    def ManualSetFilterWheelPosition(self, filterPosition, ndFilterWheelPosition):
    	return self.ol750Api.ManualSetFilterWheelPosition(filterPosition, ndFilterWheelPosition)

    def ManualSetGratingPosition(self, grating):
    	return self.ol750Api.ManualSetGratingPosition(grating)

    def ManualSetIntegrationTime(self, integrationInSec):
    	return self.ol750Api.ManualSetIntegrationTime(integrationInSec)

    def ManualSetNDFilterWheelPosition(self, filterPosition):
    	return self.ol750Api.ManualSetNDFilterWheelPosition(filterPosition)

    def ManualSetPMTHighVoltage(self, lfVoltage):
    	return self.ol750Api.ManualSetPMTHighVoltage(lfVoltage)

    def ManualSetSignalGain(self, dGainIndex):
    	return self.ol750Api.ManualSetSignalGain(dGainIndex)

    def ManualSetWavelengthPosition(self, wavelength, positionFilterWheel):
    	return self.ol750Api.ManualSetWavelengthPosition(wavelength, positionFilterWheel)

    def PerformDarkCurrent(self, portNumber, data, rangeLevelReturned):
    	return self.ol750Api.PerformDarkCurrent(portNumber, data, rangeLevelReturned)

    def PerformGratingCalibration(self, grating, calibrationFactor):
    	return self.ol750Api.PerformGratingCalibration(grating, calibrationFactor)

    def PerformQuickScan(self, startWaveInNm, endWaveInNm, waveIncInNm, speedInNmPerSec, dGain, scanData, scanDataRange):
    	return self.ol750Api.PerformQuickScan(startWaveInNm, endWaveInNm, waveIncInNm, speedInNmPerSec, dGain, scanData, scanDataRange)

    def Reset(self):
    	return self.ol750Api.Reset()

    def SendAdaptiveSettlingIntegrationTime(self, settlingTime, integrationTime):
    	return self.ol750Api.SendAdaptiveSettlingIntegrationTime(settlingTime, integrationTime)

    def SendDetectorAndGeneralInfo(self, settlingTime, integrationTime, acFrequency, acqMethod, measMode, detector, chopperFrequency, fluxOverload, pmtHighVoltage, detectorPortAndChannel, connectAorA1, connectB, connectA2, connectA3, darkCurrentGain, dsm, gainMultiplier, gainIndex, gainCount, darkCount, darkWavelength, ndFilterThresh):
    	return self.ol750Api.SendDetectorAndGeneralInfo(settlingTime, integrationTime, acFrequency, acqMethod, measMode, detector, chopperFrequency, fluxOverload, pmtHighVoltage, detectorPortAndChannel, connectAorA1, connectB, connectA2, connectA3, darkCurrentGain, dsm, gainMultiplier, gainIndex, gainCount, darkCount, darkWavelength, ndFilterThresh)

    def SendFilterWheelSetupInfo(self, cutOnWavelength):
    	return self.ol750Api.SendFilterWheelSetupInfo(cutOnWavelength)

    def SendGratingAndAutoSlitSetupInfo(self, gratingLowerW, gratingUpperW, gratingGrooves, gratingSkew, gratingEntrance, gratingExit, entranceHomeOffset, exitHomeOffset):
    	return self.ol750Api.SendGratingAndAutoSlitSetupInfo(gratingLowerW, gratingUpperW, gratingGrooves, gratingSkew, gratingEntrance, gratingExit, entranceHomeOffset, exitHomeOffset)

    def SerialOpen(self, dCommPort):
    	return self.ol750Api.SerialOpen(dCommPort)

    def SetDetectorSlide(self, dDetectorSlide):
    	return self.ol750Api.SetDetectorSlide(dDetectorSlide)

    def SetLoggingCB(self, logCB):
    	return self.ol750Api.SetLoggingCB(logCB)

    def SetPostMonoAndFilterDelays(self, moveDelayInSeconds, filterMoveDelayInSeconds):
    	return self.ol750Api.SetPostMonoAndFilterDelays(moveDelayInSeconds, filterMoveDelayInSeconds)

    def StopQuickScan(self):
    	return self.ol750Api.StopQuickScan()

    def statusReturnEventHandlerDelegate(self, sender, e):
    	return self.ol750Api.statusReturnEventHandlerDelevate()
