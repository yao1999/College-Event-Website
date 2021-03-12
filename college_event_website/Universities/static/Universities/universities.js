// add photo input on click
$('.add_photo').on('click', add_photo);

// function to add photo input
function add_photo() {
    // add new photo input to the new photo area
    var new_photo = "<div class=\d-flex w-100 justify-content-center\"><label class=\"sr-only\" for=\"university_photo\">Add University Photo</label><div id=\"div_id_picture\" class=\"form-group\"><input type=\"file\" name=\"picture\" id=\"university_photo_"+ num_photos + "\" accept=\"image/*\" class=\"fileinput fileUpload form-control-file\" required></div></div>"
    $('#new_photos').append(new_photo);

    // keeps track of number of photos via a number input
    var num_photos = parseInt($('#number_photos').val()) + 1;
    $('#number_photos').val(num_photos);
}