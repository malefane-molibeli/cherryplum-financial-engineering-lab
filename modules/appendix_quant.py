import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():

    st.header("Advanced Quant Appendix (FRM / MFE Level)")
    st.markdown("### CherryPlum Financial Training")

    st.info("This section provides mathematical derivations used in professional quantitative finance.")

    # =========================================================
    # HEDGE RATIO DERIVATION — FULL VERSION
    # =========================================================
    st.subheader("1. Minimum Variance Hedge Ratio — Full Derivation")

    st.markdown("### Step 1: Hedged Portfolio")

    st.latex(r"P = S - hF")

    st.markdown("""
Where  
S = change in spot value  
F = change in futures value  
h = hedge ratio to be determined  
""")

    st.markdown("### Step 2: Portfolio Variance")

    st.latex(r"Var(P)=Var(S-hF)")

    st.markdown("Using variance rules:")

    st.latex(r"Var(P)=\sigma_S^2 + h^2\sigma_F^2 -2h\,Cov(S,F)")

    st.markdown("### Step 3: Express covariance using correlation")

    st.latex(r"Cov(S,F)=\rho\sigma_S\sigma_F")

    st.markdown("Correlation behaves like cosine between two risk vectors:")

    st.latex(r"\rho=\cos\theta")

    st.markdown("Substitute into variance:")

    st.latex(r"Var(P)=\sigma_S^2 + h^2\sigma_F^2 -2h\rho\sigma_S\sigma_F")

    st.markdown("### Step 4: Cosine Rule Interpretation")

    st.markdown("""
Treat spot and futures risk as vectors.

Cosine rule from geometry:
""")

    st.latex(r"|P|^2 = |S|^2 + |hF|^2 -2|S||hF|\cos\theta")

    st.markdown("""
Mapping to finance:
""")

    st.latex(r"|S|=\sigma_S,\quad |F|=\sigma_F,\quad \cos\theta=\rho")

    st.markdown("""
Hedging is equivalent to projecting spot risk onto futures risk.
""")

    st.markdown("### Step 5: Minimise variance")

    st.markdown("To obtain minimum risk, differentiate variance with respect to hedge ratio:")

    st.latex(r"\frac{d}{dh}Var(P)=2h\sigma_F^2-2\rho\sigma_S\sigma_F")

    st.markdown("Set derivative equal to zero:")

    st.latex(r"2h\sigma_F^2-2\rho\sigma_S\sigma_F=0")

    st.markdown("Solve for optimal hedge ratio:")

    st.latex(r"h^*\sigma_F^2=\rho\sigma_S\sigma_F")

    st.latex(r"h^*=\rho\frac{\sigma_S}{\sigma_F}")

    st.markdown("Equivalent covariance form:")

    st.latex(r"h^*=\frac{Cov(S,F)}{Var(F)}")

    st.markdown("### Step 6: Minimum achievable variance")

    st.latex(r"\sigma^2_{min}=\sigma_S^2(1-\rho^2)")

    st.success("Correlation determines hedge effectiveness. Higher correlation → better hedge.")

    st.markdown("### Regression Interpretation")

    st.latex(r"\Delta S=a+b\Delta F+\varepsilon")

    st.markdown("Slope coefficient b equals optimal hedge ratio.")

    st.markdown("---")

    # =========================================================
    # DURATION DERIVATION
    # =========================================================
    st.subheader("2. Duration and Convexity Derivation")

    st.latex(r"P(y)=\sum C_i e^{-yt_i}")

    st.markdown("Differentiate:")

    st.latex(r"\frac{dP}{dy}=-\sum t_iC_ie^{-yt_i}")

    st.latex(r"\frac{dP}{dy}=-DP")

    st.markdown("Second derivative gives convexity:")

    st.latex(r"\frac{d^2P}{dy^2}=Convexity")

    st.latex(r"\frac{\Delta P}{P}=-D\Delta y+\frac{1}{2}C(\Delta y)^2")

    st.markdown("---")

    # =========================================================
    # FORWARD RATE DERIVATION
    # =========================================================
    st.subheader("3. Forward Rate Derivation")

    st.markdown("No-arbitrage condition:")

    st.latex(r"(1+R_2)^{T_2}=(1+R_1)^{T_1}(1+f)^{T_2-T_1}")

    st.markdown("Continuous form:")

    st.latex(r"f(T_1,T_2)=\frac{R_2T_2-R_1T_1}{T_2-T_1}")

    st.markdown("---")

    # =========================================================
    # YIELD CURVE THEORY
    # =========================================================
    st.subheader("4. Term Structure Theories")

    st.markdown("""
**Expectations theory**  
Forward rates reflect expected future short rates.

**Liquidity preference**  
Long-term rates include risk premium.

**Market segmentation**  
Different maturities driven by supply/demand.
""")

    st.markdown("---")

    # =========================================================
    # SAMPLE QUANT PLOT
    # =========================================================
    st.subheader("5. Convexity Illustration")

    y=np.linspace(0.01,0.15,100)
    price=100*np.exp(-5*y)

    fig,ax=plt.subplots()
    ax.plot(y,price)
    ax.set_title("Bond Price vs Yield")
    ax.set_xlabel("Yield")
    ax.set_ylabel("Price")
    ax.grid(True)
    st.pyplot(fig)

    st.caption("""
Advanced mathematical framework aligned with:
John C. Hull — Options, Futures and Other Derivatives.
CherryPlum Financial Training · Educational use only.
""")
