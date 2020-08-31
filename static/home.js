var body=document.querySelector("body");
var heading=document.querySelector(".heading");
var btn=document.querySelector(".mybtn");

function myfunction()
{
    body.classList.add("top-later");
    body.classList.remove("top");
    heading.classList.replace("heading","heading2");
    btn.classList.replace("mybtn","mybtn2");
}

