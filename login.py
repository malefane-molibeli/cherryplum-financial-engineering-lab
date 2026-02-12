import streamlit as st

USERS = {
    "fe2026@cherryplum.co.za": "hull2026",
    "admin@cherryplum.co.za": "cherryplum"
}

def login_screen():

    top1, top2, top3 = st.columns([1,2,1])
    with top2:
        st.image("logo.png", width=120)

    st.markdown("")

    left, center, right = st.columns([2,3,2])

    with center:

        st.markdown("### CherryPlum Financial Engineering Lab")
        st.caption("Student Access Portal")

        st.markdown("")

        username = st.text_input("Email")
        password = st.text_input("Password", type="password")

        st.markdown("")

        if st.button("Login", use_container_width=True):

            if username in USERS and USERS[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["user"] = username
                st.success("Access granted")
                st.rerun()
            else:
                st.error("Invalid login details")

def check_login():
    return st.session_state.get("logged_in", False)

def logout():
    st.session_state["logged_in"] = False
    st.session_state["user"] = None