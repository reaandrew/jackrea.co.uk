from libs import easy_shapes

easy_shapes.setup()


# Jacks work here ...
easy_shapes.draw_circle(101,101,100,"green")

for i in range(1,10):
    easy_shapes.draw_circle(101*i,101,100,"blue")

easy_shapes.finish()  # Keep window open