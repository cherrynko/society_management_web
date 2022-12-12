document.getElementById("contact-HR").addEventListener("click", ()=>{
    img = document.getElementById("home-card-img");
    if(img!=null){
        img.remove();
    }
    removable = document.getElementById("remove");
    if(removable != null){
        removable.remove();
    }

    document.getElementById("home-card-title").innerText = "Contact HR using the following Email/Phone no:";
    document.getElementById("home-card-text").innerText = "someone@mail.com\n03330000000"
    const input_form = document.createElement("form");
    input_form.setAttribute('id', 'remove');
    input_form.style.textAlign = "center";
    text = document.createElement("p");
    text.innerHTML = "<b>..or drop HR a quick message!</b>";
    input = document.createElement("textarea");
    input.style.height = "200px";
    input.style.width = "100%";
    button = document.createElement("button");
    button.setAttribute("class", "btn btn-secondary");
    button.style.margin = "20px 0px";
    button.innerText = "Submit";
    input_form.appendChild(text);
    input_form.appendChild(input);
    input_form.appendChild(button);
    document.getElementById("home-card").appendChild(input_form);
});

document.getElementById("member-info").addEventListener("click", ()=>{
    // document.getElementById("home-card-img").remove();
    // document.getElementById("home-card-text").remove();
    removable = document.getElementById("home-card-img");
    if(removable != null){
        removable.remove()
    }
    removable = document.getElementById("remove");
    if(removable != null){
        removable.remove();
    }
    document.getElementById("home-card-title").innerText = "Your members:";
    document.getElementById("home-card-text").innerText = "Here's a list of all members working under you!"
    const members_list = document.createElement("ul");
    members_list.setAttribute('id', 'remove');
    members_list.appendChild(document.createElement("li").innerHTML = '<h4>Member x:</h4><p>Info on member x..</p>')
    document.getElementById("home-card").appendChild(members_list);
});

document.getElementById("contact-director").addEventListener("click", ()=>{
    img = document.getElementById("home-card-img");
    if(img!=null){
        img.remove();
    }
    removable = document.getElementById("remove");
    if(removable != null){
        removable.remove();
    }
    document.getElementById("home-card-title").innerText = "Contact director using the following Email/Phone no:";
    document.getElementById("home-card-text").innerText = "someone@mail.com\n03330000000"
    const input_form = document.createElement("form");
    input_form.setAttribute('id', 'remove');
    input_form.style.textAlign = "center";
    text = document.createElement("p");
    text.innerHTML = "<b>..or drop your director a quick message!</b>";
    input = document.createElement("textarea");
    input.style.height = "200px";
    input.style.width = "100%";
    button = document.createElement("button");
    button.setAttribute("class", "btn btn-secondary");
    button.style.margin = "20px 0px";
    button.innerText = "Submit";
    input_form.appendChild(text);
    input_form.appendChild(input);
    input_form.appendChild(button);
    document.getElementById("home-card").appendChild(input_form);
});

/*
document.getElementById("fin-records").addEventListener("click", ()=>{
    img = document.getElementById("home-card-img");
    if(img!=null){
        img.remove();
    }
    removable = document.getElementById("remove");
    if(removable != null){
        removable.remove();
    }
    const fin_form = document.createElement("form");
    fin_form.style.textAlign = "center";


*/

