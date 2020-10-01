$(".loginbox__textbox input").on("focus", function () {
    $(this).addClass("focus");
});

$(".loginbox__textbox input").on("blur", function () {
    if ($(this).val() == "")
        $(this).removeClass("focus");
});