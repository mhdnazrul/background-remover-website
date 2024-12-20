async function uploadImage() {
  const fileInput = document.getElementById('imageUpload');
  const file = fileInput.files[0];

  if (!file) {
    alert('Please select an image file.');
    return;
  }

  const formData = new FormData();
  formData.append('image', file);

  try {
    const response = await fetch('/upload', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error('Failed to upload image.');
    }

    const data = await response.blob();
    const imageUrl = URL.createObjectURL(data);

    const outputImage = document.getElementById('outputImage');
    outputImage.src = imageUrl;
  } catch (error) {
    console.error(error);
    alert('Error removing background: ' + error.message);
  }
}
