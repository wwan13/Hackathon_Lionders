$('.signupbox__textbox input').on({
  focus: function () {
    $(this).addClass('focus');
  },
  blur: function () {
    if ($(this).val() == '') {
      $(this).removeClass('focus');
    }
  },
});

$('.text__address_num input').on({
  focus: function () {
    $(this).addClass('focus');
  },
  blur: function () {
    if ($(this).val() == '') {
      $(this).removeClass('focus');
    }
  },
  change: function () {
    // console.log($(this).val());
    // 여기서 값 바뀌는게 감지가 안되는 중
  },
});
