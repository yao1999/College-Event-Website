// add photo input on click
$('.add_photo').on('click', add_photo);

// adjust map to current view on click
$('.adjust_map').on('click', adjust_map);

// function to add photo input
function add_photo() {
    // keeps track of number of photos via a number input
    var num_photos = parseInt($('#number_photos').val()) + 1;

    // add new photo input to the new photo area
    var new_photo = "<div class=\"d-flex w-100 justify-content-start\"><label class=\"sr-only\" for=\"university_photo_" + num_photos + "\">Add University Photo</label><div id=\"div_id_picture\" class=\"form-group\"><input type=\"file\" name=\"university_photo_"+ num_photos + "\" id=\"university_photo_"+ num_photos + "\" accept=\"image/*\" class=\"fileinput fileUpload form-control-file\" required></div></div>"
    $('#new_photos').append(new_photo);

    // increment counter in html
    $('#number_photos').val(num_photos);
}

// function to adjust map
function adjust_map() {
    // grab the latitude and longitude from the form
    var latitude = parseFloat($('#location_latitude').val());
    var longitude = parseFloat($('#location_longitude').val());

    // remove the old map
    $('#current_map').remove();

    // add the new map to map
    var new_map = "<iframe id=\"current_map\" src=\"https://maps.google.com/maps?q=" + latitude + "," + longitude + "&hl=es;z=14&amp;output=embed\" width=\"550\" height=\"300\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\"></iframe>";
    $('#map').append(new_map);
}