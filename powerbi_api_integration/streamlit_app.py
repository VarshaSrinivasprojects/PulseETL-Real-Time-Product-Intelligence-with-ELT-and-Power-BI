import streamlit as st

st.title("Embedded Power BI Report Demo")

embed_url = "https://app.powerbi.com/reportEmbed?reportId=your-report-id&groupId=your-group-id"

st.markdown(f"""
<iframe width="800" height="600" src="{embed_url}" frameborder="0" allowFullScreen="true"></iframe>
""", unsafe_allow_html=True)
