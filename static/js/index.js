setTimeout(function () {
    let messages = document.getElementById('messages');
    if (messages) {
        let alert = new bootstrap.Alert(messages);
        alert.close();
    }
}, 2500);