
$(document).ready(function() {
    if (document.URL.includes("about")) {
      document.querySelector(".navbar-nav a:nth-child(1)").classList.add("active");
    }
    else if (document.URL.includes("view")) {
      document.querySelector(".navbar-nav a:nth-child(2)").classList.add("active");
    }
    else if (document.URL.includes("rankings")) {
      document.querySelector(".navbar-nav a:nth-child(3)").classList.add("active");
    }
    else if (document.URL.includes("smile")) {
      document.querySelector(".navbar-nav a:nth-child(4)").classList.add("active");
    }
  }
)
