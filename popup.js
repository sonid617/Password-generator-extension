document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('generate').addEventListener('click', function () {
      generatePassword();
    });
  
    document.getElementById('auto-fill').addEventListener('click', function () {
      autoFillPassword();
    });
  });
  
  function generatePassword() {
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+';
    var password = '';
  
    for (var i = 0; i < 12; i++) {
      var randomIndex = Math.floor(Math.random() * characters.length);
      password += characters.charAt(randomIndex);
    }
  
    document.getElementById('password').value = password;
  }
  
  function autoFillPassword() {
    generatePassword(); // Generate a new password
  
    // Get the active tab
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      // Inject a content script to fill the password into the first password input field found on the page
      chrome.tabs.executeScript(tabs[0].id, {
        code: `
          var passwordInput = document.querySelector('input[type="password"]');
          if (passwordInput) {
            passwordInput.value = "${document.getElementById('password').value}";
          }
        `,
      });
    });
  }
  