import streamlit as st
import spacy
import en_core_web_sm
from newspaper import Article
from spacy import displacy

nlp = en_core_web_sm.load()

st.title("NER DEMO")
if st.button("About"):
    st.info("This app will take an input from the user and then prints the named entities")

select = st.selectbox("Select one of the options:",['None','Paragraph','URL'])

if select == 'Paragraph':
    text = st.text_area("Enter a paragraph")

    if(st.button("Analyze")):
        doc = nlp(text)
        ent_html = displacy.render(doc, style="ent", jupyter=False)
        # Display the entity visualization in the browser:
        st.markdown(ent_html, unsafe_allow_html=True)

elif select == "URL":
    url = st.text_area("Enter url")

    if st.button("Analyze"):
        article = Article(url)
        article.download()
        article.parse()
        doc=nlp(article.text)
        ent_html = displacy.render(doc, jupyter=False, style='ent')
        st.markdown(ent_html, unsafe_allow_html=True)

else:
    st.write("you selected",select)