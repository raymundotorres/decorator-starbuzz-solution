# Starbuzz Coffee — Decorator Reference Implementation

Canonical Decorator example.

## Roles
- Component: `Beverage`
- Concrete Components: `Espresso`, `DarkRoast`, `HouseBlend`, `Decaf`
- Decorator: `CondimentDecorator`
- Concrete Decorators: `Mocha`, `Soy`, `SteamedMilk`, `Whip`

Each decorator remains a `Beverage`, wraps another `Beverage`, delegates, and adds one responsibility.
This allows runtime combinations without one subclass per combination.


## Local setup

macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

Windows PowerShell:
```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## Course conventions

- Python is only the implementation language for the exercise; the design roles are language-agnostic.
- Use an explicit object-oriented design.
- Keep one main class per source file.

