function getCount() {
    let count = document.getElementById('count').value;
    return parseInt(count);
}


function displaysElements(textQuery, textResponse) {
    // Add or display question and answer elements
    // If first question, makes the elements visible otherwise, copies and displays them
    count = getCount();
    eltQuery = document.getElementById("query-1");
    eltResponse = document.getElementById("response-1");

    if (count == 0) {
        eltQuery.classList.remove("d-none");
        eltResponse.classList.remove("d-none");
        eltQueryNew = eltQuery;
        eltResponseNew = eltResponse
    }
    else {
        eltQueryNew = eltQuery.cloneNode(true);
        eltQueryNew.id = "query-" + (count + 1);

        document.getElementById("query_response_multi").appendChild(eltQueryNew);

        eltResponseNew = eltResponse.cloneNode(true);
        eltResponseNew.id = "response-" + (count + 1);

        document.getElementById("query_response_multi").appendChild(eltResponseNew);
    }

    eltQueryNew.querySelector(".query-text-display").innerHTML = "<strong>" + textQuery + "</strong>"
    eltResponseNew.querySelector(".response-text-display").innerHTML = "<strong>" + textResponse + "</strong>"

    document.getElementById('count').value = count + 1;
    document.getElementById('query-text-form').value = "";
}
