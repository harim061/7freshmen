function Share() {
  var share_button = document.getElementById("share");
  share_button.style.visibility = "hidden";
  share_button.style.display = "none";
  var button_link = document.getElementById("button_link");

  var link = button_link.getElementsByClassName("inputbox");
  link.item(0).style.display = "block";
  link.item(0).style.visibility = "visible";

  var bubble = document.getElementsByClassName("chatBalloon").item(0);
  bubble.style.visibility = "hidden";
  // bubble.style.display="none";
}

function Copy() {
  const val = document.getElementById("link").textContent;
  const textArea = document.createElement("textarea");
  document.body.appendChild(textArea);
  textArea.value = val;
  textArea.select();
  document.execCommand("copy");
  document.body.removeChild(textArea);
}
