from ..dbus_proxy import (
    get_bus,
    get_all_props,
    get_property,
    call_method,
)


UPOWER_INTFACE = 'org.freedesktop.UPower'
UPOWER_DEVICE_INTFACE = 'org.freedesktop.UPower.Device'
UPOWER_BATTERY_OBJPATH = '/org/freedesktop/UPower/devices/battery_axp20x_battery'
UPOWER_USB_OBJPATH = '/org/freedesktop/UPower/devices/line_power_axp20x_usb'

_BATTERY_OBJ = None


def _get_battery_obj():
    global _BATTERY_OBJ
    if not _BATTERY_OBJ:
        bus = get_bus()
        _BATTERY_OBJ = bus.get_object(UPOWER_INTFACE, UPOWER_BATTERY_OBJPATH)
    return _BATTERY_OBJ


def get_battery_props():
    battery = _get_battery_obj()
    return get_all_props(battery, UPOWER_DEVICE_INTFACE)


def get_battery_percent():
    battery = _get_battery_obj()
    return int(get_property(battery, UPOWER_DEVICE_INTFACE, 'Percentage'))


# EOF
