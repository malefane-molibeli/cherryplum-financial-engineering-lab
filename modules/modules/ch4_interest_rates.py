import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():

    st.header("Interest Rate Lab — Term Structure & Interest Rate Models")

    st.markdown("### CherryPlum Financial Training")

    # ============================================================
    # SECTION 1 — COMPOUNDING & DISCOUNTING
    # ============================================================

    st.subheader("1. Compounding and Discounting")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
Financial engineering begins with the **time value of money**.

If interest rates are compounded continuously:
""")

        st.latex(r"FV = PV e^{rT}")

        st.markdown("Present value becomes:")

        st.latex(r"PV = FV e^{-rT}")

        st.markdown("""
Continuous compounding is fundamental in derivatives pricing  
because it allows smooth mathematical modelling.
""")

    with col2:
        st.markdown("#### Interactive Example")

        PV = st.number_input("Present Value", value=100)
        r = st.slider("Interest rate (%)", 0.0, 15.0, 8.0)/100
        T = st.slider("Years", 1, 10, 3)

        FV = PV*np.exp(r*T)

        st.metric("Future Value", round(FV,2))

        st.info("Continuous compounding grows smoothly over time.")

    st.markdown("---")

    # ============================================================
    # SECTION 2 — ZERO RATES & YIELD CURVE
    # ============================================================

    st.subheader("2. Zero Rates and Yield Curve")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
A **zero rate** is the interest rate for a single cash flow at maturity.

Each maturity has its own zero rate:
- 1-year rate
- 2-year rate
- 5-year rate

These form the **term structure of interest rates**.
""")

        st.latex(r"PV = FV e^{-R T}")

        st.markdown("""
The yield curve shows how interest rates vary with maturity.
""")

    with col2:
        st.markdown("#### Build Yield Curve")

        r1 = st.slider("1Y rate (%)",0.0,15.0,5.0)/100
        r2 = st.slider("2Y rate (%)",0.0,15.0,6.0)/100
        r3 = st.slider("3Y rate (%)",0.0,15.0,6.5)/100
        r5 = st.slider("5Y rate (%)",0.0,15.0,7.0)/100
        r10 = st.slider("10Y rate (%)",0.0,15.0,7.5)/100

        maturity=np.array([1,2,3,5,10])
        rates=np.array([r1,r2,r3,r5,r10])

        fig, ax = plt.subplots()
        ax.plot(maturity, rates, marker="o")
        ax.set_title("Yield Curve")
        ax.set_xlabel("Maturity")
        ax.set_ylabel("Zero Rate")
        ax.grid(True)
        st.pyplot(fig)

    st.markdown("---")

    # ============================================================
    # SECTION 3 — FORWARD RATES
    # ============================================================

    st.subheader("3. Forward Interest Rates")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
Forward rates represent future borrowing rates implied today.

They prevent arbitrage between different maturities.
""")

        st.latex(r"f(T_1,T_2)=\frac{R_2T_2 - R_1T_1}{T_2 - T_1}")

        st.markdown("""
Interpretation:

Locking in a future borrowing rate today  
removes uncertainty about future interest costs.
""")

    with col2:
        st.markdown("#### Forward Rate Calculator")

        R1 = st.slider("1Y zero (%)",0.0,15.0,5.0)/100
        R2 = st.slider("2Y zero (%)",0.0,15.0,6.0)/100

        f = (R2*2 - R1*1)/(2-1)

        st.metric("1→2 year forward rate", f"{round(f*100,2)}%")

    st.markdown("---")

    # ============================================================
    # SECTION 4 — FRA
    # ============================================================

    st.subheader("4. Forward Rate Agreements (FRA)")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
An FRA locks an interest rate today for borrowing or lending in the future.

If market rate exceeds contract rate → gain  
If market rate below contract rate → loss
""")

        st.latex(r"FRA = L(R_F - R_K)(T_2 - T_1)e^{-rT_1}")

        st.markdown("""
Where:
- L = notional  
- RF = market forward rate  
- RK = contract rate  
""")

    with col2:
        st.markdown("#### FRA Pricing Engine")

        L = st.number_input("Notional", value=1000000)
        RK = st.slider("Contract rate (%)",0.0,15.0,5.0)/100
        RF = st.slider("Market forward rate (%)",0.0,15.0,6.0)/100
        T1 = st.number_input("Start year",1.0)
        T2 = st.number_input("End year",2.0)
        disc = st.slider("Discount rate (%)",0.0,15.0,5.0)/100

        value = L*(RF-RK)*(T2-T1)*np.exp(-disc*T1)

        st.metric("FRA Value", f"{value:,.2f}")

    st.markdown("---")

    # ============================================================
    # SECTION 5 — BOND PRICING
    # ============================================================

    st.subheader("5. Bond Pricing Using Zero Rates")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
Bond price equals present value of all cashflows:

""")

        st.latex(r"P=\sum C_i e^{-R_i t_i}")

        st.markdown("""
Each cashflow discounted at its own zero rate.

This is the foundation of all fixed-income pricing.
""")

    with col2:
        st.markdown("#### Bond Price Calculator")

        face = st.number_input("Face value",100)
        coupon = st.slider("Coupon (%)",0.0,15.0,8.0)/100
        y = st.slider("Yield (%)",0.0,15.0,7.0)/100
        T = st.slider("Maturity",1,10,5)

        price=0
        for t in range(1,T+1):
            price+=face*coupon*np.exp(-y*t)
        price+=face*np.exp(-y*T)

        st.metric("Bond price", round(price,2))

    st.markdown("---")

    st.caption("""
Academic framework based on John C. Hull — Options, Futures and Other Derivatives.  
CherryPlum Financial Training · Educational use only.
""")
