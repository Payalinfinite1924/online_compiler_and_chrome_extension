document.getElementById('runCode').addEventListener('click', function() {
    const code = document.getElementById('code').value;
    const language = document.getElementById('language').value;

    // Prepare data to send to the Flask server
    const data = new FormData();
    data.append('code', code);
    data.append('language', language);

    // Send the code to the Flask server
    fetch('https://payalvpn10.pythonanywhere.com/run_code', {
        method: 'POST',
        body: data
    })
    .then(response => response.json())
    .then(data => {
        const outputDiv = document.getElementById('output');
        if (data.error) {
            outputDiv.style.color = 'red';
            outputDiv.textContent = 'Error: ' + data.error;
        } else {
            outputDiv.style.color = 'green';
            outputDiv.textContent = 'Output: \n' + data.output;
        }
    })
    .catch(error => {
        const outputDiv = document.getElementById('output');
        outputDiv.style.color = 'red';
        outputDiv.textContent = 'Failed to connect to the server!';
    });
});
