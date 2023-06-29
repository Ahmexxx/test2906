import streamlit as st
import requests
import json
from PIL import Image



def main():
    st.title("API Frontend DI AHMED - POST-GET Debugger")
    url_API =st.text_input("inserisci url dell'api","http://localhost:8000/predict")
    rdspend = st.number_input("Inserisci rdspend")
    administration = st.number_input("Inserisci administration")
    marketing = st.number_input("Inserisci marketing")


    ###GET REQUEST###
    image = Image.open('r2.jpg')

    if st.button("Predict with GET"):
        url = url_API
        url2 = f"?rdspend={rdspend}&administration={administration}&marketing={marketing}"
        link = url+url2
        st.write('"{}"'.format(link))
        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result['result']}")
        st.image(image, caption='RICCIO SU TELA')
        st.balloons()


###POST REQUEST###

    if st.button("Predict with POST"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "rdspend":rdspend,
                                                   "administration":administration,
                                                   "marketing":marketing,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result['result']}")
        st.image(image, caption='RICCIO SU TELA')
        st.balloons()
   

if __name__ == '__main__':
    main()