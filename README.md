# Python For Data Science

This repository contains a set of Python exercises and small scripts organized by module/folder. It is structured as incremental learning blocks, moving from setup and fundamentals to arrays, tabular data, OOP, and decorators/functional patterns.

## Repository structure

- `Python_00_Starting/` – initial setup and first Python steps.
- `Python_01_Array/` – array/image exercises (loading images, basic manipulation, zoom/rotate, etc.).
- `Python_02_DataTable/` – working with tabular data (data tables / dataframes).
- `Python_03_OOP/` – object-oriented programming exercises (inheritance, abstract base classes, dunder methods, simple calculators).
- `Python_04_Dod/` – decorators & higher-order functions (statistics helpers, closures, call limiting).

## What has been done (as of 2026-03-10)

Recent work includes completing modules **Python 3** and **Python 4** and adding documentation.

- **2026-03-10**: `added documentation`
- **2026-03-10**: `finished Python3`
- **2026-03-10**: `finished Python4`

(See the commit history in GitHub for the full list of changes.)

## Highlights by module

### Python_01_Array

Examples include:
- BMI helpers (`ex00/give_bmi.py`)
- Image loading utilities and test scripts
- Zooming into images and saving output (`ex03/zoom.py`)
- Rotating images via a manual transpose (`ex04/rotate.py`)

### Python_03_OOP

Examples include:
- Abstract base classes and inheritance (`Character`, `Stark`, `Baratheon`, `Lannister`)
- Basic vector operations in a `calculator` class (`ex04/ft_calculator.py`)

### Python_04_Dod

Examples include:
- Basic statistics utilities (`ex00/statistics.py`: `ft_statistics`, mean/median/quartile/std/var)
- Closures / higher-order functions (`ex01/in_out.py`: `outer`, `inner`, `square`, `pow`)
- Decorator usage with call limiting (see `ex02/tester.py`)

## How to run

Most exercises are standalone scripts. From the repository root:

```bash
python3 path/to/script.py
```

Example:

```bash
python3 Python_01_Array/ex03/zoom.py
```

## Requirements

- Python 3.10+ (for `int | float` union type syntax)
- Additional packages may be required depending on the exercise (e.g. `numpy`, `matplotlib`, `pandas`).

## Notes

This is a learning repository. File names and exercise folders follow the module structure.
