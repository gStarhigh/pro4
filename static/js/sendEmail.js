function sendMail(LessonBookingForm) {
    const username = document.querySelector('p[data-username]').getAttribute('data-username');
    const email = document.querySelector('p[data-email]').getAttribute('data-email');
    const lessonDate = document.querySelector('[name="lesson_date"]').value;
    const lessonTime = document.querySelector('[name="lesson_time"]').value;
    const noParticipants = document.querySelector('[name="no_participants"]').value;
    const focus = document.querySelector('[name="focus_lesson"]').value;
    const serviceID = "service_bp6z8w3";
    const templateID = "booking_created";
    const templateParams = {
        "from_name": username,
        "from_email": email,
        "lesson_date": lessonDate,
        "lesson_time": lessonTime,
        "no_participants": noParticipants,
        "focus_lesson": focus,
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