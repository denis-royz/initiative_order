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

function callNext() {
    $.get( "/api/v1/actors/end_of_turn", function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);
    });
}


function newChampion() {
    let name = document.getElementById("input_new_champion_name").value;
    let value = document.getElementById("input_new_champion_init").value;
    $.get( "/api/v1/actors/new?name={0}&value={1}".format(name, value), function( data ) {
         //As soon as the browser finished downloading, this function is called.
         $('#actors').html(data);

    });
}

function selectChampion() {
}