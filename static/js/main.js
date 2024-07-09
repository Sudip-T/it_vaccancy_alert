
document.getElementById('job-container').addEventListener('click', function () {
    console.log('taking screenshot...')
    var jobID = this.getAttribute('data-job-id');
    var url = '/job/take_screenshot/' + jobID + '/';
    var formData = new FormData();
    formData.append('job_id', jobID);
    fetch(url, {
        method: 'GET',
    }).then(response => {
        if (response.ok) {
            return response.text();
        } else {
            throw new Error('Network response was not ok.');
        }
    }).then(data => {
        console.log(data);
    }).catch(error => {
        console.error('Error requesting screenshot:', error);
    });
});

window.onload = function () {
    const contentDiv = document.querySelector('.content');
    const bgImage = new Image();
    bgImage.src = '/static/img/hiring_email.png';

    bgImage.onload = function () {
        contentDiv.style.width = `${bgImage.width}px`;
        contentDiv.style.height = `${bgImage.height}px`;
    };
};

