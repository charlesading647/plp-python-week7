# Week 7 Assignment: Hands-On Lab — Shopping List Manager

## Files

- `list_warmup.py` - Demonstrates list indexing, append, remove, and len.
- `shopping_list.py` - Provides an interactive shopping list manager.
- `list_report.py` - Prints numbered items, counts longer names, and finds the longest item.
- `screenshots/` - Contains screenshots showing each program running.

## Why is it safer to check `in` before calling `.remove()`?

Checking whether an item is in the list before calling `.remove()` prevents a `ValueError` when the item does not exist. This allows the program to display a helpful message instead of crashing. It also makes the program easier for users to understand and use safely.