import langchain_helper as lch
import streamlit as st

st.title("Pet name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat","Dog",
                                   "Rabbit","Guinea Pig","Goat","Sheep","Hamster"))

if animal_type == "Cat":
    pet_color=st.sidebar.text_area("What color is your cat?", max_chars=15)
elif animal_type == "Dog":
    pet_color=st.sidebar.text_area("What color is your Dog?", max_chars=15)
elif animal_type == "Rabbit":
    pet_color=st.sidebar.text_area("What color is your Rabbit?", max_chars=15)
elif animal_type == "Guinea Pig":
    pet_color=st.sidebar.text_area("What color is your Guinea Pig?", max_chars=15)
elif animal_type == "Goat":
    pet_color=st.sidebar.text_area("What color is your Goat?", max_chars=15)
elif animal_type == "Sheep":
    pet_color=st.sidebar.text_area("What color is your Sheep?", max_chars=15)
else:
    pet_color=st.sidebar.text_area("What color is your Hamster?", max_chars=15)

if pet_color:
   response = lch.generate_pet_name(animal_type, pet_color)
   st.text(response["pet_name"])