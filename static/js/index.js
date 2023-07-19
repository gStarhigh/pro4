document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        select: function (info) {

            var start = info.startStr;
            var selectedDate = start;
            var selectedTime = '18:00';

            document.getElementById('lessonDate').value = selectedDate;
            document.getElementById('lessonTime').value = selectedTime;

            $('#bookingModal').modal('show');
        }
    });
    calendar.render();


    document.getElementById('bookLessonBtn').addEventListener('click', function () {

        var focusLesson = document.getElementById('focusLesson').value;
        var numberOfParticipants = document.getElementById('numberOfParticipants').value;
        var levelEkipage = document.getElementById('levelEkipage').value;

        var bookingData = {
            'selectedDate': document.getElementById('lessonDate').value,
            'selectedTime': document.getElementById('lessonTime').value,
            'focusLesson': focusLesson,
            'numberOfParticipants': numberOfParticipants,
            'levelEkipage': levelEkipage

        };
    });
});