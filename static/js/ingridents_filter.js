$(document).ready(function(){
  $("#filetr-by-name").on("keyup", function() {
    const value = $(this).val().toLowerCase();
    $("#items-display-table *").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});