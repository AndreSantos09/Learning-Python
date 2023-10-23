import curses

def main(stdscr):
    curses.curs_set(0)  # Esconde o cursor
    stdscr.nodelay(1)   # Torna a leitura de teclas não bloqueante
    stdscr.clear()

    menu_options = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
    current_option = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()
        
        for i, option in enumerate(menu_options):
            x = width // 2 - len(option) // 2
            y = height // 2 - len(menu_options) // 2 + i
            if i == current_option:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x, option)
            if i == current_option:
                stdscr.attroff(curses.A_REVERSE)
        
        stdscr.refresh()
        
        key = stdscr.getch()
        if key == curses.KEY_UP:
            current_option = (current_option - 1) % len(menu_options)
        elif key == curses.KEY_DOWN:
            current_option = (current_option + 1) % len(menu_options)
        elif key == ord('\n'):
            stdscr.addstr(height - 1, 0, f"Você selecionou: {menu_options[current_option]}", curses.A_BOLD)
            stdscr.refresh()
            stdscr.getch()
        elif key == ord('q'):
            break

curses.wrapper(main)