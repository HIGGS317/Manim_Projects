from manim import *

class Test(Scene):
    def construct(self):
        # Step 0: Hello World
        hello = Text("Hello World", font_size=48, color=YELLOW)
        self.play(Write(hello))
        self.wait(1)
        self.play(FadeOut(hello))

        # Step 1: Classical Bit
        bit_box = Square(color=BLUE).shift(LEFT*3)
        bit_text = Text("Bit", font_size=32).next_to(bit_box, UP)
        bit_values = Text("0 or 1", font_size=28).move_to(bit_box.get_center())
        self.play(Create(bit_box), Write(bit_text))
        self.play(Write(bit_values))
        self.wait(1)

        # Step 2: Transition Arrow
        arrow = Arrow(start=bit_box.get_right(), end=RIGHT*0.5, buff=0.5, color=WHITE)
        self.play(GrowArrow(arrow))
        self.wait(0.5)

        # Step 3: Qubit
        qubit_box = Square(color=GREEN).shift(RIGHT*3)
        qubit_text = Text("Qubit", font_size=32).next_to(qubit_box, UP)
        qubit_values = VGroup(
            Text("Superposition", font_size=26, gradient=(BLUE, GREEN)),
            MathTex(r"|0\\rangle + |1\\rangle", font_size=36, color=WHITE)
        ).arrange(DOWN, buff=0.3).move_to(qubit_box.get_center())
        self.play(Create(qubit_box), Write(qubit_text))
        self.play(Write(qubit_values))
        self.wait(2)

        # Step 4: Highlight Information Storage
        info_text = Text(
            "This is how we store\ninformation in quantum computing",
            font_size=28, color=YELLOW
        ).next_to(qubit_box, DOWN*2)
        self.play(Write(info_text))
        self.wait(3)
