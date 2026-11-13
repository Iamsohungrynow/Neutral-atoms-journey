# Erasures versus bit-flip errors in a repetition code

Theory: [Chapter 12](../../tutorial/12-architectures.md)

## What you simulate

A logical bit stored in $d$ copies (the repetition code, $d=3,5,7$) and decoded
by majority vote. Each copy independently suffers an error with probability
$p$; a fraction $R_e$ of those errors are **erasures** (the copy is lost and we
know which one, like an empty tweezer in a fluorescence image) and the rest are
**bit flips** at unknown locations. The decoder votes among the non-erased
copies; ties and fully erased blocks are decided by a coin toss.

The exact logical error sums over the numbers of erasures $e$ and flips $f$
with multinomial weights:

$$P_L=\sum_{e,f}\frac{d!}{e!\,f!\,(d-e-f)!}(R_ep)^e\big((1-R_e)p\big)^f(1-p)^{d-e-f}\times\begin{cases}1&2f>d-e\\\tfrac12&2f=d-e\\0&\text{otherwise}\end{cases}$$

This is a classical-bit model. It does not protect an arbitrary quantum superposition against erasure: tracing out one qubit from $\alpha|0\rangle^{\otimes d}+\beta|1\rangle^{\otimes d}$ destroys its branch coherence.

Limits: pure flips give $3p^2-2p^3$ for $d=3$ and scale as $p^{(d+1)/2}$; pure
erasures give $p^d/2$.

## Run it

Run these commands from the **repository root**, using the environment from the [shared setup](../README.md).

    python -m pip install -r hands-on/requirements.txt
    python hands-on/12-erasure-code/erasure.py

## The code explained

`p_logical(d, p, Re)` evaluates the double sum above. `p_logical_mc` draws one
uniform random number per copy and classifies it as an erasure
($u<R_ep$), a flip ($R_ep\le u<p$) or no error, then applies the decoder to
400 000 blocks. The slope $d\ln P_L/d\ln p$ at small $p$ is the smallest number of faults that
can cause a failure; it is computed from the exact formula.

## Expected output

     d   model                         P_L MC (p = 0.3)      exact
     3   bit-flip only (R_e = 0)          2.155e-01 +/- 6.5e-04   2.160e-01
     3   98% erasures (R_e = 0.98)     1.846e-02 +/- 2.1e-04   1.807e-02
     3   erasure only (R_e = 1)        1.356e-02 +/- 1.8e-04   1.350e-02
     5   bit-flip only (R_e = 0)          1.626e-01 +/- 5.8e-04   1.631e-01
     5   98% erasures (R_e = 0.98)     2.535e-03 +/- 8.0e-05   2.544e-03
     5   erasure only (R_e = 1)        1.265e-03 +/- 5.5e-05   1.215e-03
     7   bit-flip only (R_e = 0)          1.259e-01 +/- 5.2e-04   1.260e-01
     7   98% erasures (R_e = 0.98)     3.900e-04 +/- 3.1e-05   3.884e-04
     7   erasure only (R_e = 1)        1.225e-04 +/- 1.7e-05   1.093e-04
    small-p slope d ln P_L / d ln p (the number of faults needed to cause a failure):
       d = 3: bit-flip 2.00 (expect 2.0), erasure 3.00 (expect 3), 98% erasure 2.01
       d = 5: bit-flip 3.00 (expect 3.0), erasure 5.00 (expect 5), 98% erasure 3.04
       d = 7: bit-flip 4.00 (expect 4.0), erasure 7.00 (expect 7), 98% erasure 4.10
    at p = 1e-2, d = 5: bit-flip 9.85e-06, 98% erasure 7.88e-09, erasure 5.00e-11

The Monte Carlo comparison uses $p=0.3$, large enough that every case produces
at least dozens of failures in 400 000 shots, so the check is informative for the
erasure-dominated codes too.

![Logical error versus physical error, and versus erasure fraction](figures/erasure.png)

Left: logical error versus $p$. Pure erasures (dotted) fall almost twice as steeply as
bit-flip errors (solid): exponent $d$ instead of $(d+1)/2$. With 98% conversion (dashed), the small residual bit-flip rate
eventually sets the slope, but the curve sits orders of magnitude lower. Right:
the logical error at $p=1\%$ versus $R_e$ decreases throughout the range, with
the steepest reduction near complete conversion. For $d=5$, the improvement is
about 3.2 times at $R_e=0.5$ and 65 times at $R_e=0.9$.

The runner checks the Monte Carlo against the exact sum, the closed-form limits
$3p^2-2p^3$ and $p^d/2$, and the failure exponents $(d+1)/2$ and $d$.

## Try this

1. At what erasure fraction does the $d=5$ code reach $10^{-8}$ at $p=1\%$?
2. Add a probability $q$ that an erasure check itself misses an erasure (so
   some erasures become unknown errors). How small must $q$ be to keep most of
   the benefit?
3. Model an atom that is lost and **replaced** by a fresh atom in a random
   state. Is that an erasure, a flip, or neither?
