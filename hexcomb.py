def hexcomb(hex_row):
    hex_height = 4  
    def hex_line(row, hex_row):
        if row == 0:
            return ' '.join([' --- '] * hex_row)
        elif row == 1:
            return ' '.join(['/   \\'] * hex_row)
        elif row == 2:
            return ' '.join(['\\   /'] * hex_row)
        elif row == 3:
            return ' '.join([' --- '] * hex_row)

    for line in range(hex_height):
        print(hex_line(line, hex_row))

if __name__ == "__main__":
    hex_row = int(input("Enter the number of hexagons in a row: "))
    hexcomb(hex_row)
