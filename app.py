import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

length_options= ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Post Generator")
    col1, col2, col3 = st.columns(3)
    fs = FewShotPosts()
    tags = fs.get_tags()
    with (col1):
        # Add "Others" option
        tag_options = list(tags)
        # tag_options+= ["Others"]
        selected_tag = st.selectbox("Title", options=tag_options)

        # Show text input if Others is selected
        if selected_tag == "Others":
            custom_tag = st.text_input("Enter your topic")
            final_tag = custom_tag.strip() if custom_tag else None
        else:
            final_tag = selected_tag
        # selected_tags = st.selectbox("Title", options=fs.get_tags())
    with col2:
        selected_length = st.selectbox("Length", options=length_options)
    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    if st.button("Generate"):
        post = generate_post(selected_length, selected_language, selected_tag)
        st.write(post)
if __name__=="__main__":
    main()

