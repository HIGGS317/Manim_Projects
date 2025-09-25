from manim import *
import math 


## Changes for portrait mode
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

class HermitePolynomials(Scene):
    def construct(self):
        
        title = Text("Hermite Polynomials Derivation", font_size=36)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))    
        eq_title = Text("Hermite Differential Equation:", font_size=30)
        equation = MathTex(r"y'' - 2xy' + 2ny = 0", font_size=36)
        equation_group = VGroup(eq_title, equation).arrange(DOWN, buff=0.5)
        self.play(Write(equation_group))
        self.wait(2)
        self.play(equation_group.animate.to_edge(UP))
       
        series_title = Text("Power Series Solution:", font_size=30)
        series = MathTex(r"y(x) = \sum_{k=0}^{\infty} a_k x^k", font_size=36)
        series_group = VGroup(series_title, series).arrange(DOWN, buff=0.5)
        self.play(Write(series_group))
        self.wait(2)
        self.play(series_group.animate.next_to(equation_group, DOWN, buff=0.5))

        self.play(FadeOut(series_group))
        
        deriv_title = Text("Derivatives:", font_size=30)
        y_prime = MathTex(r"y'(x) = \sum_{k=1}^{\infty} k a_k x^{k-1}", font_size=32)
        y_double_prime = MathTex(r"y''(x) = \sum_{k=2}^{\infty} k(k-1) a_k x^{k-2}", font_size=32)
        deriv_group = VGroup(deriv_title, y_prime, y_double_prime).arrange(DOWN, buff=0.3)
        self.play(Write(deriv_group))
        self.wait(2)
        self.play(deriv_group.animate.next_to(series_group, DOWN, buff=0.5))
        
        
        self.play(FadeOut(deriv_group), FadeOut(series_group))
        
        sub_title = Text("Substitute into the equation:", font_size=30)
        sub_eq = MathTex(
            r"\sum_{k=2}^{\infty} k(k-1) a_k x^{k-2}",
            r"- 2x \sum_{k=1}^{\infty} k a_k x^{k-1}",
            r"+ 2n \sum_{k=0}^{\infty} a_k x^k = 0",
            font_size=28
        )
        sub_group = VGroup(sub_title, sub_eq).arrange(DOWN, buff=0.5)
        self.play(Write(sub_group))
        self.wait(2)
        self.play(sub_group.animate.next_to(equation_group, DOWN, buff=0.5))
        
        # Simplify the second term
        simplify_title = Text("Simplify the second term:", font_size=30)
        simplify_eq = MathTex(
            r"-2x \sum_{k=1}^{\infty} k a_k x^{k-1} = -2 \sum_{k=1}^{\infty} k a_k x^k",
            font_size=32
        )
        simplify_group = VGroup(simplify_title, simplify_eq).arrange(DOWN, buff=0.5)
        self.play(Write(simplify_group))
        self.wait(2)
        self.play(simplify_group.animate.next_to(sub_group, DOWN, buff=0.5))
        
        # Shift indices
        self.play(FadeOut(sub_group), FadeOut(simplify_group))
        
        shift_title = Text("Shift indices to combine terms:", font_size=30)
        shift_eq1 = MathTex(
            r"\sum_{m=0}^{\infty} (m+2)(m+1) a_{m+2} x^m",
            r"- 2 \sum_{m=1}^{\infty} m a_m x^m",
            r"+ 2n \sum_{m=0}^{\infty} a_m x^m = 0",
            font_size=28
        )
        shift_group = VGroup(shift_title, shift_eq1).arrange(DOWN, buff=0.5)
        self.play(Write(shift_group))
        self.wait(2)
        self.play(shift_group.animate.next_to(equation_group, DOWN, buff=0.5))
        
        # Show recurrence relation
        self.play(FadeOut(shift_group))
        
        recur_title = Text("Recurrence Relation:", font_size=30)
        recur_eq = MathTex(
            r"a_{m+2} = -\frac{2(n-m)}{(m+2)(m+1)} a_m",
            font_size=36
        )
        recur_group = VGroup(recur_title, recur_eq).arrange(DOWN, buff=0.5)
        self.play(Write(recur_group))
        self.wait(2)
        self.play(recur_group.animate.next_to(equation_group, DOWN, buff=0.5))
        
        # Show examples
        self.play(FadeOut(recur_group), FadeOut(equation_group))
        
        examples_title = Text("Hermite Polynomial Examples:", font_size=36)
        self.play(Write(examples_title))
        self.wait(1)
        self.play(examples_title.animate.to_edge(UP))
        
        # Show H0
        h0 = MathTex(r"H_0(x) = 1", font_size=36)
        self.play(Write(h0))
        self.wait(1)
        
        # Show H1
        h1 = MathTex(r"H_1(x) = 2x", font_size=36)
        self.play(ReplacementTransform(h0, h1))
        self.wait(1)
        
        # Show H2
        h2 = MathTex(r"H_2(x) = 4x^2 - 2", font_size=36)
        self.play(ReplacementTransform(h1, h2))
        self.wait(1)
        
        # Show H3
        h3 = MathTex(r"H_3(x) = 8x^3 - 12x", font_size=36)
        self.play(ReplacementTransform(h2, h3))
        self.wait(1)
        
        # Show H4
        h4 = MathTex(r"H_4(x) = 16x^4 - 48x^2 + 12", font_size=36)
        self.play(ReplacementTransform(h3, h4))
        self.wait(2)
        
        # Final summary
        self.play(FadeOut(h4), FadeOut(examples_title))
        
        final_text = Text("Hermite polynomials are solutions to the\nHermite differential equation and are\nimportant in quantum mechanics.", 
        font_size=30, line_spacing=1.2)
        self.play(Write(final_text))
        self.wait(3)
        
        self.play(FadeOut(final_text))
        
        
        rodrigues_title = Text("Rodrigues Formula for Hermite Polynomials:", font_size=30)
        rodrigues_formula = MathTex(
            r"H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}",
            font_size=36
        )
        rodrigues_group = VGroup(rodrigues_title, rodrigues_formula).arrange(DOWN, buff=0.5)
        self.play(Write(rodrigues_group))
        self.wait(3)