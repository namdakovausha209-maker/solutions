def month_calendar(start_weekday, days):
    result_lines = []
    current_day = 1
    while current_day <= days:
        line = []
        if not result_lines:
            for _ in range(start_weekday):
                line.append("  ")
        while len(line) < 7 and current_day <= days:
            line.append(f"{current_day:2}")
            current_day += 1
        result_lines.append(" ".join(line))
    return "\n".join(result_lines)
