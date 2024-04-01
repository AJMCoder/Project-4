function sendMail(contactForm) {
    emailjs.send("gmail", "cityserve", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "league_enquiry": contactForm.subject.value,
        "message": contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            alert("Your email has been sent successfully!");
        },
        function(error) {
            console.log("FAILED", error);
            alert("Your email was not sent. Please try again later.");
        }
    );
    return false;  // To block from loading a new page
}