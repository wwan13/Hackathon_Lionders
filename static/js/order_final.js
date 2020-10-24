$(document).ready(function () {
    $('#radioButton').click(function () {
        // getter
        var radioVal = $('input[name="lionders"]:checked').val();
        alert(radioVal);
    });
})