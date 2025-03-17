from libs import easy_shapes

easy_shapes.setup()

# Draw shapes with smooth edges
easy_shapes.draw_circle(100, 100, 50, "red")
easy_shapes.draw_square(200, 100, 60, "blue")
easy_shapes.draw_triangle(300, 200, 80, "green")
easy_shapes.draw_star(400, 100, 50, "yellow")

# Jacks work here ...
easy_shapes.draw_circle(101,101,100,"green")
easy_shapes.draw_circle(150,150,100,"blue")


easy_shapes.finish()  # Keep window open