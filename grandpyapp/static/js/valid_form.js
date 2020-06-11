
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
            displaysElements(document.getElementById("query-text-form").value,
                responseJson[2][0],
                responseJson[2][1]); //provisoire
            let lat = responseJson[1][1];
            let lng = responseJson[1][2];
            displayMap(lat, lng);
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


