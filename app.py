import streamlit as st
from modules import ch4_interest_rates, ch3_hedging, duration_risk, bootstrapping, appendix_quant
from login import login_screen, check_login, logout

# =====================================================
# CONFIG
# =====================================================
st.set_page_config(page_title="CherryPlum Financial Engineering Lab", layout="wide")

# ================= LOGIN GATE =================
if not check_login():
    login_screen()
    st.stop()

# =====================================================
# DARK STYLE
# =====================================================
st.markdown("""
<style>
body {background-color:#0e1117; color:white;}
.block-container {padding-top:1rem;}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================
col1, col2 = st.columns([1,7])

with col1:
    st.image("logo.png", width=120)

with col2:
    st.title("CherryPlum Financial Engineering Lab")
    st.markdown("### Financial Engineering • Derivatives • Risk")
    st.caption("Developed by Malefane.H. Molibeli")

st.markdown("---")

# =====================================================
# LOGGED USER + LOGOUT
# =====================================================
if "user" in st.session_state:
    st.sidebar.success(f"Logged in as: {st.session_state['user']}")

if st.sidebar.button("Logout"):
    logout()
    st.rerun()

# =====================================================
# TOP NAVIGATION TABS (PROFESSIONAL)
# =====================================================
tabs = st.tabs([
    "Dashboard",
    "Interest Rates (Ch4)",
    "Hedging (Ch3)",
    "Duration & Convexity",
    "Bootstrapping",
    "Quant Appendix",
    "About"
])

# =====================================================
# DASHBOARD
# =====================================================
with tabs[0]:
    st.subheader("Welcome")

    st.markdown("""
This platform supports your Financial Engineering course  
and is built as a live computational laboratory.

You will use it to:

- Understand **Hull Chapter 3 — Hedging with Futures**
- Understand **Hull Chapter 4 — Interest Rates**
- Explore **FRAs and forward rates**
- Compute **duration & convexity**
- Build **zero curves**
- Develop quantitative intuition
""")

    st.markdown("### Course Structure")

    st.markdown("""
**Module 1:** Hedging with Futures (Hull Ch3)  
**Module 2:** Interest Rates & FRAs (Hull Ch4)  
**Module 3:** Duration & Convexity  
**Module 4:** Zero Curve Bootstrapping  
**Advanced Appendix:** Quant / FRM Mathematics  
""")

# =====================================================
# MODULES
# =====================================================
with tabs[1]:
    ch4_interest_rates.run()

with tabs[2]:
    ch3_hedging.run()

with tabs[3]:
    duration_risk.run()

with tabs[4]:
    bootstrapping.run()

with tabs[5]:
    appendix_quant.run()

# =====================================================
# ABOUT & LEGAL
# =====================================================
with tabs[6]:
    st.header("Academic Acknowledgement")

    st.markdown("""
This platform follows the structure and core concepts of:

**John C. Hull**  
*Options, Futures and Other Derivatives*

Used strictly for educational and training purposes.
""")

    st.markdown("### CherryPlum Financial Training")

    st.markdown("""
© CherryPlum Financial Training 2025. All rights reserved.  
Educational use only. Not financial advice.  
www.cherryplum.co.za
""")

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("CherryPlum Financial Training • © 2025 • All rights reserved")