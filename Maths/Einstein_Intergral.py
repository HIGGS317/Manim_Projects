from manim import *
import numpy as np

config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class BoseEinsteinIntegral(Scene):
    def construct(self):
        # Title
        title = MathTex(r"\text{Solving the Bose-Einstein Integral}").scale(1).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Step 1: Show the Bose-Einstein distribution
        eq1 = MathTex(
            r"n(E) = \frac{g(E)}{e^{(E-\mu)/k_BT} - 1}"
        ).shift(UP * 1.5)
        
        label1 = Text("Bose-Einstein distribution", font_size=20).next_to(eq1, DOWN, buff=0.3)
        self.play(Write(eq1))
        self.play(Write(label1))
        self.wait(2)

        # Step 2: Show the integral for total number density
        eq2 = MathTex(
            r"N = \int_0^{\infty} n(E) \, dE = \int_0^{\infty} \frac{g(E)}{e^{(E-\mu)/k_BT} - 1} \, dE"
        ).scale(0.8).next_to(label1, DOWN, buff=0.4)
        
        self.play(Write(eq2))
        self.wait(2)

        # Step 3: Substitute density of states for 3D case
        eq3 = MathTex(
            r"g(E) = \frac{V}{2\pi^2} \left(\frac{2m}{h^2}\right)^{3/2} E^{1/2}"
        ).next_to(eq2, DOWN, buff=0.4)
        
        label3 = Text("Density of states (3D)", font_size=20).next_to(eq3, DOWN, buff=0.3)
        self.play(Write(eq3))
        self.play(Write(label3))
        self.wait(2)

        # Clear previous equations to make room
        self.play(FadeOut(eq1), FadeOut(label1), FadeOut(eq2))
        
        # Move remaining equations up
        self.play(eq3.animate.move_to(UP * 1.8), label3.animate.move_to(UP * 0.8))

        # Step 4: Substitute and show the integral
        eq4 = MathTex(
            r"N = \frac{V}{2\pi^2} \left(\frac{2m k_B T}{h^2}\right)^{3/2} \int_0^{\infty} \frac{x^{1/2}}{e^{x-\alpha} - 1} \, dx"
        ).scale(0.7).next_to(label3, DOWN, buff=0.4)
        
        substitution = MathTex(r"x = \frac{E}{k_B T}, \quad \alpha = \frac{\mu}{k_B T}").scale(0.7).next_to(eq4, DOWN, buff=0.3)
        
        self.play(Write(eq4))
        self.play(Write(substitution))
        self.wait(2)

        # Step 5: Show the polylogarithm solution
        eq5 = MathTex(
            r"\int_0^{\infty} \frac{x^{1/2}}{e^{x-\alpha} - 1} \, dx = \Gamma(3/2) \, \text{Li}_{3/2}(e^{\alpha})"
        ).scale(0.8).next_to(substitution, DOWN, buff=0.4)
        
        self.play(Write(eq5))
        self.wait(2)

        # Step 6: Final result
        self.play(FadeOut(eq3), FadeOut(label3), FadeOut(substitution))
        self.play(eq4.animate.move_to(UP * 1.5), eq5.animate.move_to(ORIGIN))

        final_result = MathTex(
            r"N = \frac{V}{2\pi^2} \left(\frac{2m k_B T}{h^2}\right)^{3/2} \frac{\sqrt{\pi}}{2} \, \text{Li}_{3/2}(e^{\mu/k_BT})"
        ).scale(0.7).next_to(eq5, DOWN, buff=0.5)

        self.wait(2)
        self.play(FadeOut(eq4), FadeOut(eq5))
        # Box the final result
        final_result.move_to(ORIGIN)
        box = SurroundingRectangle(final_result, color=YELLOW, buff=0.2)
        
        self.play(Write(final_result))
        self.play(Create(box))
        self.wait(2)

        # Step 7: Add explanation
        explanation = VGroup(
            Tex("\\rm{The Bose-Einstein integral is solved using the polylogarithm function} $Li_{3/2}(z)$", font_size=20),
            Tex("\\rm{This gives the number density of bosons in thermal equilibrium}", font_size=20),
            Tex("\\rm{where $\\mu$ is the chemical potential and $T$ is the temperature}", font_size=20)
        ).arrange(DOWN, buff=0.15).next_to(box, DOWN, buff=0.4)
        
        self.play(FadeIn(explanation))
        self.wait(3)

        # Step 8: Show special case for μ = 0 (photons)
        self.play(FadeOut(explanation))
        self.wait(1)
        self.play(Create(box.set_opacity(0)))
        final_result.animate.move_to(UP * 1.5)  # Make box transparent

        special_case = MathTex(
            r"\text{For photons } (\mu = 0): \quad N = \frac{V}{2\pi^2} \left(\frac{2m k_B T}{h^2}\right)^{3/2} \frac{\sqrt{\pi}}{2} \zeta(3/2)"
        ).scale(0.6).next_to(final_result, DOWN, buff=0.4)

        zeta_note = Tex("where $\\zeta(3/2) \\approx 2.612$ is the Riemann zeta function", font_size=22).next_to(special_case, DOWN, buff=0.2)

        self.play(Write(special_case))
        self.play(Write(zeta_note))
        self.wait(3)

class BoseEinsteinVisualization(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 2, 0.5],
            tips=False,
            axis_config={"include_numbers": True},
        ).scale(0.8)
        
        x_label = axes.get_x_axis_label("E / k_B T")
        y_label = axes.get_y_axis_label("n(E)")
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Title
        title = MathTex(r"\text{Bose-Einstein Distribution for Different Chemical Potentials}").scale(0.8).to_edge(UP)
        self.play(Write(title))
        
        # Define the Bose-Einstein distribution function
        def bose_einstein(x, mu_over_kT):
            return 1 / (np.exp(x - mu_over_kT) - 1)
        
        # Plot for different chemical potentials
        mu_values = [-2, -1, 0, 1]
        colors = [RED, BLUE, GREEN, YELLOW]
        
        curves = []
        labels = []
        
        for i, mu in enumerate(mu_values):
            # Create the curve
            x_vals = np.linspace(max(mu + 0.1, 0.1), 6, 100)
            y_vals = [bose_einstein(x, mu) for x in x_vals if bose_einstein(x, mu) < 10]
            x_vals = x_vals[:len(y_vals)]
            
            if len(x_vals) > 0 and len(y_vals) > 0:
                curve = axes.plot_line_graph(
                    x_vals, y_vals,
                    line_color=colors[i],
                    stroke_width=3
                )
                curves.append(curve)
                
                # Add label
                label = MathTex(f"\\mu/k_BT = {mu}", color=colors[i]).scale(0.6)
                labels.append(label)
        
        # Arrange labels
        legend = VGroup(*labels).arrange(DOWN, buff=0.2).to_corner(UR)
        
        # Animate the curves
        for curve, label in zip(curves, labels):
            self.play(Create(curve), Write(label), run_time=1.5)
            self.wait(0.5)
        
        self.wait(2)
        
        # Add explanation
        explanation = Text(
            "The integral under each curve gives the total number density",
            font_size=24
        ).to_edge(DOWN)
        
        self.play(Write(explanation))
        self.wait(3)