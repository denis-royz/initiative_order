function refresh_ui_authorization(){
    document.getElementById("nav-sign-out").style.display = "none";
}

$(document).ready(function() {
    refresh_ui_authorization();
    $("ul").removeClass("lazy");
});