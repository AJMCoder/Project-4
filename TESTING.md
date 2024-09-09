## Manual Testing

### When user is *Not logged in*

#### Every link was tested to ensure that it redirects to the appropriate url and functions as intended.

<details><summary>Navbar</summary>
<img src="static/images/readme/testing/loggedout/navbar-not.png" >
</details>

<details><summary>Logo</summary>
<img src="static/images/readme/testing/loggedout/logo-not.jpg" >
</details>

<details><summary>Home page - When the user is logged out, you will see in the top right, a notification that states this.</summary>
<img src="static/images/readme/testing/loggedout/home-not.jpg" >
</details>

<details><summary>Contact Us Button</summary>
<img src="static/images/readme/testing/loggedout/contact-not.png" >
</details>

<details><summary>Events page</summary>
<img src="static/images/readme/testing/loggedout/events-not.png" >
</details>

<details><summary>Event detail page</summary>
<img src="static/images/readme/testing/loggedout/event-detail-not.png" >
</details>

<details><summary>Matches Page</summary>
<img src="static/images/readme/testing/loggedout/matches-not.png" >
</details>

<details><summary>Submit match result page</summary>
<img src="static/images/readme/testing/loggedout/submit-not.png" >
</details>

<details><summary>Rules page</summary>
<img src="static/images/readme/testing/loggedout/rules-not.png" >
</details>

<details><summary>Contact page</summary>
<img src="static/images/readme/testing/loggedout/contact-not.png" >
</details>

<details><summary>Registration page</summary>
<img src="static/images/readme/testing/loggedout/register-not.png" >
</details>

<details><summary>Login page</summary>
<img src="static/images/readme/testing/loggedout/login-not.png" >
</details>

#### Registration Page

Each instance of the registration page was tested to ensure the necessary warnings and signals were in place incase of the form being incomplete.

<details><summary>Registration with no information presented</summary>
<img src="static/images/readme/testing/loggedout/no-info.png" >
</details>

<details><summary>Registration with no password entered</summary>
<img src="static/images/readme/testing/loggedout/no-pass.png" >
</details>

<details><summary>Registration with no repeat password entered</summary>
<img src="static/images/readme/testing/loggedout/repeat-pass.png" >
</details>

<details><summary>Registration with incorrect/insufficiently completed password</summary>
<img src="static/images/readme/testing/loggedout/pass-format.png" >
</details>

<details><summary>Registration link to sign-in page</summary>
<img src="static/images/readme/testing/loggedout/signin-link.png" >
</details>

#### Login Page

The login page was tested to ensure that different scenarios where accommodated for.

<details><summary>Login page with incorrect username or password</summary>
<img src="static/images/readme/testing/loggedout/incorrect-pass-user.png" >
</details>

<details><summary>Login page with remembered user information</summary>
<img src="static/images/readme/testing/loggedout/remembered-user.png" >
</details>

<details><summary>Login page with link to registration page</summary>
<img src="static/images/readme/testing/loggedout/link-to-registration.png" >
</details>


### When user is *Logged in*

#### Every link was tested to ensure that it redirects to the appropriate url and functions as intended now that the user is logged in.

<details><summary>Navbar</summary>
<img src="static/images/readme/testing/loggedin/navbar.png" >
</details>

<details><summary>Home page - Now that the user is logged in, it tells them which account they are logged in with.</summary>
<img src="static/images/readme/testing/loggedin/home.jpg" >
</details>

<details><summary>Events page</summary>
<img src="static/images/readme/testing/loggedin/events/events.png" >
</details>

<details><summary>Event detail page</summary>
<img src="static/images/readme/testing/loggedin/events/event-details.png" >
</details>

<details><summary>Event creation page</summary>
<img src="static/images/readme/testing/loggedin/events/event-create.png" >
</details>

<details><summary>Event editting</summary>
<img src="static/images/readme/testing/loggedin/events/event-edit.png" >
</details>

<details><summary>Event deletion</summary>
<img src="static/images/readme/testing/loggedin/events/event-delete.png" >
</details>

<details><summary>Matches Page</summary>
<img src="static/images/readme/testing/loggedin/matches.png" >
</details>

<details><summary>Submit match result page</summary>
<img src="static/images/readme/testing/loggedin/match-submit.png" >
</details>

<details><summary>Submit match results with insufficient input</summary>
<img src="static/images/readme/testing/loggedin/match-submit-incomplete.png" >
</details>

<details><summary>Rules page</summary>
<img src="static/images/readme/testing/loggedin/rules.png" >
</details>

<details><summary>Contact page</summary>
<img src="static/images/readme/testing/loggedin/contact.png" >
</details>

<details><summary>Logout page</summary>
<img src="static/images/readme/testing/loggedin/logout.png" >
</details>

#### Event creation process

<details><summary>Test event: The event is being written to test the publishing capabilities of the website.</summary>
<img src="static/images/readme/testing/loggedin/events/test-event.png" >
</details>

