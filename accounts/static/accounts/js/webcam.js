const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const faceDataInput = document.getElementById('face_data');

// Access webcam
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing webcam: ", err);
        alert("Could not access the webcam. Please allow access and try again.");
    });

// Capture function
function capture() {
    const context = canvas.getContext('2d');
    canvas.style.display = 'block';
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageDataURL = canvas.toDataURL('image/jpeg');
    faceDataInput.value = imageDataURL;
}
