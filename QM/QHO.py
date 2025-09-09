from math import factorial

import numpy as np
from manim import *
from scipy.special import hermite

# To run this animation, save it as a Python file (e.g., quantum_harmonic_oscillator.py)
# and run the following command in your terminal:
# manim -pql quantum_harmonic_oscillator.py
# This will render both scenes. To render a specific one, use its name, e.g.:
# manim -pql quantum_harmonic_oscillator.py QuantumHarmonicOscillatorStationaryStates


class QuantumHarmonicOscillatorStationaryStates(Scene):
    """
    An animation visualizing the stationary states of a 1D Quantum Harmonic Oscillator.
    It displays the potential energy well, the quantized energy levels, and the
    probability density functions for the first few energy states (n=0 to n=3).
    """

    def construct(self):
        # 1. Setup the Scene and Axes
        self.camera.background_color = "#f9f9f9"  # A light background
        title = Title(
            "Quantum Harmonic Oscillator: Stationary States",
            color=BLACK,
            include_underline=False,
        ).to_edge(UP)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 5, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLACK, "include_tip": False},
        ).add_coordinates()

        # Add labels to the axes
        x_label = axes.get_x_axis_label("x", edge=DOWN, direction=DOWN).set_color(BLACK)
        y_label = axes.get_y_axis_label("E", edge=LEFT, direction=LEFT).set_color(BLACK)

        # 2. Define the Potential and Energy Levels
        # We use simplified units where m = omega = h_bar = 1
        k = 1.0  # Spring constant

        def potential_func(x):
            """The potential energy V(x) = 1/2 * k * x^2."""
            return 0.5 * k * x**2

        potential_graph = axes.plot(potential_func, color=BLUE, x_range=[-3.5, 3.5])
        potential_label = axes.get_graph_label(
            potential_graph, label="V(x) = \\frac{1}{2}kx^2", x_val=-3
        ).set_color(BLUE)

        # Group axes and potential for initial animation
        setup_group = VGroup(axes, x_label, y_label, potential_graph, potential_label)

        self.play(Write(title))
        self.play(Create(setup_group), run_time=2)
        self.wait(1)

        # 3. Define and Plot Wavefunctions (Probability Densities)

        # n-th energy level: E_n = (n + 1/2)
        def energy_level(n):
            return n + 0.5

        # n-th probability density: |psi_n(x)|^2
        # Proportional to (H_n(x))^2 * exp(-x^2)
        def prob_density_func(n):
            # Hermite polynomial of degree n
            H_n = hermite(n)

            def func(x):
                # We add the energy level to shift the plot vertically
                # and scale it for better visualization.
                psi_squared = (H_n(x) ** 2) * np.exp(-(x**2))
                # Normalization constant for psi_n
                norm_factor = np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))
                return 0.5 * psi_squared / norm_factor + energy_level(n)

            return func

        # 4. Animate the states sequentially
        max_n = 3
        for n in range(max_n + 1):
            # Energy level line
            E_n = energy_level(n)
            energy_line = DashedLine(
                start=axes.c2p(-5, E_n),
                end=axes.c2p(5, E_n),
                color=ORANGE,
                stroke_width=3,
            )

            # Probability density plot
            prob_density_graph = axes.plot(
                prob_density_func(n), x_range=[-4, 4], color=GREEN_C
            )

            # Labels for the state
            n_label_text = f"n = {n}"

            n_label = MathTex(n_label_text, color=BLACK).next_to(
                axes.c2p(4, E_n), RIGHT
            )

            # Group for this state
            state_group = VGroup(energy_line, prob_density_graph, n_label)

            # Animate the appearance of the state
            self.play(
                FadeIn(energy_line),
                Create(prob_density_graph),
                Write(n_label),
                run_time=2,
            )
            self.wait(1)

        self.wait(3)


