function refresh_ui_authorization(){
    document.getElementById("nav-sign-out").style.display = "none";
}

$(document).ready(function() {
    refresh_ui_authorization();
    $("ul").removeClass("lazy");
});

String.prototype.format = function() {
    var formatted = this;
    for( var arg in arguments ) {
        formatted = formatted.replace("{" + arg + "}", arguments[arg]);
    }
    return formatted;
};

var selected_champion_id = null

function callNext() {
    $.get( "/api/v1/actors/end_of_turn", function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);
    });
}

function selectChampion(actor_id) {
    document.getElementById("selected-actor").innerHTML = document.getElementById("btn-select-champion-"+actor_id).value
    document.getElementById("input_selected_champion_initiative").value = document.getElementById("btn-select-champion-"+actor_id).getElementsByTagName('span')[0].innerHTML
    selected_champion_id = actor_id
}

function newChampion() {
    let name = document.getElementById("input_new_champion_name").value;
    let value = document.getElementById("input_new_champion_init").value;
    $.get( "/api/v1/actors/new?name={0}&value={1}".format(name, value), function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);

    });
}

function callDelete() {
    let actor_id = selected_champion_id
    $.get( "/api/v1/delete?actor_id={0}".format(actor_id), function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);

    });
}

function updateSelectedActorsInitiative() {
    let actor_id = selected_champion_id
    let value = document.getElementById("input_selected_champion_initiative").value;
    $.get( "/api/v1/set_init?actor_id={0}&value={1}".format(actor_id, value), function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);

    });
}


function resetEverything() {
    $.get( "/api/v1/reset", function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);

    });
}