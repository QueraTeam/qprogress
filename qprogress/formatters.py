def default_format_func(current_index: int, total_count: int) -> None:
    percent = (current_index / total_count) * 100
    fill_count = int(percent / 2)
    progress_bar = f"{'=' * fill_count}{' ' * (50 - fill_count)}"
    print(f"\rProcessing [{current_index} / {total_count}] [{progress_bar}] {percent:.1f}%", end="")
