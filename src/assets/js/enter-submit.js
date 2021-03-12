document.getElementById('name')
    .addEventListener('keyup', function(event) {
        if (event.code === 'Enter') {
            event.preventDefault();
            document.querySelector('form').submit();
        }
    }
);