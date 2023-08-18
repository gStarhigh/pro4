// Renders Google Maps through an API to the About page.
const apiKey = document.getElementById("map").getAttribute("data-api-key");

// Sets the location for the map.
function initMap() {
    const location = {
        lat: 56.20593888061705,
        lng: 13.0081107977851
    };
    // Centers the map and decides the zoom.
    let map = new google.maps.Map(document.getElementById("map"), {
        center: location,
        zoom: 8,
        apiKey: apiKey
    });
    // Puts the marker on the map.
    let marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "Starhög Equestrian"
    });
}