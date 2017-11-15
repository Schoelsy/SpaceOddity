

/*
$(function(){

    $("#send_button").click(function(){
        $("#myModal").modal("hide");
    });

    $("#myModal").on("hidden.bs.modal", function(){
        alert("OK");
    });
});
*/
function closeFunction(){
    $("#modal_alert").modal("hide");
}
function myFunction() {
    setTimeout(function(){
        $("#modal_alert").modal("hide");
    }, 500);

}