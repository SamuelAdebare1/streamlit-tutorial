import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np


table = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5, 6, 7], "Column 2": [
                     11, 12, 13, 14, 15, 16, 17]})
st.markdown("""
<style>
   #MainMenu {
            visibility: hidden;
   }        
</style>
""", unsafe_allow_html=True)
st.title("Hi! I am streamlit Web App")
st.subheader("Hi! I am streamlit subheader")
st.header("Hi1 I am streamlit header")
st.text("Hi, I am text paragraph")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {"a": "1,2,3", "b": "4,5,6"}
st.json(json)
code = """
print("Hello universe")
def funct():
    return 0;
"""
st.code(code, language="python")
st.write("## H2")
st.metric(label="Wind Speed", value="120ms⁻¹", delta="-1.4ms⁻¹")
st.table(table)
st.dataframe(table)
st.image("airplane.jpg", caption="This is an airplane view", width=680)
st.audio("airplane.mp3")
st.video("cloud.mp4")


def change():
    # print("changed")
    print(st.session_state.checker)


state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")
# if state:
#     st.write("Hi")
# radio_btn = st.radio("In which country do you live in?",
#                      options=["US", "UK", "Canada"])
# print(radio_btn)


def btn_click():
    print("Button Clicked")


btn = st.button("Click Me", on_click=btn_click)
select = st.selectbox("What is your favorurite auto brand?",
                      options=["Audi", "Toyota", "Tesla"])
print(select)
multi_select = st.multiselect("What is your favourite tech brand?", options=[
                              "Google", "Apple", "Microsoft", "Meta"])
st.write(multi_select)
st.title("Uploading files")
images = st.file_uploader("Please upload an image", type=["png", "jpg"])
if images is not None:
    for image in images:
        st.image(image)
video = st.file_uploader("Please upload a video", type="mp4")
# if video is not None:
#     st.video(video)
# val = st.slider("This is a slier", min_value=50, max_value=150, value=70)
# val = st.text_input("Text input", max_chars=60)
# val = st.text_area("Course description")
# val = st.date_input("Enter your registration date")
# val = st.time_input("Set timer")

# print(val)


def converter(value):
    m, s, mm = value.split(":")
    # converts m(minute), s(seconds), mm(milliseconds) to seconds
    t_s = int(m)*60 + int(s)+int(mm)/1000
    return t_s


val = st.time_input("Set Timer", value=time(0, 0, 0))
if str(val) == "00:00:00":
    st.write("Please set timer")
else:
    sec = converter(str(val))
    print(sec)
    bar = st.progress(0)
    per = sec/100
    progress_status = st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + "%")
        ts.sleep(per)

st.markdown("<h1>User Registration</h1>", unsafe_allow_html=True)
# first method
form = st.form("Form 1")
form.text_input("First Name")
form.form_submit_button("Submit")
# second method
with st.form("Form 2", clear_on_submit=True):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last Name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year = st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state = st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please fill the above fields")
        else:
            st.success("Submitted Successfully")

# =========Side Bar and Graph========
x = np.linspace(0, 10, 100)
bar_x = np.array([1, 2, 3, 4, 5])
opt = st.sidebar.radio("Select any Graph", options=("Line", "Bar", "H-bar"))
# st.sidebar.write("This is a side bar" )
if opt == "Line":
    st.markdown("<h1 style='text-align: center;'>Line Chart</h1>",
                unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    st.write(fig)
elif opt == "Bar":
    st.markdown("<h1 style='text-align: center;'>Bar Chart</h1>",
                unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align: center;'>H-Bar Chart</h1>",
                unsafe_allow_html=True)
    fig = plt.figure()
    plt.style.use(
        "https://raw.githubusercontent.com/dhaitz/matplotlib-stylesheets/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    st.write(fig)