<details><summary>Test event: Once created, the user is directed to the event details where they can change an details. However, if they leave this page, it cannot be editted until published fully on the site. This requires Admin approval.</summary>
<img src="static/images/readme/testing/loggedin/events/test-event-detail.png" >
</details>

<details><summary>Test event: Now that the event has been approved by an admin, it will appear on the events page.</summary>
<img src="static/images/readme/testing/loggedin/events/test-event-published.png" >
</details>


#### Footer Links

All footer links open their respective websites in a new tab.

<details><summary>Facebook</summary>
<img src="static/images/readme/testing/loggedout/facebook-not.png" >
</details>

<details><summary>Instagram</summary>
<img src="static/images/readme/testing/loggedout/instagram-not.png" >
</details>

<details><summary>X *Twitter*</summary>
<img src="static/images/readme/testing/loggedout/x-not.png" >
</details>


## Automated Testing

Django's automated testing is useful because it ensures the reliability and stability of applications by detecting bugs early in the development process. It helps prevent regressions when new features are added or code is refactored, providing developers with confidence in their changes. Automated testing speeds up the development cycle by reducing the need for manual testing and offers comprehensive coverage, from unit tests to end-to-end simulations.

### Event app testing

#### These tests in the EventTests class are verifying various functionalities related to event management in a Django application:

<details><summary>test_create_event: This test checks whether a new event can be successfully created via a POST request. It verifies that the response status is a redirect (302) and that the new event exists in the database.</summary>
<img src="static/images/readme/testing/automated/test-create.png" >
</details>

<details><summary>test_edit_event: This test ensures that an existing event can be updated. It sends a POST request to edit the event, then checks that the response is a redirect (302) and that the event's title is updated correctly in the database.</summary>
<img src="static/images/readme/testing/automated/test-edit.png" >
</details>

<details><summary>test_delete_event: This test verifies that an event can be deleted. It checks that after sending a POST request to delete the event, the event no longer exists in the database, and the response is a redirect (302).</summary>
<img src="static/images/readme/testing/automated/test-delete.png" >
</details>

<details><summary>test_events: This test confirms that the event listing page is accessible (returns a 200 status code) and contains the title of an event.</summary>
<img src="static/images/readme/testing/automated/test-event.png" >
</details>

<details><summary>test_event_detail: This test checks that the event detail page for a specific event can be accessed (200 status code) and that the page contains the event's title.</summary>
<img src="static/images/readme/testing/automated/test-event-detail.png" >
</details>

<details><summary>test terminal: This is the result of running the test through the command - *python manage.py test events*. As you can see, the system ran 5 tests, and 0 issues were found.</summary>
<img src="static/images/readme/testing/automated/test-outcome.png" >
</details>

Overall, these tests ensure that event creation, editing, deletion, listing, and detail view functionality work as expected.

### Conact form testing

#### These tests in the ContactFormTest class validate the functionality of the ContactForm:

<details><summary>test_contact_form_valid_data: This test checks that the contact form is valid when all required fields (first name, last name, email, and body) are provided with correct data.</summary>
<img src="static/images/readme/testing/automated/contact-valid.png" >
</details>

<details><summary>test_contact_form_invalid_data: This test ensures that the form is invalid when no data is provided. It verifies that the form has 4 errors, corresponding to the missing required fields.</summary>
<img src="static/images/readme/testing/automated/contact-invalid.png" >
</details>

<details><summary>test_contact_form_partial_data: This test verifies that the form is invalid when some required fields are missing. It specifically checks that the errors include lname (last name) and body when those fields are left empty.</summary>
<img src="static/images/readme/testing/automated/contact-required.png" >
</details>

<details><summary>test terminal: This is the result from running the command - *python manage.py test contact* in the terminal. As you can see, 3 tests were ran and 0 issues found.</summary>
<img src="static/images/readme/testing/automated/contact-outcome.png" >
</details>

Overall, these tests ensure that the contact form behaves correctly, validating both complete and incomplete data inputs.

## Validator Testing

### HTML files

The HTML files pass  through the ![W3C validator]()

<details><summary>Home</summary>
<img src="" >
</details>

<details><summary>Events</summary>
<img src="" >
</details>

<details><summary>Event detail</summary>
<img src="" >
</details>

<details><summary>Event create</summary>
<img src="" >
</details>

<details><summary>Matches</summary>
<img src="" >
</details>

<details><summary>Submit Matches</summary>
<img src="" >
</details>

<details><summary>Rules</summary>
<img src="" >
</details>

<details><summary>Contact</summary>
<img src="" >
</details>

<details><summary>Sign In</summary>
<img src="" >
</details>

<details><summary>Registration</summary>
<img src="" >
</details>

<details><summary>Sign Out</summary>
<img src="" >
</details>








<details><summary>#</summary>
<img src="" >
</details>