from manim import *

class BangunRuangSceneV2(ThreeDScene):
    def construct(self):
        # Set camera angle for a nice 3D view
        self.set_camera_orientation(phi=60 * DEGREES, theta=270 * DEGREES)

        # Define shapes with label names
        shapes = [
            (Cube(side_length=2).set_color(RED), "Kubus"),
            (Sphere().scale(1.5).set_color(BLUE), "Bola"),
            (Cylinder().scale([1, 1, 2]).set_color(RED), "Silinder"),
            (Cone().scale([1, 1, 2]).set_color(ORANGE), "Kerucut"),
            (Tetrahedron().scale(1.5).set_color(PURPLE), "Tetrahedron"),
        ]

        for shape, name in shapes:
            label = Text(name, font_size=40)
            label.scale(1.2)
            label.next_to(shape, DOWN, buff=0.3)
            label.always_face_camera = True

            self.play(Create(shape))
            self.play(Write(label))
            self.wait(2)

            self.play(FadeOut(shape),FadeOut(label))