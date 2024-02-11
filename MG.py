import streamlit as st
from altair import Chartf
from requests import post
from pydub import AudioSegment
from io import BytesIO

def Musicgeneration():

    b = post (
    "https://api-inference.huggingface.co/models/facebook/musicgen-small",
    headers = {
    'Authorization': 'Bearer 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'
    },

    json = {
        "inputs" : "Beautiful piano music for weddings"
    }

)

    i = AudioSegment.from_file(BytesIO(b.content))
    
    i.export("0.mp4", format="mp4")
    return i


def main():
    st.audio(Musicgeneration)


if __name__ == "__main__":
    main()
