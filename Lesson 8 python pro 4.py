import streamlit as st

with st.sidebar:
    image = 'alan.jfif'
    st.image(image, caption='Alan Walker')
    st.write('Họ và tên: Alan Olav Walker')
    st.write('Nghệ danh: Alan Walker')
    st.write('Alan Walker là một nhà sản xuất nhạc điện tử và DJ người Na Uy – Anh, nổi tiếng với những bản hit như "Faded" và được biết đến với phong cách bí ẩn, luôn đeo mặt nạ khi biểu diễn.')

st.title('Bài hát yêu thích')
st.write('Alone')
audio = open('Alan Walker - Alone (Lyrics).mp3)
st.audio(audio, format='audio/mp3')

st.title('MV yêu thích')
st.write('Alone')
video = 'https://www.youtube.com/watch?v=bPs0xFd4skY&list=RDbPs0xFd4skY&start_radio=1'
st.video(video, format='video/mp4')
