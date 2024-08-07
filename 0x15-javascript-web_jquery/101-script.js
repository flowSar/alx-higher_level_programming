
$(function () {
  const listElemtn = $('UL.my_list');
  $('DIV#add_item').click(function () {
    listElemtn.append('<li>Item</li>');
  });

  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });

  $('DIV#clear_list').click(function () {
    listElemtn.empty();
  });
});
