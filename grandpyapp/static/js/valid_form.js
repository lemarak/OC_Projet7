
let form = document.getElementById('form-query');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    myFormData = new FormData(form);
    if (myFormData.get('query-text-form') == "") {
        return 0;
    }

    displayLoader(true);

    fetch("/query",
        {
            method: "POST",
            body: myFormData
        })
        .then(response => { return response.json() })
        .then(responseJson => {
            console.log(responseJson);
            displaysElements(document.getElementById("query-text-form").value,
                responseJson[2][0], // title
                responseJson[2][1], // text to diplays in response
                responseJson[2][2]); // wikipedia link
            let lat = responseJson[1][1];
            let lng = responseJson[1][2];
            if (lng != 0 && lat != 0) {
                displayMap(lat, lng);
            }
            displayLoader(false);
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
