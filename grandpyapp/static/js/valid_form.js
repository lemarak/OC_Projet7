
let form = document.getElementById('form-query');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    myFormData = new FormData(form);
    if (myFormData.get('query-text-form') == "") {
        return 0;
    }

    displayLoader(true); // loader on

    fetch("/query",
        {
            method: "POST",
            body: myFormData
        })
        .then(response => { return response.json() })
        .then(responseJson => {
            console.log(responseJson)
            displaysElements(document.getElementById("query-text-form").value,
                responseJson['response_wiki']['response_grandpy'], // title
                responseJson['response_wiki']['content_page'], // text to diplays in response
                responseJson['response_wiki']['url_link_wiki']); // wikipedia link
            let lat = responseJson['response_google']['lat'];
            let lng = responseJson['response_google']['lng'];
            if ( responseJson['response_google']['place_id'] != 0) {
                displayMap(lat, lng);
            }
            displayLoader(false); // loader off
        })


    

});

function displayLoader(display) {
    let eltDisplay = document.querySelector('#loader-query')
    if (display) {
        eltDisplay.classList.remove("d-none");
    } else {
        eltDisplay.classList.add("d-none");
    }
}
