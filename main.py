import streamlit as st
import pandas as pd

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
