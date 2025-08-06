import streamlit as st
import pandas as pd

st.set_page_config(page_title="Pro Sports Agent Finder", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("agents_database.csv")

agents = load_data()

st.title("🏈 Pro Sports Agent Finder")
st.write("Helping athletes like Jonathan Ross connect with top NFL agents.")

st.sidebar.header("Athlete Profile")
name = st.sidebar.text_input("Full Name", "Jonathan Ross")
team = st.sidebar.text_input("Current Team & League", "Bay Area Panthers, IFL")
position = st.sidebar.text_input("Position", "Defensive Line")
tfl = st.sidebar.number_input("Tackles for Loss", min_value=0, value=10)
sacks = st.sidebar.number_input("Sacks", min_value=0, value=5)
highlight = st.sidebar.text_input("Highlight Reel Link", "https://youtube.com/...")
email = st.sidebar.text_input("Email", "jonathanross@email.com")
phone = st.sidebar.text_input("Phone", "555-555-5555")

if st.sidebar.button("Find Agents"):
    st.subheader("Top Agent Matches")
    st.dataframe(agents)

    st.subheader("Outreach Templates")

    st.markdown(f"""
    **Email:**

    Hello [Agent Name],

    My name is **{name}**, currently playing {position} for {team}.
    I currently have {tfl} TFL and {sacks} sacks this season.

    Here is my highlight reel: {highlight}

    I’d love to connect and discuss representation opportunities.

    Best regards,  
    {name}  
    Phone: {phone}  
    Email: {email}
    """)

    st.markdown(f"""
    **Text Message:**

    Hello [Agent Name], this is {name} ({position}, {team}).
    I hold the franchise record in Tackles for Loss and am seeking representation 
    to transition into the NFL. Can I send you my highlight reel?
    """)

    st.markdown(f"""
    **Phone Call Script:**

    Hi [Agent Name], this is {name}, {position} for {team}.
    I hold the record for Tackles for Loss with the franchise, and I’m seeking 
    representation to make the move to the NFL. 
    I’d like to share my highlight reel and discuss how we might work together. 
    When would be a good time to talk further?
    """)
