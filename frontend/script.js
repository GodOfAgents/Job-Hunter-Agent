document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('email', document.getElementById('email').value);
    formData.append('phone', document.getElementById('phone').value);
    formData.append('location', document.getElementById('location').value);
    formData.append('frequency', document.getElementById('frequency').value);
    formData.append('resume', document.getElementById('resume').files[0]);

    fetch('http://localhost:5000/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert('Application submitted successfully!');
        document.getElementById('myForm').reset();
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred while submitting the application.');
    });
});