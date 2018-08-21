# Import standard python libraries
import os, sys

# Set system path
sys.path.append(os.environ["OPENAG_BRAIN_ROOT"])

# Import run peripheral parent class
from device.peripherals.classes.peripheral_runner import PeripheralRunner

# Import device utilities
from device.utilities.accessors import get_peripheral_config

# Import driver
from device.peripherals.modules.atlas_ph.driver import AtlasPHDriver


class DriverRunner(PeripheralRunner):
    """Runs driver."""

    def __init__(self, *args, **kwargs):
        """Initializes run driver."""
        super().__init__(*args, **kwargs)

        # Initialize parser
        self.parser.add_argument("--info", action="store_true", help="read sensor info")
        self.parser.add_argument(
            "--status", action="store_true", help="read sensor status"
        )
        self.parser.add_argument("--ph", action="store_true", help="read pH")

    def run(self, *args, **kwargs):
        """Runs driver."""
        super().run(*args, **kwargs)

        # Initialize driver optional parameters
        mux = self.communication.get("mux", None)
        if mux != None:
            mux = int(mux, 16)

        # Initialize driver
        self.driver = AtlasPHDriver(
            name=self.args.name,
            bus=self.communication["bus"],
            address=int(self.communication["address"], 16),
            mux=mux,
            channel=self.communication.get("channel", None),
        )

        # Check if reading info
        if self.args.info:
            print("Reading info")
            info = self.driver.read_info()
            print(info)

        # Check if reading status
        elif self.args.status:
            print("Reading status")
            status = self.driver.read_status()
            print(status)

        # Check if reading pH
        elif self.args.ph:
            print("Reading pH")
            ph, error = self.driver.read_potential_hydrogen()
            print("pH: {}".format(ph))


# Run main
if __name__ == "__main__":
    dr = DriverRunner()
    dr.run()
