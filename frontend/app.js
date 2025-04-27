// app.js for login.html
document.getElementById('loginForm')?.addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ username, password })
    });
  
    const data = await response.json();
    if (response.ok) {
        localStorage.setItem('token', data.access_token);
        localStorage.setItem('username', data.username);
        localStorage.setItem('role', data.role);
        localStorage.setItem('name', data.name);
        
    //   window.location.href = 'output.html';
    } else {
      alert('Login failed: ' + (data.detail || 'Unknown error'));
    }
  });
  