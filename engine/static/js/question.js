function answer(selected) {
    for(let i = 0; i < 3; i++) {
        document.getElementById(getSelected(i)).onclick = null;
        document.getElementById(getSelected(i)).style.backgroundColor = '#00a6ff';
    }

    document.getElementById(getSelected(selected)).style.backgroundColor = 'red';
    document.getElementById(getSelected(correctAnswer)).style.backgroundColor = 'green';
}

function getSelected(number) {
    switch(number) {
        case 0:
            return "a";
        case 1:
            return "b";
        case 2:
            return "c";
    }
}

function nextQuestion() {
    window.location.href = '/question/category/' + localStorage.getItem("selectedCategory");
}

function loadMedia() {
    if(getFileType(media).split("/")[0] == "image") {
        document.getElementById("media").innerHTML = '<img src="' + media + '">'
    } 
    else if (getFileType(media).split("/")[0] == "audio") {
        console.log("audio")
    }
    else if (getFileType(media).split("/")[0] == "video") {
        document.getElementById("media").innerHTML = '<video controls><source src="' + media + '" type="' + getFileType(media) + '"></video>'
    }
}

function getFileType(fileName) {
    const extensionToTypeMap = {
        // Common image file types
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'bmp': 'image/bmp',
        'webp': 'image/webp',
        
        // Common audio file types
        'mp3': 'audio/mpeg',
        'wav': 'audio/wav',
        'ogg': 'audio/ogg',
        
        // Common video file types
        'mp4': 'video/mp4',
        'avi': 'video/x-msvideo',
        'mov': 'video/quicktime',
        'wmv': 'video/x-ms-wmv',
    };

    // Extract file extension
    const extension = fileName.split('.').pop().toLowerCase();
    
    // Get file type from map
    return extensionToTypeMap[extension] || 'unknown';
}
