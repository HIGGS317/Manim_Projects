from manim import *

class SolveSchrodinger(Scene): 
    def construct(self):
        
        # Original Schrödinger equation
        sch = MathTex(
            r"-\frac{\hbar^2}{2m}\frac{d^2 \psi}{dx^2} + \frac{1}{2}m\omega^2x^2 \psi = E\psi"
        )
        self.play(Write(sch))
        self.wait(1)

        # Introduce alpha and beta
        alpha_beta = MathTex(
            r"\alpha = \frac{m\omega}{\hbar},\quad \beta = \frac{2mE}{\hbar^2}"
        )
        self.play(Write(alpha_beta.next_to(sch, DOWN)))
        self.wait(1)

        # Simplified form
        simplified = MathTex(
            r"\frac{d^2\psi}{dx^2} + (\beta - \alpha^2 x^2)\psi = 0"
        )
        self.play(TransformMatchingTex(sch, simplified))
        self.wait(1.5)
        self.play(FadeOut(alpha_beta))
        self.wait(1) 
        # Substitution x -> sqrt(alpha) * y
        substitution = MathTex(
            r"x = \sqrt{\frac{1}{\alpha}} y \quad \Rightarrow \quad",
            r"\frac{d^2 \psi}{dy^2} + (\lambda - y^2)\psi = 0"
        ).next_to(simplified, DOWN)
        self.play(Write(substitution))
        self.wait(1.5)






        # Hermite solution
        hermite = MathTex(
            r"\psi_n(y) = N_n e^{-y^2/2} H_n(y)"
        ).next_to(substitution, DOWN)
        self.play(Write(hermite))
        self.wait(1.5)




        # Energy eigenvalues
        energy = MathTex(
            r"E_n = \hbar \omega \left(n + \tfrac{1}{2}\right)"
        ).next_to(hermite, DOWN)
        self.play(Write(energy))
        self.wait(2)
        # Final highlight
        step9 = MathTex(    
            r"\text{Step 9: Solve the differential equation}"
        ).next_to(energy, DOWN)
        self.play(Write(step9))
        self.wait(2) 