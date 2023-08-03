function sendMail() {
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
}

function SendContactMail() {
    const name = document.querySelector('[name="name"]').value;
    const email = document.querySelector('[name="email"]').value;
    const subject = document.querySelector('[name="subject"]').value;
    const message = document.querySelector('[name="message"]').value;

    const serviceID = "service_bp6z8w3";
    const templateID = "contact_form";
    const templateParams = {
        "from_name": name,
        "from_email": email,
        "subject": subject,
        "message": message,
    }
    emailjs.send(serviceID, templateID, templateParams)
}