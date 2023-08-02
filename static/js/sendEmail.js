function sendMail(LessonBookingForm) {
    const serviceID = "service_bp6z8w3";
    const templateID = "booking_created";
    const username = "{{ user.username }}";
    const templateParams = {
        "from_name": username,
        "from_email": "{{user.email}}",
        "booking_info": "{{user.focus_lesson}}",

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