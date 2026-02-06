"""
Runner for the 1-D plume model experiment(s).


Examples
--------
>>> from plume_model import run_sim
>>> from constants import PhysicalConstants, SimulationParameters
>>> results = run_sim(
...     sim_params=SimulationParameters.from_yaml(),
...     const=PhysicalConstants.from_yaml()
... )
>>> print(f"Peak LFR: {results.extract_cube('flash_rate').data.max():.3f} fl s-1 km-2")
Peak LFR: 0.234 fl s-1 km-2
"""

import time

import iris
import paths
from constants import PhysicalConstants, SimulationParameters

from plume_model import run_sim

iris.FUTURE.save_split_attrs = True


def main():
    """Main simulation runner."""
    start_time = time.time()

    # Load the constants and simulation parameters from YAML files
    const = PhysicalConstants.from_yaml()
    sim_params = SimulationParameters.from_yaml()

    run_label = (
        f"{sim_params.plume_base_temp:.0f}__{sim_params.temp_supercool:.0f}__"
        f"{sim_params.water_collision_efficiency:.1f}__{sim_params.ice_collision_efficiency:.1f}"
    ).replace(".", "p")

    print(f"Running simulation: {run_label}")

    # Run the simulation
    result = run_sim(sim_params, const)

    # Save the result to a NetCDF file
    iris.save(result, paths.plume_model_output / f"lightning_sim_{run_label}.nc")

    elapsed_time = time.time() - start_time
    print(f"Calculation time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()
