// add email input on click
$('.add_email').on('click', add_email);

// function to add email input
function add_email() {
    // keeps track of number of emails via a number input
    var num_emails = parseInt($('#number_emails').val()) + 1;

    // add new email input to the new email area
    var new_email = "<div class=\"col-md-12\"><div class=\"d-flex w-100 justify-content-center\"><label class=\"sr-only\" for=\"rso_email_" + num_emails + "\">Add Member Email</label><div id=\"div_id_email\" class=\"form-group\"><input type=\"text\" placeholder=\"Member Email*\" name=\"rso_email_"+ num_emails + "\" id=\"rso_email_"+ num_emails + "\" class=\"text-center text-white textinput textInput form-control\" required></div></div></div>"
    $('#new_email').append(new_email);

    // increment counter in html
    $('#number_emails').val(num_emails);
}