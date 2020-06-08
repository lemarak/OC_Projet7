
let form = document.getElementById('form-query');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    myFormData = new FormData(form);
    if (myFormData.get('query-text-form') == "") {
        return 0;
    }
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            displaysElements(document.getElementById("query-text-form").value,
                response[0]+'<br>'+response[1]) //provisoire
        }
    };
    request.open("POST", "query");
    request.send(myFormData);
});


