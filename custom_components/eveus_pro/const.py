"""Constants for the Eveus Pro integration."""

DOMAIN = "eveus_pro"

# Status mapping
STATUS_MAPPING = {
    0: "Idle",
    1: "Charging",
    2: "Error",
}

SUBSTATUS_MAPPING = {
    0: "No issues",
    1: "Plugged in",
    2: "Disconnected",
    3: "Overload",
}