# Craps (Python)

A text-based version of craps played from the terminal. The player manages a bankroll and places pass or don't pass line bets against a simulated shooter.

## How to Play

Run the game:

```bash
python play_craps.py
```

- You start with a $500 bankroll
- Enter a bet amount (must be positive and within your bankroll)
- Choose your line: **1** for pass line, **2** for don't pass line
- The come out roll resolves immediately on 7, 11, 2, 3, or 12 (12 is a push on the don't pass)
- Any other roll establishes a point, and the shooter keeps rolling — with a brief randomized pause between rolls for suspense — until hitting the point or crapping out with a 7
- Win/loss is added to your bankroll, and you can keep playing until you bust or quit

A "simple game" of craps means pass or don't pass line only — no proposition bets, field bets, or odds yet.

## Requirements

- Python 3.x
- No third-party dependencies (standard library only)
- Tested on Linux and Mac

## Project Structure

| File | Purpose |
|------|---------|
| `play_craps.py` | Main game loop: bankroll, betting, and user interaction |
| `craps.py` | Resolves a single game from the come out roll |
| `keep_rolling.py` | Rolls until the point is made or the shooter craps out |
| `roll_die.py` | Rolls n six-sided dice and returns the total |
| `game_constants.py` | Shared named constants (bet types, outcomes) |
| `get_valid_input.py` | Reusable input validation helper |

## Revision History

This version is a refactor of the initial upload. Changes made:

- **Deduplicated point-roll logic** — the three identical branches for points of 4/10, 5/9, and 6/8 were collapsed into a single `point in (4, 5, 6, 8, 9, 10)` branch
- **Crash-proof input handling** — all user inputs (bet, line selection, keep playing) are validated in loops via a new `get_valid_input()` helper that catches non-numeric entry, rejects out-of-range bets, and handles zero/negative bets
- **Fixed a negative-bet exploit** — bets of zero or less previously slipped through validation
- **Replaced recursion with a loop** — `keep_rolling()` previously called itself recursively for each subsequent roll; it now uses a `while` loop
- **Named constants** — magic numbers for bet types (pass/don't pass) and outcomes (win/lose) are now defined in `game_constants.py` and imported where needed
- **Imports moved to the top of each module** — previously imported inside function bodies
- **Resolved a circular import** — constants originally lived in `craps.py`, which created an import cycle with `keep_rolling.py`; a standalone constants module fixed it
- **Miscellaneous** — fixed variable name and spelling bugs, removed unused imports and dead debug code, extracted input validation into a reusable module for use in other projects

## Known Issues / Future Work

- Game logic and console output are interleaved — separating them would enable large-scale simulations without edits, and fix the text bouncing between "shooter" and "player"
- Betting is currently even money only

## Roadmap

1. Allow the player to take/lay odds behind the line
2. Display the individual dice for each roll
3. Separate game logic from presentation
4. ???

## License

MIT — see [LICENSE](LICENSE) for details.