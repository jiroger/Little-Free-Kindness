$(document).ready(function() {
  if (document.URL.includes("about")) {
    document.querySelector(".navbar-nav a:nth-child(1)").classList.add("active");
  } else if (document.URL.includes("view")) {
    document.querySelector(".navbar-nav a:nth-child(2)").classList.add("active");
  } else if (document.URL.includes("rankings")) {
    document.querySelector(".navbar-nav a:nth-child(3)").classList.add("active");
  } else if (document.URL.includes("smile")) {
    document.querySelector(".navbar-nav a:nth-child(4)").classList.add("active");
  }
})

if ($("#ip").length > 0) {
  $.getJSON('http://www.geoplugin.net/json.gp?jsoncallback=?', function(data) {
    $("#ip").html(data["geoplugin_request"]);
    $("#submit").click(function (e) {
      e.preventDefault();
      $.ajax({
        type : "POST",
        url : "report",
        data: JSON.stringify({ "ip" : data["geoplugin_request"] } ),
        contentType: "application/json; charset=utf-8",
        dataType: "json"
      });
    });
  });
};
