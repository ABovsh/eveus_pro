"""Config flow for the Eveus Pro integration."""
from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class EveusProConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Eveus Pro."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step where the user provides input."""
        errors = {}

        if user_input is not None:
            # TODO: Validate user input here (e.g., check connectivity)
            return self.async_create_entry(title="Eveus Pro Charger", data=user_input)

        # Form schema
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("charger_ip"): str,
                    vol.Required("username"): str,
                    vol.Required("password"): str,
                }
            ),
            errors=errors,
        )