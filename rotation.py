from manim import *

"""
Positions:
    Abosulte Positions:
        -Sides: .to_edge() -- UP, DOWN, LEFT, RIGHT
        -Corners: .to_corner() -- UR, UL, DR, DL
    Relative Positions:
        - .move_to()
            - Locate object and move it
"""
class Positions(Scene):
    def construct(self):
        #Add dots for edge
        object1 = Dot().set_color(RED)
        object2 = Dot().set_color(RED)
        object3 = Dot().set_color(RED)
        object4 = Dot().set_color(RED)

        #Add dots for corners
        object5 = Dot().set_color(BLUE)
        object6 = Dot().set_color(BLUE)
        object7 = Dot().set_color(BLUE)
        object8 = Dot().set_color(BLUE)

        #Add objects for relative positions
        square1 = Square().set_color(GREEN).set_fill(GREEN, opacity=1.0).scale(.08)
        square2 = Square().set_color(GREEN).set_fill(RED, opacity=1.0).scale(.08)
        square3 = Square().set_color(GREEN).set_fill(PURPLE, opacity=1.0).scale(.08)
        square4 = Square().set_color(GREEN).set_fill(YELLOW, opacity=1.0).scale(.08)
        square5 = Square().set_color(GREEN).set_fill(BLUE, opacity=1.0).scale(.08)
        vector = Vector([2,2,0])
        text = Text("Text").set_color(GREEN)


        # Abosulte Positions
        object1.to_edge(UP)
        object2.to_edge(DOWN)
        object3.to_edge(LEFT)
        object4.to_edge(RIGHT)

        object5.to_corner(UL)
        object6.to_corner(UR)
        object7.to_corner(DL)
        object8.to_corner(DR)

        #Add Grid
        numberplane = NumberPlane()

        #Relative Positions
        square1.move_to(2*UP + RIGHT)

        square2.move_to(vector)

        text.move_to([-3, 2, 0])
        square3.move_to(text)
        square4.move_to(text.get_center() + 5*RIGHT)

        square5.next_to(text, RIGHT)

        # square1.shift(DOWN)
        # self.wait()
        # square1.shift(LEFT)
        # self.wait()
        # square1.shift(UP)
        # self.wait()


        self.add(object1, object2, object3, object4, object3, object4, object5, object6, object7, object8, numberplane, square1, square2, vector, square3, square4, square5, text)
        self.play(square1.animate.shift(UP), run_time = 1)
        self.wait()
