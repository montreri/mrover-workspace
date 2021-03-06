# from ctypes import c_float, c_int32, c_uint32, cast, byref, POINTER
import struct
from enum import Enum


BITMASK = 0xFFFFFFF0


STATUS_1 = 0x02041400
STATUS_2 = 0x02041440
STATUS_3 = 0x02041480
STATUS_4 = 0x020414C0
STATUS_5 = 0x02041500
STATUS_6 = 0x02041540
STATUS_7 = 0x02041580
STATUS_8 = 0x020415C0
STATUS_9 = 0x02041600
STATUS_10 = 0x02041640
STATUS_11 = 0x02041680


CONTROL_1 = 0x02040000
CONTROL_2 = 0x02040040
CONTROL_3 = 0x02040080
CONTROL_5 = 0x02040100
CONTROL_6 = 0x02040140


PARAM_REQUEST = 0x02041800
PARAM_RESPONSE = 0x02041840
PARAM_SET = 0x02041880


class Param(Enum):
    ProfileParamSlot0_P = 1
    ProfileParamSlot0_I = 2
    ProfileParamSlot0_D = 3
    ProfileParamSlot0_F = 4
    ProfileParamSlot0_IZone = 5
    ProfileParamSlot0_CloseLoopRampRate = 6
    ProfileParamSlot1_P = 11
    ProfileParamSlot1_I = 12
    ProfileParamSlot1_D = 13
    ProfileParamSlotI_F = 14
    ProfileParamSlot1_IZone = 15
    ProfileParamSlot1_CloseLoopRampRate = 16
    ProfileParamSoftLimitForThreshold = 21
    ProfileParamSoftLimitRevThreshold = 22
    ProfileParamSoftLimitForEnable = 23
    ProfileParamSoftLimitRevEnable = 24
    OnBoot_BrakeMode = 31
    OnBoot_LimitSwitch_Forward_NormallyClosed = 32
    OnBoot_LimitSwitch_Reverse_NormallyClosed = 33
    OnBoot_LimitSwitch_Forward_Disable = 34
    OnBoot_LimitSwitch_Reverse_Disable = 35
    Fault_OverTemp = 41
    Fault_UnderVoltage = 42
    Fault_ForLim = 43
    Fault_RevLim = 44
    Fault_HardwareFailure = 45
    Fault_ForSoftLim = 46
    Fault_RevSoftLim = 47
    StckyFault_OverTemp = 48
    StckyFault_UnderVoltage = 49
    StckyFault_ForLim = 50
    StckyFault_RevLim = 51
    StckyFault_ForSoftLim = 52
    StckyFault_RevSoftLim = 53
    AppliedThrottle = 61
    CloseLoopErr = 62
    FeedbackDeviceSelect = 63
    RevMotDuringCloseLoopEn = 64
    ModeSelect = 65
    ProfileSlotSelect = 66
    RampThrottle = 67
    RevFeedbackSensor = 68
    LimitSwitchEn = 69
    LimitSwitchClosedFor = 70
    LimitSwitchClosedRev = 71
    SensorPosition = 73
    SensorVelocity = 74
    Current = 75
    BrakeIsEnabled = 76
    EncPosition = 77
    EncVel = 78
    EncIndexRiseEvents = 79
    QuadApin = 80
    QuadBpin = 81
    QuadIdxpin = 82
    AnalogInWithOv = 83
    AnalogInVel = 84
    Temp = 85
    BatteryV = 86
    ResetCount = 87
    ResetFlags = 88
    FirmVers = 89
    SettingsChanged = 90
    QuadFilterEn = 91
    PidIaccum = 93
    Status1FrameRate = 94
    Status2FrameRate = 95
    Status3FrameRate = 96
    Status4FrameRate = 97
    Status6FrameRate = 98
    Status7FrameRate = 99
    ClearPositionOnIdx = 100
    PeakPosOutput = 104
    NominalPosOutput = 105
    PeakNegOutput = 106
    NominalNegOutput = 107
    QuadIdxPolarity = 108
    Status8FrameRate = 109
    AllowPosOverflow = 110
    ProfileParamSlot0_AllowableClosedLoopErr = 111
    NumberPotTurns = 112
    NumberEncoderCPR = 113
    PwdPosition = 114
    AinPosition = 115
    ProfileParamVcompRate = 116
    ProfileParamSlot1_AllowableClosedLoopErr = 117
    Status9FrameRate = 118
    MotionProfileHasUnderrunErr = 119
    Reserved120 = 120
    LegacyControlMode = 121
    MotMag_Accel = 122
    MotMag_VelCruise = 123
    Status10FrameRate = 124
    CurrentLimThreshold = 125
    CustomParam0 = 137
    CustomParam1 = 138
    PersStorageSaving = 139
    ClearPositionOnLimitF = 144
    ClearPositionOnLimitR = 145
    NominalBatteryVoltage = 146
    SampleVelocityPeriod = 147
    SampleVelocityWindow = 148


def fxp_10_22_to_float(raw):
    CONVERSION_CONST = 0.0000002384185791015625
    packed_raw = struct.pack('I', raw)
    val = struct.unpack('f', packed_raw)[0]
    return val * CONVERSION_CONST


def float_to_fxp_10_22(val):
    CONVERSION_CONST = 0x400000
    if val > 1023:
        val = 1023
    elif val < 0:
        val = 0
    packed_val = struct.pack('f', val)
    unsigned_raw = struct.unpack('I', packed_val)[0]
    unsigned_raw = (unsigned_raw * CONVERSION_CONST) % 0xFFFFFFFF
    packed_unsigned_raw = struct.pack('I', unsigned_raw)
    return struct.unpack('i', packed_unsigned_raw)[0]
