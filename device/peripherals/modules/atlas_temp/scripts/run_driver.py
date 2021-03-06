# Import standard python libraries
import os, sys, logging

# Set system path
sys.path.append(os.environ["PROJECT_ROOT"])

# Import typing modules
from typing import Any

# Import device utilities
from device.utilities.accessors import get_peripheral_config

# Import driver modules
from device.peripherals.classes.atlas.scripts.run_driver import (
    DriverRunner as AtlasDriverRunner,
)
from device.peripherals.modules.atlas_temp.driver import AtlasTempDriver


class DriverRunner(AtlasDriverRunner):
    """Runs driver."""

    # Initialize driver class
    Driver = AtlasTempDriver

    # Initialize defaults
    default_device = "edu-v0.3.0"  # TODO: build a config that uses a DO sensor
    default_name = "AtlasTemp-Reservoir"

    def __init__(self, *args: Any, **kwargs: Any):
        """Initializes run driver."""

        # Initialize parent class
        super().__init__(*args, **kwargs)

        # Initialize parser
        self.parser.add_argument("--temp", action="store_true", help="read temperature")

    def run(self, *args: Any, **kwargs: Any):
        """Runs driver."""

        # Run parent class
        super().run(*args, **kwargs)

        # Check if reading pH
        if self.args.temp:
            print("Temp: {} C".format(self.driver.read_temperature()))


# Run main
if __name__ == "__main__":
    dr = DriverRunner()
    dr.run()
