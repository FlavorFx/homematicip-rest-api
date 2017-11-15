from homematicip.base.constants import MOTION_DETECTOR_INDOOR, \
    KEY_REMOTE_CONTROL_ALARM, PLUGABLE_SWITCH, FULL_FLUSH_SHUTTER, \
    HEATING_THERMOSTAT, SHUTTER_CONTACT, SHUTTER_CONTACT_INVISIBLE, \
    WALL_MOUNTED_THERMOSTAT_PRO, BRAND_WALL_MOUNTED_THERMOSTAT, SMOKE_DETECTOR, \
    FLOOR_TERMINAL_BLOCK_6, PLUGABLE_SWITCH_MEASURING, \
    TEMPERATURE_HUMIDITY_SENSOR_DISPLAY, TEMPERATURE_HUMIDITY_SENSOR, \
    PUSH_BUTTON, ALARM_SIREN_INDOOR, BRAND_SHUTTER, PRECENCE_DETECTOR_INDOOR
from homematicip.device import HeatingThermostat, ShutterContact, \
    WallMountedThermostatPro, SmokeDetector, FloorTerminalBlock6, \
    PlugableSwitchMeasuring, TemperatureHumiditySensorDisplay, PushButton, \
    AlarmSirenIndoor, MotionDetectorIndoor, KeyRemoteControlAlarm, \
    PlugableSwitch, FullFlushShutter, TemperatureHumiditySensorWithoutDisplay, \
    PresenceDetectorIndoor
from homematicip.group import SecurityGroup, SwitchingGroup, \
    ExtendedLinkedSwitchingGroup, LinkedSwitchingGroup, AlarmSwitchingGroup, \
    HeatingHumidyLimiterGroup, HeatingTemperatureLimiterGroup, \
    HeatingChangeoverGroup, InboxGroup, SecurityZoneGroup, HeatingGroup, \
    HeatingCoolingDemandGroup, HeatingExternalClockGroup, \
    HeatingDehumidifierGroup, HeatingCoolingDemandBoilerGroup, \
    HeatingCoolingDemandPumpGroup, SwitchingProfileGroup, \
    OverHeatProtectionRule, SmokeAlarmDetectionRule, LockOutProtectionRule, \
    ShutterWindProtectionRule
from homematicip.securityEvent import SilenceChangedEvent, \
    ActivationChangedEvent, AccessPointConnectedEvent, \
    AccessPointDisconnectedEvent, SensorEvent

TYPE_CLASS_MAP = {
    HEATING_THERMOSTAT: HeatingThermostat,
    SHUTTER_CONTACT: ShutterContact,
    SHUTTER_CONTACT_INVISIBLE : ShutterContact,
    WALL_MOUNTED_THERMOSTAT_PRO: WallMountedThermostatPro,
    BRAND_WALL_MOUNTED_THERMOSTAT: WallMountedThermostatPro,
    SMOKE_DETECTOR: SmokeDetector,
    FLOOR_TERMINAL_BLOCK_6: FloorTerminalBlock6,
    PLUGABLE_SWITCH_MEASURING: PlugableSwitchMeasuring,
    TEMPERATURE_HUMIDITY_SENSOR_DISPLAY: TemperatureHumiditySensorDisplay,
    TEMPERATURE_HUMIDITY_SENSOR: TemperatureHumiditySensorWithoutDisplay,
    PUSH_BUTTON: PushButton,
    ALARM_SIREN_INDOOR: AlarmSirenIndoor,
    MOTION_DETECTOR_INDOOR: MotionDetectorIndoor,
    KEY_REMOTE_CONTROL_ALARM: KeyRemoteControlAlarm,
    PLUGABLE_SWITCH: PlugableSwitch,
    FULL_FLUSH_SHUTTER: FullFlushShutter,
    BRAND_SHUTTER: FullFlushShutter,
    PRECENCE_DETECTOR_INDOOR: PresenceDetectorIndoor
    }

TYPE_GROUP_MAP = {
    "SECURITY": SecurityGroup,
    "SWITCHING": SwitchingGroup,
    "EXTENDED_LINKED_SWITCHING": ExtendedLinkedSwitchingGroup,
    "LINKED_SWITCHING": LinkedSwitchingGroup,
    "ALARM_SWITCHING": AlarmSwitchingGroup,
    "HEATING_HUMIDITY_LIMITER": HeatingHumidyLimiterGroup,
    "HEATING_TEMPERATURE_LIMITER": HeatingTemperatureLimiterGroup,
    "HEATING_CHANGEOVER": HeatingChangeoverGroup,
    "INBOX": InboxGroup,
    "SECURITY_ZONE": SecurityZoneGroup, "HEATING": HeatingGroup,
    "HEATING_COOLING_DEMAND": HeatingCoolingDemandGroup,
    "HEATING_EXTERNAL_CLOCK": HeatingExternalClockGroup,
    "HEATING_DEHUMIDIFIER": HeatingDehumidifierGroup,
    "HEATING_COOLING_DEMAND_BOILER": HeatingCoolingDemandBoilerGroup,
    "HEATING_COOLING_DEMAND_PUMP": HeatingCoolingDemandPumpGroup,
    "SWITCHING_PROFILE": SwitchingProfileGroup,
    "OVER_HEAT_PROTECTION_RULE": OverHeatProtectionRule,
    "SMOKE_ALARM_DETECTION_RULE": SmokeAlarmDetectionRule,
    "LOCK_OUT_PROTECTION_RULE": LockOutProtectionRule,
    "SHUTTER_WIND_PROTECTION_RULE": ShutterWindProtectionRule
    }

TYPE_SECURITY_EVENT_MAP = {
    "SILENCE_CHANGED": SilenceChangedEvent,
    "ACTIVATION_CHANGED": ActivationChangedEvent,
    "ACCESS_POINT_CONNECTED": AccessPointConnectedEvent,
    "ACCESS_POINT_DISCONNECTED": AccessPointDisconnectedEvent,
    "SENSOR_EVENT": SensorEvent
    }
