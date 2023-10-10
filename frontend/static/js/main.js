document.addEventListener('DOMContentLoaded', () => {
    const uploadForm = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const resultsDiv = document.getElementById('results');

    uploadForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData();
        formData.append('image', fileInput.files[0]);

        try {
            // Send a POST request to the backend API
            const response = await fetch('/api/uploadimage/', {
                method: 'POST',
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();
                displayColorResults(data);
            } else {
                resultsDiv.textContent = 'Error: ' + response.statusText;
            }
        } catch (error) {
            console.error('Error:', error);
            resultsDiv.textContent = 'An error occurred. Please try again.';
        }
    });

    // Function to display color identification results
    function displayColorResults(results) {
        resultsDiv.innerHTML = '<h2>Color Identification Results:</h2>';
        const colorList = document.createElement('ul');

        for (const color in results) {
            const rgb = results[color];
            const listItem = document.createElement('li');
            listItem.innerHTML = `<strong>${color}:</strong> RGB(${rgb.join(', ')})`;
            colorList.appendChild(listItem);
        }

        resultsDiv.appendChild(colorList);
    }
});
