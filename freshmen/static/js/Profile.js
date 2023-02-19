function loadFile(input)
{
    var file=input.files[0];

    var newImage=document.createElement("img");
    newImage.setAttribute("class","img");

    newImage.src=URL.createObjectURL(file);

    newImage.style.width="130px";
    newImage.style.height="130px";
    newImage.style.borderRadius="50%";
    newImage.style.position="absolute"
    var button=document.getElementById("chooseFile_button");
    button.style.visibility="hidden";

    var container=document.getElementById("profile_background");
    container.appendChild(newImage);
}

function Save()
{
    console.log('hi')
    var input=document.getElementsByClassName('inputbox')
    for (var i=0;i<input.length;i++)
    {
        var item=input.item(i);
        item.readOnly=true;
    }
    var save_button=document.getElementById('save_button');
    if(save_button.innerText=='저장')
    {
        save_button.innerText='편집';
        var input=document.getElementsByClassName('inputbox')
        for (var i=0;i<input.length;i++)
        {
            var item=input.item(i);
            item.readOnly=true;
        }
        var share_button=document.getElementById("share_button");
        share_button.style.visibility='visible'

    }
    else{
        save_button.innerText='저장';
        var input=document.getElementsByClassName('inputbox')
        for (var i=0;i<input.length;i++)
        {
            var item=input.item(i);
            item.readOnly=false;
        }
        var share_button=document.getElementById("share_button");
        share_button.style.visibility='hidden'
    }
}