/****************
 * Declarations
 ****************/

let eltQuery = document.getElementById("query-1");
let eltResponse = document.getElementById("response-1");

let eltDivMap = document.getElementById("div-map");
let eltMap = document.getElementById("google-map");

function getCount() {
    let count = document.getElementById('count').value;
    return parseInt(count);
}

/****************************************************************** 
* Displays the elements corresponding to the questions and answers
*******************************************************************/
function displaysElements(textQuery, textResponse, wikilink) {
    /* Add or display question and answer elements
       If first question, makes the elements visible otherwise, copies and displays them
    */
    count = getCount();

    eltDivMap.classList.add('d-none');

    if (count == 0) {
        eltQuery.classList.remove("d-none");
        eltResponse.classList.remove("d-none");
        eltQueryNew = eltQuery;
        eltResponseNew = eltResponse;
    }
    else {
        eltQueryNew = eltQuery.cloneNode(true);
        eltQueryNew.id = "query-" + (count + 1);

        document.getElementById("query_response_multi").appendChild(eltQueryNew);

        eltResponseNew = eltResponse.cloneNode(true);
        eltResponseNew.id = "response-" + (count + 1);

        document.getElementById("query_response_multi").appendChild(eltResponseNew);
    }

    eltQueryNew.querySelector(".query-text-display").innerHTML = "<strong>" + textQuery + "</strong>";

    textResponse = formatResponse(textResponse);
    eltResponseNew.querySelector(".response-text-display").innerHTML = textResponse + '<br>';
    if (wikilink != "#") {
        eltResponseNew.querySelector(".response-text-display").appendChild(getWikiLink(wikilink));
    }
    document.getElementById('count').value = count + 1;
    document.getElementById('query-text-form').value = "";

    eltResponseNew.scrollIntoView(true);
    document.getElementById('query-text-form').focus();
}

function getWikiLink(wikilink) {
    /*Create element link to wikipedia */
    let aWiki = document.createElement('a');
    let aContent = document.createTextNode('Voir plus ici...');
    aWiki.appendChild(aContent);
    aWiki.setAttribute('href', wikilink);
    aWiki.setAttribute('target', '_blank');
    return aWiki;
}

function formatResponse(textResponse) {
    /* Format response
    delete == or === and replace by <br> */
    text = textResponse.replace(/===/g, '<br>');
    text = textResponse.replace(/=/g, '--');
    return text;
}

/*******************************
* display and update Google Map
********************************/

function displayMap(lat, lng) {

    map = new google.maps.Map(eltMap, {
        center: new google.maps.LatLng(lat, lng),
        zoom: 15,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: true,
        scrollwheel: true,
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.HORIZONTAL_BAR
        },
        navigationControl: true,
        navigationControlOptions: {
            style: google.maps.NavigationControlStyle.ZOOM_PAN
        }
    });

    //displays Marker
    var marker = new google.maps.Marker({
        position: { lat: lat, lng: lng },
        map: map
    });

    eltDivMap.classList.remove('d-none');

}
