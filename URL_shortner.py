import streamlit as st
import pyshorteners as pyst
import pyperclip
from PIL import Image
from PIL.ImageFilter import *
import re
from pydub import AudioSegment, silence
import speech_recognition as sr
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
#-----------------------------------------------
st.set_page_config(page_title="KP WEB APP", page_icon=":sunglasses:", layout="centered", initial_sidebar_state="expanded")
with st.sidebar:
    option = option_menu("SELECT WHAT YOU WANT(KP MODEL)", options=["URL SHORTNER", "IMAGE EDITOR", "WORD DENSITY CHECKER", "AUDIO TO TEXT CONVERTER"],
    icons=[":grinning:",":stuck_out_tongue_winking_eye:",":grinning:","kissing"], default_index=0)
#option = st.sidebar.radio("SELECT WHAT YOU WANT", options=["URL SHORTNER", "IMAGE EDITOR", "WORD DENSITY CHECKER", "AUDIO TO TEXT CONVERTER"],ic)
#--------------------------------------------
st.markdown("""  
<style>

.css-1rs6os.edgvbvh3
{
    visibility: hidden;
}
</style>""",unsafe_allow_html=True)
#following code is used to remove "made with streamlit" 
st.markdown("""
<style>
.css-1lsmgbg.egzxvld0
{
    visibility: hidden;
 } 
</style>""", unsafe_allow_html=True)
#---------------------------------------------
def lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
loettie_1 = lottie("https://assets10.lottiefiles.com/packages/lf20_7fCbvNSmFD.json")
loettir_2 = lottie("https://assets2.lottiefiles.com/packages/lf20_qavaymcn.json")
loettir_3 = lottie("https://assets3.lottiefiles.com/packages/lf20_CZva9peGiW.json")
loettir_4 = lottie("https://assets6.lottiefiles.com/packages/lf20_BgywoUBeiL.json")
#-----------------------------------------------
if option=="URL SHORTNER":
    shortner = pyst.Shortener()
    st.sidebar.markdown("-----------")
    st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.sidebar.markdown("This is web app used for to short long website links we can use it if u want")
    #--------------------------------
    st.markdown("<h1 style='text-align: center;'>URL SHORTNER(KP MODEL)</h1>", unsafe_allow_html=True)
    #---------------------------------
    form = st.form("Name")
    url = form.text_input("URL HERE")
    but = form.form_submit_button("SHORT")
    st_lottie(loettie_1)
    #----------------------------------
    def copying():
        pyperclip.copy(short)
    #--------------------------------
    if but:
        short = shortner.tinyurl.short(url)
        st.write("\n\n")
        st.markdown(f"<h3 style='text-align: center;'>SHORTED URL</h3>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{short}</h3>", unsafe_allow_html=True)
        st.button("Copy",on_click=copying)
elif option=="IMAGE EDITOR":
    st.sidebar.markdown("-----------")
    st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.sidebar.markdown("This is small web app used for edit image we can use if you want")
    st.markdown("<h1 style= 'text-align: center;'> Image Editor(KP MODEL) </h1>", unsafe_allow_html=True)
    st.write("---------------")
    image_1 = st.file_uploader("Upload your File", type=["png", "jpg", "jpng"])
    st_lottie(loettir_2)

    if image_1:
        #------------------------------------
        but = st.checkbox("See Origanl-Image")
        st.write("\n\n")
        info = st.empty()
        size = st.empty()
        format = st.empty()
        model = st.empty()
        if but:
            st.image(image_1)
        #----------------------------------
        img = Image.open(image_1)
        info.markdown("<h2 style= 'text-align: center;'> Information </h2>", unsafe_allow_html=True)
        size.markdown(f"<h6>Size: {img.size}</h6>",unsafe_allow_html=True)
        format.markdown(f"<h6>Format: {img.format}</h6>",unsafe_allow_html=True)
        model.markdown(f"<h6>Model: {img.mode}</h6>",unsafe_allow_html=True)
        #-----------------------------------------------
        st.markdown("<h2 style= 'text-align: center;'> Resizing </h2>", unsafe_allow_html=True)
        width = st.number_input("Width", value=img.width)
        height = st.number_input("Height", value=img.height)
        #----------------------------------------------
        st.markdown("<h2 style= 'text-align: center;'> Rotation </h2>", unsafe_allow_html=True)
        degree = st.number_input("Degree")
        #-------------------------------------------------------
        st.markdown("<h2 style= 'text-align: center;'> Filter </h2>", unsafe_allow_html=True)
        selectnox = st.selectbox("Filters", options=("None", "Blur", "Detail", "Emboss","Smooth"))
        #------------------------------------------------------
        st.write("\n\n\n\n")
        st.write("\n\n")
        st.write("\n\n")
        st.write("\n\n")
        s_but = st.button("Submit")
        if s_but:
            edte = img.resize((width, height)).rotate(degree)
            if filter == "None":
                st.image(edte)
            elif filter == "Blur":
                a = edte.filter(BLUR)
                st.image(a)
            elif filter=="Detail":
                a = edte.filter(DETAIL)
                st.image(a)
            elif filter=="Emboss":
                a= edte.filter(EMBOSS)
                st.image(a)
            else:
                a= edte.filter(SMOOTH)
                st.image(a)
