import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def run():

    st.header("Futures Hedging Lab — Risk Management with Futures")

    st.markdown("### CherryPlum Financial Training")

    # =========================================================
    # WHAT IS HEDGING
    # =========================================================
    st.subheader("1. Purpose of Hedging")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
Hedging uses futures contracts to reduce exposure to price risk.

A hedger sacrifices upside potential to reduce uncertainty.

Two types:
- **Short hedge** → protect against falling prices  
- **Long hedge** → protect against rising prices  
""")

        st.latex(r"Hedging\ reduces\ variance,\ not\ necessarily\ losses")

    with col2:
        st.info("Hedging converts uncertain future price into known effective price.")

    st.markdown("---")

    # =========================================================
    # LONG SHORT HEDGE
    # =========================================================
    st.subheader("2. Long vs Short Hedge")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
**Short hedge**
Used when asset will be sold in future.

**Long hedge**
Used when asset will be purchased in future.
""")

    with col2:
        exposure = st.number_input("Exposure value", value=1000000)
        price_move = st.slider("Price change (%)",-20.0,20.0,5.0)/100

        unhedged = exposure*(1+price_move)
        st.metric("Unhedged value", round(unhedged,2))

    st.markdown("---")

    # =========================================================
    # BASIS RISK
    # =========================================================
    st.subheader("3. Basis Risk")

    col1, col2 = st.columns(2)

    with col1:
        st.latex(r"Basis = S - F")

        st.markdown("""
Basis risk arises because spot and futures prices do not move perfectly together.

At maturity:
""")
        st.latex(r"F_T = S_T")

    with col2:
        st.markdown("#### Spot vs Futures Simulation")

        t=np.arange(50)
        spot=100+np.cumsum(np.random.normal(0,1,50))
        futures=spot+np.random.normal(0,1,50)

        fig,ax=plt.subplots()
        ax.plot(spot,label="Spot")
        ax.plot(futures,label="Futures")
        ax.legend()
        ax.set_title("Basis Risk Example")
        st.pyplot(fig)

    st.markdown("---")

    # =========================================================
    # OPTIMAL HEDGE RATIO
    # =========================================================
    st.subheader("4. Optimal Hedge Ratio")

    col1, col2 = st.columns(2)

    with col1:
        st.latex(r"h^*=\rho\frac{\sigma_S}{\sigma_F}")

        st.markdown("""
Optimal hedge ratio minimises variance of hedged position.

Can be estimated using regression:
""")

        st.latex(r"\Delta S = a + b\Delta F")

        st.markdown("b is the hedge ratio.")

    with col2:
        rho=st.slider("Correlation",0.0,1.0,0.8)
        sigma_s=st.slider("Spot volatility",0.1,5.0,2.0)
        sigma_f=st.slider("Futures volatility",0.1,5.0,1.8)

        h=rho*(sigma_s/sigma_f)

        st.metric("Optimal hedge ratio", round(h,3))

    st.markdown("---")

    # =========================================================
    # NUMBER OF CONTRACTS
    # =========================================================
    st.subheader("5. Optimal Number of Contracts")

    col1, col2 = st.columns(2)

    with col1:
        st.latex(r"N=h^*\frac{Exposure}{Futures\ Value}")

    with col2:
        exposure=st.number_input("Exposure", value=5000000)
        futures_value=st.number_input("Futures contract value", value=100000)
        hedge_ratio=st.slider("Hedge ratio",0.0,2.0,1.0)

        N=hedge_ratio*exposure/futures_value
        st.metric("Contracts required", round(N,2))

    st.markdown("---")

    # =========================================================
    # EQUITY HEDGE
    # =========================================================
    st.subheader("6. Equity Portfolio Hedge")

    col1, col2 = st.columns(2)

    with col1:
        st.latex(r"N=\frac{\beta V}{FQ}")

    with col2:
        beta=st.slider("Portfolio beta",0.0,2.0,1.1)
        V=st.number_input("Portfolio value", value=10000000)
        F=st.number_input("Index futures price", value=4000)
        Q=st.number_input("Multiplier", value=10)

        N=(beta*V)/(F*Q)
        st.metric("Index futures to short", round(N,2))

    st.markdown("---")

    # =========================================================
    # METALLGESELLSCHAFT
    # =========================================================
    st.subheader("7. Metallgesellschaft Case Study")

    st.markdown("""
A major hedging failure in 1993.

Firm used short-term futures to hedge long-term oil contracts.

Problems:
- liquidity risk
- margin calls
- roll risk
- mismatch of maturities

Lesson:
> Hedging reduces price risk but can introduce liquidity risk.
""")

    st.caption("""
Academic framework based on John C. Hull — Options, Futures and Other Derivatives.  
CherryPlum Financial Training · Educational use only.
""")