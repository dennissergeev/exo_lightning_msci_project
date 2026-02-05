"""Common paths useful for manipulating datasets and generating figures."""

from pathlib import Path

# Absolute path to the top level of the repository
root = Path(__file__).resolve().parents[2].absolute()

# Absolute path to the `src` folder
src = root / "src"

# Absolute path to the `src/data` folder (contains datasets)
data = src / "data"

# Absolute path to the `src/plume_model_output` folder (contains model output)
plume_model_output = data / "plume_model_output"

# Absolute path to the `src/plume_model` folder (contains model code)
model = src / "plume_model"

# Absolute path to the `src/config` folder (contains YAML config files)
config = model / "config"

# Absolute path to the `src/figures` folder (contains figure output)
figures = src / "figures"
