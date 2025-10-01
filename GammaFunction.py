# save as gamma_recurrence.py and run with e.g.
# manim -pql gamma_recurrence.py GammaRecurrence
from manim import *

class GammaFunction(Scene):
    def construct(self):
        title = Title("Gamma function: recurrence and half-integer example")
        self.play(Write(title))
        self.wait(0.4)

        # 1. Definition
        gamma_def = MathTex(r"\Gamma(z) = \int_{0}^{\infty} t^{\,z-1} e^{-t}\,dt")
        gamma_def.to_edge(UP)
        self.play(Write(gamma_def))
        self.wait(0.6)

        # 2. Replace z -> z+1
        step1 = MathTex(
            r"\Gamma(z+1) = \int_{0}^{\infty} t^{\,z} e^{-t}\,dt"
        ).next_to(gamma_def, DOWN, buff=0.8)
        self.play(Write(step1))
        self.wait(0.5)

        # 3. Integration by parts setup
        ibp_setup = MathTex(
            r"\text{Integration by parts: } u=t^{z},\quad dv=e^{-t}dt"
        ).scale(0.8).next_to(step1, DOWN, buff=0.6)
        self.play(Write(ibp_setup))
        self.wait(0.5)

        # 4. Compute du and v
        du_v = MathTex(
            r"du = z t^{z-1}dt,\qquad v=-e^{-t}"
        ).scale(0.8).next_to(ibp_setup, DOWN, buff=0.3)
        self.play(Write(du_v))
        self.wait(0.6)

        # 5. Integration by parts formula line
        ibp_line = MathTex(
            r"\Gamma(z+1)=\Big[-t^{z} e^{-t}\Big]_{0}^{\infty} + z\int_{0}^{\infty} t^{\,z-1} e^{-t}dt"
        ).next_to(du_v, DOWN, buff=0.6)
        self.play(Write(ibp_line))
        self.wait(0.6)

        # 6. Show boundary term is zero
        bdry_explain = MathTex(
            r"\text{Boundary term } \Big[-t^{z} e^{-t}\Big]_{0}^{\infty}=0"
        ).scale(0.8).next_to(ibp_line, DOWN, buff=0.4)
        self.play(Write(bdry_explain))
        self.wait(0.6)

        # 7. Conclude recurrence
        recurrence = MathTex(
            r"\Rightarrow\qquad \Gamma(z+1)=z\Gamma(z)"
        ).next_to(bdry_explain, DOWN, buff=0.6)
        self.play(Write(recurrence))
        self.wait(1.0)

        # Emphasize the recurrence
        self.play(recurrence.animate.scale(1.15))
        self.wait(0.4)
        self.play(recurrence.animate.scale(1/1.15))

        # 8. Apply to z = 1/2
        apply_half = MathTex(
            r"\text{Take } z=\tfrac12:",
            r"\quad \Gamma\!\big(\tfrac32\big)=\tfrac12\,\Gamma\!\big(\tfrac12\big)"
        ).arrange(DOWN, aligned_edge=LEFT).next_to(recurrence, DOWN, buff=0.8)
        self.play(Write(apply_half[0]))
        self.play(Write(apply_half[1]))
        self.wait(0.8)

        # 9. Reminder: Gamma(1)=1 and Gamma(1/2)=sqrt(pi)
        facts = MathTex(
            r"\Gamma(1)=\int_{0}^{\infty} e^{-t}dt = 1,\qquad"
            r"\Gamma\!\big(\tfrac12\big)=\sqrt{\pi}"
        ).scale(0.9).next_to(apply_half, DOWN, buff=0.6)
        self.play(Write(facts))
        self.wait(0.8)

        # 10. Numeric substitution and final result
        numeric = MathTex(
            r"\therefore\; \Gamma\!\big(\tfrac32\big)=\tfrac12\sqrt{\pi}."
        ).next_to(facts, DOWN, buff=0.6)
        self.play(Write(numeric))
        self.wait(1.0)

        # 11. Correct the mistaken equality the user wrote and emphasize
        correction = MathTex(
            r"\text{Note: } \Gamma\!\big(\tfrac12+1\big)=\Gamma\!\big(\tfrac32\big)\neq\Gamma(1)."
        ).scale(0.9).next_to(numeric, DOWN, buff=0.6)
        self.play(Write(correction))
        self.wait(1.0)

        # 12. Summarize in a box
        box = SurroundingRectangle(VGroup(recurrence, apply_half[1], numeric), buff=0.4)
        box_text = MathTex(r"\text{Recurrence \& half-integer example}").scale(0.65)
        box_text.next_to(box, UP, buff=0.1)
        self.play(Create(box), Write(box_text))
        self.wait(1.2)

        self.play(FadeOut(VGroup(title, gamma_def, step1, ibp_setup, du_v,
                                 ibp_line, bdry_explain, apply_half[0],
                                 facts, correction)))
        self.play(box.animate.to_edge(UP))
        self.wait(0.6)

        final = MathTex(
            r"\Gamma(z+1)=z\Gamma(z)", r"\qquad",
            r"\Gamma\!\big(\tfrac32\big)=\tfrac12\sqrt{\pi}", r"\qquad",
            r"\Gamma(1)=1"
        ).scale(0.9).next_to(box, DOWN, buff=0.6)
        self.play(Write(final))
        self.wait(1.4)
