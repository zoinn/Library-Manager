document.querySelector('form').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.querySelector('#username').value;
    const password = document.querySelector('#password').value;

    fetch('/api/token/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.access) {
            localStorage.setItem('token', data.access);
            window.location.href = '/library/';
        } else {
            alert('Login failed');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Login failed');
    });
});