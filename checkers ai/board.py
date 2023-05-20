import tkinter as tk


class Board(tk.Tk):

    def __init__(self, init_board, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Chinese Checkers")
       
        self.resizable(False, False)
        
        self.configure(bg="#fff")

      
        self.pieces = {}
        self.board = init_board
        self.r_size = len(init_board)
        self.c_size = len(init_board[0])

        
        self.canvas = tk.Canvas(self, width=550, height=550, bg="#fff",
                                highlightthickness=0)
        self.canvas.grid(row=1, column=1,
                         columnspan=self.c_size, rowspan=self.r_size)

        
        self.status = tk.Label(self, anchor="c", font=(None, 16),
                               bg="#212121", fg="#fff", text="Green player's turn")
        self.status.grid(row=self.r_size + 3, column=0,
                         columnspan=self.c_size + 3, sticky="ewns")

        
        self.canvas.bind("<Configure>", self.draw_pieces)

        
        self.columnconfigure(0, minsize=48)
        self.rowconfigure(0, minsize=48)
        self.columnconfigure(self.c_size + 2, minsize=48)
        self.rowconfigure(self.r_size + 2, minsize=48)
        self.rowconfigure(self.r_size + 3, minsize=48)

  
    def add_click_handler(self, func):
        self.click_handler = func

    def set_status(self, text):
        self.status.configure(text=text)

    def set_status_color(self, color):
        self.status.configure(bg=color)

    def draw_pieces(self, event=None, board=None):

        if board is not None:
            self.board = board

        self.canvas.delete("tile")
 
        cell_width = int(self.canvas.winfo_width() / self.c_size)
        cell_height = int(self.canvas.winfo_height() / self.r_size)
        border_size = 5

       
        for col in range(self.c_size):
            for row in range(self.r_size):
                board_tile = self.board[row][col]
                tile_color, outline_color = board_tile.get_tile_colors()

                x1 = col * cell_width + border_size / 2
                y1 = row * cell_height + border_size / 2
                x2 = (col + 1) * cell_width - border_size / 2
                y2 = (row + 1) * cell_height - border_size / 2

                
                tile = self.canvas.create_oval(x1, y1, x2, y2,
                                               tags="tile", width=border_size, fill=tile_color,
                                               outline=outline_color)
                self.pieces[row, col] = tile

                self.canvas.tag_bind(tile, "<1>", lambda event, row=row,
                                                         col=col: self.click_handler(row, col))

        self.update()
