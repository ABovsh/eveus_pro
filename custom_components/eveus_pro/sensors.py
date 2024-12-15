"""Sensor platform for the Eveus Pro integration."""

from homeassistant.components.sensor import SensorEntity
from .const import DOMAIN, STATUS_MAPPING, SUBSTATUS_MAPPING

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the Eveus Pro sensors."""
    data = hass.data[DOMAIN][config_entry.entry_id]

    sensors = [
        EveusSensor("Status", "status", data),
        EveusSensor("Substatus", "substatus", data),
        EveusSensor("Current Power", "current_power", data),
        EveusSensor("Total Energy", "total_energy", data),
    ]
    async_add_entities(sensors, update_before_add=True)


class EveusSensor(SensorEntity):
    """Representation of a Eveus Pro sensor."""

    def __init__(self, name, sensor_type, data):
        """Initialize the sensor."""
        self._name = f"eveus_{name.lower().replace(' ', '_')}"
        self._sensor_type = sensor_type
        self._data = data
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        if self._sensor_type == "status":
            return STATUS_MAPPING.get(self._data.get("status", 0))
        elif self._sensor_type == "substatus":
            return SUBSTATUS_MAPPING.get(self._data.get("substatus", 0))
        else:
            return self._data.get(self._sensor_type)

    @property
    def unique_id(self):
        """Return a unique ID for the sensor."""
        return f"{DOMAIN}_{self._sensor_type}"

    @property
    def device_class(self):
        """Return the class of this device."""
        return None