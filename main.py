import streamlit as st 
from PIL import Image
import style

st.title('Pytorch Style Transfer')

input_image = st.file_uploader("choose you image", type = ['png', 'jpg'])
#input_image = Image.open(input_image)

if input_image is None:
    st.sidebar.write('please use defacult image')
    

    img = st.sidebar.selectbox(
        'Select Default Image',
        ('amber.jpg', 'cat.jpg')
    )
    input_image = 'images/content-images/' + img

style_name = st.sidebar.selectbox(
    'Select style',
    ('candy', 'mosaic','udnie')
)



model = 'saved_models/' + style_name + '.pth'
output_image = 'images/output-images/' + style_name + '.jpg'


img = Image.open(input_image)
style_image = Image.open('images/style-images/' + style_name + '.jpg')



st.write("### Souce Image:")
st.image(img, width=400)
st.write("---")
st.write("### Style Image:")
st.image(style_image, width=400)



#st.write('This is the selected style image')
#st.image('images/style-images/'+style_name+'.jpg', width= 400)

clicked = st.button('stylize')
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write("### Stylized Image:")
    img = Image.open(output_image)
    st.image(img, width = 400)







