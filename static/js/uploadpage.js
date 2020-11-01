window.addEventListener('beforeunload', function () {
    return 'The upload will cancel if you leave the page, continue?';
});
window.addEventListener('load', function () {
    var req = new XMLHttpRequest();
    console.log(req)
    req.addEventListener('progress', function (evt) {
        var percentage = '' + (evt.loaded / evt.total * 100) + '%';
        // use percentage to update progress bar or something
    });
    req.addEventListener('load', function () {
        alert('Upload Finished');
        window.removeEventListener('beforeunload');
        window.close();
    });
    req.open('POST', '/upload/'+encodeURIComponent(window.file.name));
    req.send(window.file);
});