elif option=="WORD DENSITY CHECKER":
    st.sidebar.markdown("-----------")
    st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.sidebar.markdown("This is small web app used for to check density of word in your paragraph")
    st.markdown("<h1 style='text-align: center;'>Keyword Density Checkwer(KP MODEL)</h1>", unsafe_allow_html=True)
    st.markdown("--------",unsafe_allow_html=True)
    #----------------------------------------------------
    text = st.text_area("PASTE HERE YOUR PARAGRAPH")
    but = st.button("Check")
    st_lottie(loettir_3)
    col_1, col_2, col_3 = st.columns(3)
    word_dict = dict()
    if but:
    #-----------------------------------------------------
        col_1.markdown(f"<h3> Keywords</h3>", unsafe_allow_html=True)
        col_2.markdown(f"<h3> Density</h3>", unsafe_allow_html=True)
        col_3.markdown(f"<h3> Percentage</h3>", unsafe_allow_html=True)
        sim_text = re.sub("[.?!&;:*@,]", "", text)
        words = sim_text.lower().split(" ")
        t_len = len(words)
        for word in words:
            if word in word_dict:
                word_dict[word]=word_dict[word]+1
            else:
                word_dict[word]=1
        print(word_dict)
        keys = list(word_dict.keys())
        values = list(word_dict.values())
        for i in range(len(keys)):
            col_1.markdown(f"<h5>{keys[i]}</h5>", unsafe_allow_html=True)
            col_2.markdown(f"<h5>{values[i]}</h5>", unsafe_allow_html=True)
            col_3.markdown(f"<h5>{round(values[i]/(t_len)*100)}</h5>", unsafe_allow_html=True)

else:
    st.sidebar.markdown("-----------")
    st.sidebar.markdown(f"<h3 style='text-align: center;'>{option}</h3>",unsafe_allow_html=True)
    st.sidebar.markdown("This is small app used for to convert audio file into text")
    reco = sr.Recognizer()
    final_result = ""
    #--------------------------------------------
    st.markdown("<h1 style='text-align: center;'>Audio to Text Converter(KP MODEL)</h1>", unsafe_allow_html=True)
    st.markdown("--------",unsafe_allow_html=True)
    #------------------------------------------------------
    audio = st.file_uploader("Upload Your File", type=["mp3","wav"])
    st_lottie(loettir_4)
    if audio:
        st.audio(audio)
        audio_segment = AudioSegment.from_file(audio)#convert into audio segment 
        chunks=silence.split_on_silence(audio_segment, min_silence_len=500, silence_thresh=audio_segment.dBFS-20, keep_silence=100)
        for index,chu in enumerate(chunks):
            chu.export(str(index)+".wav", format="wav")
            with sr.AudioFile(str(index)+".wav") as source:
                recorded = reco.record(source)
                try:
                   text = reco.recognize_google(recorded)
                   st.write(text)
                   final = final_result+" " +text
                except:
                    a= "we not able to convert your audio"
                    final = final_result+" "+ a
        st.text_area("", value=final)
    #-----------------------------------------------------






