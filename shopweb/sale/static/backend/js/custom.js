document.addEventListener('DOMContentLoaded', function () {
    var toastElement = document.querySelector('.toast');
    var toast = new bootstrap.Toast(toastElement, {
        delay: 3000 // Duration before the toast hides
    });
    toast.show(); // Show the toast
});