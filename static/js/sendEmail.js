// Function for sending email from when a lesson is booked.
function sendMail() {
    const username = document.querySelector('p[data-username]').getAttribute('data-username');
    const email = document.querySelector('p[data-email]').getAttribute('data-email');
    const lessonDate = document.querySelector('[name="lesson_date"]').value;
    const lessonTime = document.querySelector('[name="lesson_time"]').value;
    const noParticipants = document.querySelector('[name="no_participants"]').value;
    const focus = document.querySelector('[name="focus_lesson"]').value;
    const termsChecked = document.querySelector('[name="terms_checked"]').checked;
    const serviceID = "service_bp6z8w3";
    const templateID = "booking_created";
    const templateParams = {
        "from_name": username,
        "from_email": email,
        "lesson_date": lessonDate,
        "lesson_time": lessonTime,
        "no_participants": noParticipants,
        "focus_lesson": focus,
    };

    // Lesson date validation
    const bookingDate = new Date(lessonDate);
    const dayOfWeek = bookingDate.getDay(); // 0 = Sunday, 1, 6 = Saturday

    // Terms checked validation
    if (!termsChecked) {
        alert("Please check the terms and conditions before submitting.");
        return false; // Stop form submission
    } else if (dayOfWeek === 0 || dayOfWeek === 6) {
        // LessonDate is a Saturday or Sunday
        console.log("Not Sending email...");
        return false; // Stop form submission
    } else {
        // LessonDate is not a Saturday or Sunday
        emailjs.send(serviceID, templateID, templateParams);
        console.log("Sending email...");
    }
}

// Function for sending email from the contact form.
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
    };
    emailjs.send(serviceID, templateID, templateParams);
}