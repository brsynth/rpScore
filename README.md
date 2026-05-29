# rpScore

Computes a global score for a heterologous pathway. The score is calculated from a learning process based on reaction rules score, flux balance analysis and thermodynamics metrics, and the number of reactions in the pathway.


## Input

Positional argument:
* **infile**: (string) Path to pathway (rpSBML) file
* **outfile**: (string, required if one single input file is passed) path to store the scored pathway

Optional arguments:
* **--no_of_rxns_thres**: (int, default=10) number of reactions above which a pathway is not scored (too long)
* **--data_train_file**: (string) path to the trained data
* **--log**: (string, default=error) Set the log level, choices are 'debug', 'info', 'warning', 'error', 'critical'
* **--version**: Display program's version and exit


## Installation Guide

### Overview

`rpthermo` depends on `rplibs`, which depends on `cobra`, which requires `python-libsbml`.  
On Apple Silicon (`arm64`) macOS, `python-libsbml` is not available as a native Conda package.

Therefore, installation must be done using an **Intel (`osx-64`) Conda environment under Rosetta**.

---

### General case
```bash
conda install -c conda-forge rpthermo
```

---

### Apple Silicon macOS (M1/M2/M3)

#### 1. Install Rosetta 2

```bash
softwareupdate --install-rosetta --agree-to-license
```

#### 2. Install

```bash
CONDA_SUBDIR=osx-64 conda install -c conda-forge rpfba
```

Or with mamba:

```bash
CONDA_SUBDIR=osx-64 mamba install -c conda-forge rpfba
```

#### 3. Persist platform setting

```bash
conda config --env --set subdir osx-64
```

#### 4. Verify installation

```bash
python -c "import rpfba; print('rpfba installed successfully')"
```

#### 5. (Optional) Dev installation

```bash
CONDA_SUBDIR=osx-64 conda env create -f environment.yaml
```

---

### Troubleshooting

#### Solver fails on Apple Silicon

Make sure you are using:

```bash
CONDA_SUBDIR=osx-64
```

#### Wrong architecture environment

Check:

```bash
conda config --show subdir
```

Expected output:

```bash
subdir: osx-64
```


## Run

<!-- ### rpScore process -->
**From Python code**
```python
from rpscore import predict_score
from rplibs import rpPathway

pathway = rpPathway(
    infile='tests/rpscore/data/pathway.xml'
)

global_score = predict_score(pathway)
```
**From CLI**
```sh
python -m rpscore <input_rpsbml> <output_rpsbml>
```

## Tests
Test can be run with the following commands:

### Natively
```bash
cd tests
pytest -v
```

## CI/CD
For further tests and development tools, a CI toolkit is provided in `ci` folder (see [ci/README.md](ci/README.md)).

## Authors

* **Jean-Loup Faulon**
* **Joan Hérisson**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thomas Duigou

<!-- ### How to cite rpScore? -->