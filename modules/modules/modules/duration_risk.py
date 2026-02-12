import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():

    st.header("Duration, DV01 & Convexity Lab")
    st.markdown("### CherryPlum Financial Training")

    # =====================================================
    # THEORY
    # =====================================================
    st.subheader("1. Duration Theory")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
Duration measures bond price sensitivity to interest rate changes.
""")

        st.latex(r"D=\frac{\sum t_i PV(C_i)}{Price}")

        st.markdown("Modified duration:")

        st.latex(r"D_{mod}=\frac{D}{1+y}")

        st.markdown("Price sensitivity:")

        st.latex(r"\frac{\Delta P}{P}\approx -D_{mod}\Delta y")

    with col2:
        st.info("Duration ≈ effective maturity of bond")

    st.markdown("---")

    # =====================================================
    # INTERACTIVE PRICE SENSITIVITY
    # =====================================================
    st.subheader("2. Price Sensitivity Engine")

    col1, col2 = st.columns(2)

    with col1:
        V=st.number_input("Bond/Portfolio value", value=100000000)
        duration=st.slider("Modified duration",0.1,15.0,4.5)
        convexity=st.slider("Convexity",0.0,200.0,60.0)
        y=st.slider("Current yield (%)",0.0,15.0,6.0)/100

    with col2:
        shock=st.slider("Yield shock (bps)",-300,300,100)
        dy=shock/10000

        pct_change=(-duration*dy)+0.5*convexity*(dy**2)
        value_change=V*pct_change

        st.metric("Approx % price change", f"{pct_change*100:.3f}%")
        st.metric("Value change", f"{value_change:,.0f}")

    st.markdown("---")

    # =====================================================
    # PRICE-YIELD CURVE
    # =====================================================
    st.subheader("3. Convexity Curve")

    shocks=np.linspace(-0.03,0.03,60)
    pct=(-duration*shocks)+0.5*convexity*(shocks**2)

    fig,ax=plt.subplots()
    ax.plot(shocks*100,pct*100)
    ax.set_xlabel("Yield change (%)")
    ax.set_ylabel("Price change (%)")
    ax.set_title("Price-Yield Convexity Relationship")
    ax.grid(True)
    st.pyplot(fig)

    # =====================================================
    # DV01
    # =====================================================
    st.subheader("4. DV01 (Dollar Value of 1bp)")

    dv01=V*duration*0.0001
    st.metric("DV01", f"{dv01:,.0f}")

    st.markdown("""
DV01 measures dollar change for 1 basis point move in yield.
Used daily by banks and asset managers.
""")

    st.caption("""
Academic framework based on John C. Hull — Options, Futures and Other Derivatives.  
CherryPlum Financial Training · Educational use only.
""")
