"""Service mode for MPF w volume controls disabled."""

from mpf.modes.service.code.service import Service

class ServiceNoVol(Service):
    async def _run(self):
        while True:
            # wait for key
            key = await self._get_key()

            if key == "ENTER":
                # start main menu
                await self._start_main_menu()