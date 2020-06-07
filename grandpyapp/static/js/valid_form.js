
let form = document.getElementById('form-query');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            let response = JSON.parse(this.responseText);
            console.log(response[0]);
            displaysElements(document.getElementById("query-text-form").value,
                response[0])

        }
    };
    request.open("POST", "query");
    request.send(new FormData(form));
});


