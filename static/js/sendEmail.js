function sendMail(LessonBookingForm) {
    const username = document.querySelector('p[data-username]').getAttribute('data-username');
    const email = document.querySelector('p[data-email]').getAttribute('data-email');
    const focusLesson = document.querySelector('[name="focus_lesson"]').value;
    const serviceID = "service_bp6z8w3";
    const templateID = "booking_created";
    const templateParams = {
        "from_name": username,
        "from_email": email,
        "booking_info": focusLesson,

    }

    emailjs.send(serviceID, templateID, templateParams)
        .then(
            function (response) {
                console.log("SUCCESS", response);
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false;
}