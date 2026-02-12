import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():

    st.header("Advanced Quant Appendix (FRM / MFE Level)")
    st.markdown("### CherryPlum Financial Training")

    st.info("This section provides mathematical derivations used in professional quantitative finance.")

    # =========================================================
    # HEDGE RATIO DERIVATION
    # =========================================================
    st.subheader("1. Optimal Hedge Ratio — Mathematical Derivation")

    st.latex(r"Var(\Delta P)=Var(\Delta S-h\Delta F)")
    st.latex(r"= \sigma_S^2 + h^2\sigma_F^2 -2h\rho\sigma_S\sigma_F")

    st.markdown("Minimise variance → differentiate:")

    st.latex(r"\frac{d}{dh}Var=2h\sigma_F^2-2\rho\sigma_S\sigma_F=0")

    st.latex(r"h^*=\rho\frac{\sigma_S}{\sigma_F}")

    st.markdown("Regression interpretation:")

    st.latex(r"\Delta S=a+b\Delta F+\varepsilon")

    st.markdown("b equals optimal hedge ratio.")

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
