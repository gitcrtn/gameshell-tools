import dbus


PROPERTIES_INTFACE = 'org.freedesktop.DBus.Properties'

_BUS = None


def get_bus():
    global _BUS
    if not _BUS:
        _BUS = dbus.SystemBus()
    return _BUS


def call_method(obj, iface, name, *args, **kwargs):
    interface = dbus.Interface(obj, iface)
    method = interface.get_dbus_method(name, dbus_interface=None)
    return method(*args, **kwargs)


def get_property(obj, iface, name):
    interface = dbus.Interface(obj, PROPERTIES_INTFACE)
    method = interface.get_dbus_method("Get", dbus_interface=None)
    return method(iface, name)


def get_all_props(obj, iface):
    interface = dbus.Interface(obj, PROPERTIES_INTFACE)
    return dict(interface.GetAll(iface))


# EOF
