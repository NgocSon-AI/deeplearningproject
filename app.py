import streamlit as st

import os
import torch
from torchvision.transforms import transforms
from PIL import Image
from pathlib import Path


def save_image(uploaded_file):
    if uploaded_file is not None:
        save_path = os.path.join("images", "input.jpeg")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"Image save to {save_path}")

        model = torch.load(Path('model/model.pt'))
        model.eval()
        trans = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
        ])

        image = Image.open(Path('images/input.jpeg'))
        input_tensor = trans(image)
        input_tensor = input.view(1, 1, 224, 224).repeat(1, 3, 1, 1)
        with torch.no_grad():  # Tắt gradient để tiết kiệm bộ nhớ
            output = model(input_tensor)
        output = model(input)
        prediction = int(torch.max(output.data, 1)[1].numpy())
        print(prediction)

        if (prediction == 0):
            print("Normal")
            st.text_area(label="Prediction: ", value = "Normal", height=100)

        if (prediction == 1):
            print("Pneumonia")
            st.text_area(label="Prediction: ", value = "Pneumonia", height=100)

if __name__ == '__main__':
    st.title("Xray Classifier")
    uploaded_file = st.file_uploader(label="Upload an image", type=["jpg", "jepg", "png"], accept_multiple_files = False, key ="image_uploader")
    save_image(uploaded_file)