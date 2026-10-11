# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-10-11

### Added
- `game_constants.py` module holding shared named constants (`PASS_LINE`, `DONT_PASS`, `SHOOTER_WINS`, `SHOOTER_LOSES`)
- `get_valid_input.py` module providing reusable, crash-proof input validation for use across projects
- Centralized input validation loop for bet, line selection, and keep-playing prompts
- Cross-platform screen clearing (Windows/Linux/Mac)

### Changed
- Collapsed three duplicated point-roll branches (4/10, 5/9, 6/8) into a single `point in (4, 5, 6, 8, 9, 10)` branch in `craps.py`
- Replaced recursive dice rolling in `keep_rolling()` with a `while` loop
- Moved module imports from inside function bodies to the top of each module
- Replaced magic numbers for bet types and outcomes with named constants imported from `game_constants.py`
- Renamed and expanded README with gameplay instructions, requirements, and project structure

### Fixed
- Negative and zero bets bypassing validation, allowing players to gain money on losses
- Non-numeric user input crashing the game with an unhandled `ValueError`
- Invalid line selections (values other than 1 or 2) causing an infinite loop or proceeding with garbage values
- Circular import between `craps.py` and `keep_rolling.py` (constants now live in a standalone module)
- Misspelled variable name (`winngins`) causing a `NameError` on point-cycle losses
- Sequential bet validation loops that allowed out-of-bankroll bets after re-entry

### Removed
- Unused imports and dead debug print statements
- Redundant validation checks superseded by `get_valid_input()`

## [1.0.0] - 2020-09-09

### Added
- Initial release:  text based craps with pass/don't pass line betting