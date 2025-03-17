from libs import easy_shapes

easy_shapes.setup()

# Head
easy_shapes.draw_square(180, 80, 240, "gray")

# Eyes
easy_shapes.draw_circle(240, 140, 20, "cyan")
easy_shapes.draw_circle(360, 140, 20, "cyan")

# Pupils
easy_shapes.draw_circle(240, 140, 8, "black")
easy_shapes.draw_circle(360, 140, 8, "black")

# Antenna
easy_shapes.draw_triangle(300, 20, 30, "red")
easy_shapes.draw_rectangle(295, 50, 10, 30, "gray")

# Mouth (rectangle speaker-style)
easy_shapes.draw_rectangle(260, 250, 80, 30, "darkgray")

# Star emblem
easy_shapes.draw_star(300, 100, 20, "yellow")

easy_shapes.finish()
