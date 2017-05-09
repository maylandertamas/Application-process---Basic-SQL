def print_table(table, title_list):
    border_horizontal = '_'
    border_vertical = '|'
    border_cross = '+'
    columns = [list(x) for x in zip(*table, title_list)]
    lengths = [max(map(len, map(str, col))) for col in columns]
    separate_rows = border_vertical + border_vertical.join(' {:^%d} ' % l for l in lengths) + border_vertical
    separate_crosses = border_cross + border_cross.join(border_horizontal * (l+2) for l in lengths) + border_cross

    print(separate_crosses)
    print(separate_rows.format(*title_list))
    print(separate_crosses)
    for row in table:
        print(separate_rows.format(*row))
        print(separate_crosses)
