# my_code_projects

Collection of small Python console apps for practice (games, utilities, and a PDF organizer). Sibling project [`15_atm`](../15_atm) composes several of these ideas into one menu-driven ATM demo.

## Requirements

Python 3. Optional extras used by some projects:

```bash
pip install termcolor qrcode pillow pymupdf
```

| Package     | Used by                                      |
|-------------|----------------------------------------------|
| `termcolor` | quiz, tic-tac-toe, cows & bulls, etc.        |
| `qrcode`    | `3_qr_code_generator`                        |
| `pymupdf`   | `email_organizer` (import as `fitz`)         |

## Projects

| Folder | Entry point(s) | Notes |
|--------|----------------|--------|
| `1_dice_game` | `dice_game.py`, `cards.py` | Dice / cards helpers |
| `2_number_guessing_game` | `numbers_game.py` | Number guessing |
| `3_qr_code_generator` | `qr_code.py`, `qr_code_genv1.py` | Needs `qrcode` |
| `4_currency_converter` | scripts in folder | Hardcoded rates, no API |
| `5_rock,paper,scissors` | `rock_paper_scissors.py` | Classic RPS |
| `6_quiz_game` | `quiz_game.py` … `quiz_game_v3.py` | Needs `termcolor` |
| `7_tic_tac_toe` | `TicTacToe.py`, `TicTacToe_v2.py` | Needs `termcolor` |
| `8_todo_list` | `todo_list.py` | Simple todo CLI |
| `9_pig_dice_game` | `pig_dice_game.py`, `pig_dice_game_v2.py` | Pig dice |
| `10_cows_and_bulls` | `cows_and_bulls.py`, `cows_and_bulls_v2.py` | Needs `termcolor` |
| `11_password_strength_checker` | `password_strength_checker.py`, `_v2.py` | Password scoring |
| `12_password_generator` | `password_generator.py` … `_v3.py` | Password generation |
| `13_word_guessing_game` | `word_guessing.py` | Word guess |
| `14_slot_machine` | `slot.py` | Slot machine |
| `email_organizer` | `email_organizer.py`, `fuzzy_matching.py` | PDF tooling via PyMuPDF |

Some folders include problem-statement `.mp4` videos.

## How to run

```bash
cd 2_number_guessing_game
python numbers_game.py
```

Prefer the highest versioned script in a folder when multiple exist (for example `*_v3.py`).
