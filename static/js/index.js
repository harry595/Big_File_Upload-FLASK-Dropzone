// get value from <input id="upload" type="file"> on page
var upload = document.getElementById('upload');
upload.addEventListener('input', function () {
    // open new tab and stick the selected file in it
    var file = upload.files[0];
    console.log(file)
    var uploadTab = window.open('/upload-page', '_blank');
    if (uploadTab) {
        uploadTab.file = file;
    } else {
        alert('Failed to open new tab');
    }
});