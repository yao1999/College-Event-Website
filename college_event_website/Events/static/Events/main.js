// adjust map to current view on click
$('.adjust_map').on('click', adjust_map);

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