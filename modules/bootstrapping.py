import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():

    st.header("Zero Curve Bootstrapping Lab")
    st.markdown("### CherryPlum Financial Training")

    st.markdown("""
Bootstrapping derives zero rates from market bond prices.
Each maturity is solved sequentially.
""")

    # =====================================================
    # INPUT BONDS
    # =====================================================
    st.subheader("Input Bond Market Data")

    col1, col2 = st.columns(2)

    with col1:
        P1 = st.number_input("1Y zero bond price", value=95.0)
        P2 = st.number_input("2Y bond price (coupon)", value=97.0)
        c2 = st.slider("2Y coupon (%)",0.0,15.0,5.0)/100

        P3 = st.number_input("3Y bond price (coupon)", value=98.0)
        c3 = st.slider("3Y coupon (%)",0.0,15.0,6.0)/100

    with col2:
        st.info("""
We solve zero rates sequentially:

1Y rate from zero bond  
2Y rate from 2Y bond  
3Y rate from 3Y bond  
""")

    # =====================================================
    # BOOTSTRAP
    # =====================================================
    R1 = -np.log(P1/100)/1

    C2 = 100*c2
    R2 = -np.log((P2 - C2*np.exp(-R1*1))/(100+C2))/2

    C3 = 100*c3
    R3 = -np.log((P3 - C3*np.exp(-R1*1) - C3*np.exp(-R2*2))/(100+C3))/3

    st.subheader("Bootstrapped Zero Rates")

    st.metric("1Y zero rate", f"{R1*100:.3f}%")
    st.metric("2Y zero rate", f"{R2*100:.3f}%")
    st.metric("3Y zero rate", f"{R3*100:.3f}%")

    # =====================================================
    # PLOT CURVE
    # =====================================================
    maturities=[1,2,3]
    rates=[R1,R2,R3]

    fig, ax = plt.subplots()
    ax.plot(maturities,rates,marker="o")
    ax.set_title("Bootstrapped Zero Curve")
    ax.set_xlabel("Maturity")
    ax.set_ylabel("Zero rate")
    ax.grid(True)
    st.pyplot(fig)

    st.markdown("""
This zero curve is used for:
- bond pricing  
- FRA pricing  
- swaps  
- derivatives  
""")

    st.caption("""
Academic framework based on John C. Hull — Options, Futures and Other Derivatives.  
CherryPlum Financial Training · Educational use only.
""")
