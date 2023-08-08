const apiKey = document.getElementById("map").getAttribute("data-api-key");

function initMap() {
    const location = {
        lat: 56.20593888061705,
        lng: 13.0081107977851
    };

    let map = new google.maps.Map(document.getElementById("map"), {
        center: location,
        zoom: 8,
        apiKey: apiKey
    });

    let marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "Starhög Equestrian"
    });
}