class QuantumHarmonicOscillatorTimeEvolution(Scene):
    """
    An animation visualizing the time evolution of a superposition of states
    in a 1D Quantum Harmonic Oscillator. It shows the probability density
    of a wave packet oscillating within the potential well.
    """

    def construct(self):
        # 1. Setup the Scene and Axes
        self.camera.background_color = "#f9f9f9"
        title = Title(
            "Quantum Harmonic Oscillator: Time Evolution",
            color=BLACK,
            include_underline=False,
        ).to_edge(UP)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[0, 4, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLACK, "include_tip": False},
        ).add_coordinates()

        x_label = axes.get_x_axis_label("x", edge=DOWN, direction=DOWN).set_color(BLACK)
        y_label = axes.get_y_axis_label(
            "|\\Psi(x,t)|^2", edge=LEFT, direction=LEFT
        ).set_color(BLACK)

        # 2. Draw the potential well
        k = 1.0
        potential_graph = axes.plot(
            lambda x: 0.5 * k * x**2, color=BLUE, x_range=[-3.5, 3.5]
        )
        potential_label = axes.get_graph_label(
            potential_graph, label="V(x)", x_val=-3, direction=UP
        ).set_color(BLUE)

        setup_group = VGroup(axes, x_label, y_label, potential_graph, potential_label)
        self.play(Write(title))
        self.play(Create(setup_group), run_time=2)
        self.wait(1)

        # 3. Define the superposition state and its time evolution
        time = ValueTracker(0)

        # Time-independent eigenfunctions psi_n(x)
        def get_psi(n):
            norm_factor = 1.0 / (np.sqrt(2**n * factorial(n)) * np.pi**0.25)
            H_n = hermite(n)

            def psi_n_x(x):
                return norm_factor * H_n(x) * np.exp(-(x**2) / 2.0)

            return psi_n_x

        psi_0 = get_psi(0)
        psi_1 = get_psi(1)
        E_0 = 0.5
        E_1 = 1.5

        # Time-dependent wavefunction Psi(x, t) as a superposition of n=0 and n=1
        def psi_t(x, t):
            c0 = 1 / np.sqrt(2)
            c1 = 1 / np.sqrt(2)
            term0 = c0 * psi_0(x) * np.exp(-1j * E_0 * t)
            term1 = c1 * psi_1(x) * np.exp(-1j * E_1 * t)
            return term0 + term1

        # The probability density |Psi(x, t)|^2
        def prob_density_t(t_val):
            def func(x):
                val = psi_t(x, t_val)
                prob = np.abs(val) ** 2
                # Scale for visualization
                return prob * 3.5

            return func

        # Create the dynamic graph
        prob_density_graph = always_redraw(
            lambda: axes.plot(
                prob_density_t(time.get_value()),
                x_range=[-4, 4],
                color=PURPLE_B,
            ).set_fill(PURPLE_B, opacity=0.5)
        )

        # Create a time label
        time_label = always_redraw(
            lambda: MathTex(f"t = {time.get_value():.2f}", color=BLACK).to_corner(UR)
        )

        # Add explanatory text
        explanation = Tex(
            "A superposition, e.g., $\\Psi(x,0) = \\frac{1}{\\sqrt{2}}(\\psi_0 + \\psi_1)$, is not stationary.",
            color=BLACK,
        ).to_corner(DL)

        self.play(Write(explanation))
        self.wait(2)

        # 4. Animate the time evolution
        self.play(Create(prob_density_graph), Write(time_label))
        self.wait(1)

        explanation.generate_target()
        explanation.target.become(
            Tex(
                "The probability density now oscillates in time.", color=BLACK
            ).to_corner(DL)
        )
        self.play(MoveToTarget(explanation))

        # The oscillation period T is 2*pi / (E1 - E0) = 2*pi / 1 = 2*pi
        self.play(time.animate.set_value(2 * PI), run_time=10, rate_func=linear)
        self.wait(0.5)
        self.play(time.animate.set_value(4 * PI), run_time=10, rate_func=linear)

        self.wait(3)
