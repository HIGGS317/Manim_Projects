from manim import *
import numpy as np

# To render:
# manim -pqh quantum_tunneling.py QuantumTunnelingWithClassical

class QuantumTunnelingWithClassical(Scene):
    def construct(self):
        # --- Physics Parameters ---
        barrier_height = 3
        barrier_width = 2
        barrier_left = -1
        barrier_right = barrier_left + barrier_width
        x_min, x_max = -5, 5
        E = 1
        m = 1
        hbar = 1

        # === 1. CLASSICAL ANIMATION (IMPROVED) ===
        ground_y = -1.45
        ground = Line(LEFT*5, RIGHT*5).shift(UP*ground_y)
        barrier = Rectangle(
            width=barrier_width,
            height=barrier_height,
            color=RED_B,
            fill_color=RED_B,
            fill_opacity=0.7
        ).move_to(RIGHT*(barrier_left+barrier_width/2) + UP*ground_y + UP*barrier_height/2)
        # Ball: higher for visibility
        ball_y = ground_y + 1.4
        ball = Dot(LEFT*3.8 + UP*ball_y, color=BLUE_B, radius=0.25)
        # Energy level: higher above ground, and labeled
        e_level_y = ball_y + 0.32
        e_level = DashedLine(
            start=LEFT*5 + UP*e_level_y,
            end=RIGHT*5 + UP*e_level_y,
            color=BLUE_B,
            stroke_width=4,
            dash_length=0.17
        )
        e_label = Text("Energy (E)", font_size=28, color=BLUE_B).next_to(e_level, UP, buff=0.14).to_edge(LEFT, buff=1.3)
        classical_caption = VGroup(
            Text("Classical Case:", font_size=33).to_edge(UP),
            Text("If E < V0, particle cannot cross the barrier!", font_size=30).next_to(ORIGIN, DOWN).shift(UP*2.7)
        )
        self.add(ground, barrier)
        self.play(FadeIn(classical_caption), FadeIn(ball), FadeIn(e_level), FadeIn(e_label))
        self.wait(0.7)
        # Ball only goes up to barrier and bounces back
        self.play(ball.animate.move_to(RIGHT*(barrier_left-0.22) + UP*ball_y), run_time=1.0)
        self.wait(0.25)
        self.play(ball.animate.move_to(LEFT*4.1 + UP*ball_y), run_time=0.7)
        self.wait(0.5)
        self.play(FadeOut(classical_caption), FadeOut(ball), FadeOut(ground), FadeOut(e_level), FadeOut(e_label), FadeOut(barrier))
        self.wait(0.4)

        # === 2. QUANTUM TUNNELING STEPWISE ===
        axes = Axes(
            x_range=[x_min, x_max, 1],
            y_range=[0, barrier_height + 1, 1],
            x_length=10,
            y_length=3,
            axis_config={"include_tip": False},
        ).to_edge(DOWN, buff=0.9)
        barrier_quantum = Rectangle(
            width=barrier_width,
            height=barrier_height,
            color=RED_B,
            fill_color=RED_B,
            fill_opacity=0.55
        ).move_to(
            axes.c2p(barrier_left + barrier_width / 2, barrier_height / 2)
        ).align_to(axes.c2p(barrier_left, 0), DOWN)
        barrier_label = MathTex("V_0", font_size=36, color=RED_B)\
            .next_to(barrier_quantum, UP, buff=0.1)
        regI = Text("Region I", font_size=26).next_to(axes.c2p(-3.9, 0), DOWN, buff=0.14)
        regII = Text("Region II", font_size=26).next_to(axes.c2p(0, 0), DOWN, buff=0.14)
        regIII = Text("Region III", font_size=26).next_to(axes.c2p(3.9, 0), DOWN, buff=0.14)
        self.play(Create(axes), FadeIn(barrier_quantum), FadeIn(barrier_label))
        self.play(FadeIn(regI), FadeIn(regII), FadeIn(regIII))

        k = np.sqrt(2 * m * E) / hbar
        kappa = np.sqrt(2 * m * (barrier_height - E)) / hbar

        # --- 1. REGION I ---
        capI = Text(
            "Region I: Free particle — oscillating wave",
            font_size=32
        ).to_edge(UP).shift(DOWN*0.18)
        psiI_eq = MathTex(
            r"\psi_I(x) = Ae^{ikx} + Be^{-ikx}",
            font_size=37
        ).set_color(YELLOW_B).next_to(capI, DOWN, buff=0.2)
        self.play(FadeIn(capI), FadeIn(psiI_eq))
        self.wait(0.6)
        psi_I = lambda x: np.cos(k * x)
        psiI_graph = axes.plot(
            lambda x: 1.2 + 0.7 * psi_I(x),
            x_range=[x_min, barrier_left],
            color=YELLOW_B, stroke_width=5
        )
        self.play(Create(psiI_graph))
        self.wait(1.0)
        self.play(FadeOut(capI), FadeOut(psiI_eq))
        self.wait(0.22)

        # --- 2. REGION II ---
        capII = Text(
            "Region II: Inside barrier — exponential decay",
            font_size=32
        ).to_edge(UP).shift(DOWN*0.18)
        psiII_eq = MathTex(
            r"\psi_{II}(x) = Ce^{-\kappa x}",
            font_size=37
        ).set_color(GREEN_B).next_to(capII, DOWN, buff=0.2)
        self.play(FadeIn(capII), FadeIn(psiII_eq))
        self.wait(0.6)
        psi_II = lambda x: np.exp(-kappa * (x - barrier_left))
        psiII_graph = axes.plot(
            lambda x: 1.2 + 0.7 * psi_II(x),
            x_range=[barrier_left, barrier_right],
            color=GREEN_B, stroke_width=5
        )
        self.play(FadeOut(psiI_graph))
        self.play(Create(psiII_graph))
        self.wait(1.0)
        self.play(FadeOut(capII), FadeOut(psiII_eq))
        self.wait(0.22)

        # --- 3. REGION III ---
        capIII = Text(
            "Region III: Emerges again — low amplitude",
            font_size=32
        ).to_edge(UP).shift(DOWN*0.18)
        psiIII_eq = MathTex(
            r"\psi_{III}(x) = Fe^{ikx}",
            font_size=37
        ).set_color(BLUE_B).next_to(capIII, DOWN, buff=0.2)
        self.play(FadeIn(capIII), FadeIn(psiIII_eq))
        self.wait(0.6)
        psi_III = lambda x: 0.25 * np.cos(k * (x - barrier_right))
        psiIII_graph = axes.plot(
            lambda x: 1.2 + 0.7 * psi_III(x),
            x_range=[barrier_right, x_max],
            color=BLUE_B, stroke_width=5
        )
        self.play(FadeOut(psiII_graph))
        self.play(Create(psiIII_graph))
        self.wait(1.0)
        self.play(FadeOut(capIII), FadeOut(psiIII_eq))
        self.wait(0.22)

        # --- 4. Combine All Regions: Full wavefunction ---
        psiI_graph_full = axes.plot(
            lambda x: 1.2 + 0.7 * psi_I(x),
            x_range=[x_min, barrier_left],
            color=YELLOW_B, stroke_width=4
        )
        psiII_graph_full = axes.plot(
            lambda x: 1.2 + 0.7 * psi_II(x),
            x_range=[barrier_left, barrier_right],
            color=GREEN_B, stroke_width=4
        )
        psiIII_graph_full = axes.plot(
            lambda x: 1.2 + 0.7 * psi_III(x),
            x_range=[barrier_right, x_max],
            color=BLUE_B, stroke_width=4
        )
        all_waves = VGroup(psiI_graph_full, psiII_graph_full, psiIII_graph_full)
        combined_label = Text(
            "Quantum Wavefunction: All regions",
            font_size=33
        ).to_edge(UP)
        self.play(FadeOut(psiIII_graph))
        self.play(FadeIn(all_waves), FadeIn(combined_label))
        self.wait(1.1)

        # --- 5. Transmission probability: formula and explanation ---
        self.play(FadeOut(combined_label))
        trans_eq = MathTex(
            r"T \sim e^{-2\kappa a}",
            font_size=44
        ).to_edge(UP).shift(DOWN*0.1)
        kappa_eq = MathTex(
            r"\kappa = \sqrt{\frac{2m(V_0 - E)}{\hbar^2}}",
            font_size=36
        ).next_to(trans_eq, DOWN, buff=0.35)
        self.play(FadeIn(trans_eq))
        self.wait(0.6)
        self.play(FadeIn(kappa_eq))
        self.wait(0.8)

        t_caption = Text(
            "T is the transmission probability.", font_size=32
        ).next_to(kappa_eq, DOWN, buff=0.6)
        self.play(FadeIn(t_caption))
        self.wait(1.8)
        self.play(FadeOut(trans_eq), FadeOut(kappa_eq), FadeOut(t_caption))

        # --- Caption: Wider/taller barrier, T decreases ---
        wider_caption = Text(
            "As the potential barrier becomes wider or taller,\nthe transmission probability decreases.",
            font_size=29
        ).to_edge(UP)
        self.play(FadeIn(wider_caption))
        self.wait(2)
        self.play(FadeOut(wider_caption), FadeOut(regI), FadeOut(regII), FadeOut(regIII), FadeOut(barrier_quantum), FadeOut(barrier_label), FadeOut(all_waves))

        # --- Final summary ---
        summary = Text(
            "Quantum particles can tunnel through Forbidden zones!",
            font_size=31
        ).to_edge(UP)
        self.play(FadeIn(summary))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])
