var url = window.location.href;
var btn_actual = "ninguna";

switch(true) {
  case (url.indexOf("producto") != -1):
    btn_actual = document.getElementById("btn-producto");
    btn_actual.style.backgroundColor = "#b10450";
    break;

  case (url.indexOf("home") != -1):
    btn_actual = document.getElementById("btn-home");
    btn_actual.style.backgroundColor = "#b10450";
    break;

  case (url.indexOf("usuario") != -1):
    btn_actual = document.getElementById("btn-usuario");
    btn_actual.style.backgroundColor = "#b10450";
    break;
}

// console.log(btn_actual);
// console.log(url);