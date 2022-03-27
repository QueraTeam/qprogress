def default_format_func(current_index: int, total_count: int) -> None:
    percent = (current_index / total_count) * 100
    fill_count = int(percent / 2)
    print(f"\rProcessing [{'=' * fill_count}{' ' * (50 - fill_count)}] {percent:.1f}%", end="")
