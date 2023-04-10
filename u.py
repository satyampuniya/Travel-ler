#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from streamlit_lottie import st_lottie
import streamlit as st
#from streamlit_extras.colored_header import colored_header

st.set_page_config(page_title = "Travel-ler" , page_icon = ":minibus:", layout = "wide")


def get_lottie(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles.css")


#ASSET INVENTORY
lottie_url = get_lottie("https://assets9.lottiefiles.com/packages/lf20_bhebjzpu.json")

#HEADER SECTION

with st.container():
    lc, rc = st.columns([3,2])
    with lc:
        st.title("Book your traveller with Travel-ler")
        st.write("Booking a traveller has never been this easy!")
        st.subheader("Pilot program based in Delhi-NCR :construction:")
    with rc:
        st_lottie(lottie_url,height = 300,key ="Travel")

with st.container():
	#st.write("---")
	st.subheader("Your Destination Awaits - We'll Get You There Safely and Swiftly!")	
	st.write("Go big on your next adventure with our minibus booking company. Whether you're planning a group excursion, corporate event, or airport transfer, our fleet of modern minibuses are at your service. From luxurious leather seats to ample luggage space, our minibuses are designed with your comfort and convenience in mind.  So sit back, relax, and enjoy the ride with our reliable minibus rental service. Book with us today and experience the ultimate in group travel!")

with st.container():
    form = """<form action="https://formsubmit.co/satyampuniya_pr@srmuniv.edu.in" method="POST">
        <div>
	<label>Name</label>
        <input type="text" name="name" placeholder="Your name" required>
        </div>
	<div>
	<label>Contact Number</label>
	<input type="tel" name="nmbr" pattern="[0-9]{10}" placeholder="Phone Number">
	</div>
	<div>
	<label>Email Id</label>
	<input type="email" name="email" placeholder="Your email" required>
        </div>
	<div>
	<label>Start Date</label>
	<input type="date" name="start_date" required>
	</div>
	<div>	
	<label>Return Date</label>
	<input type="date" name="end_date" required>
	</div>
        <button type="submit">Submit</button>
    </form>"""
    st.markdown(form, unsafe_allow_html = True)
    

# In[ ]:




