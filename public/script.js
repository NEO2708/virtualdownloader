var title = document.getElementById("title");
var content = document.getElementById("content");
var download = document.getElementById("download");
var form = document.getElementById("form");
var red = document.getElementsByClassName("red")[0];
var paste = document.getElementById("pstbtn");
var clear = document.getElementById("clrbtn");
var error = document.getElementById("error");
var htdw = document.getElementById("iasuh");
var huc = document.getElementById("iasuh");
var igdownload = document.getElementById("downloadButtonig");
var loader = document.getElementById("loader");
var inp = document.getElementById("postUrlInputIg")

function trigger() {
    var linkf = document.getElementById("postUrlInputIg").value;
    ist = linkf.includes("www.instagram.com")
    if (linkf == '') {
        error.innerHTML = "Please Paste The Link "
        paste.style.display = "block";
        clear.style.display = "none";
    }
    else if (ist == false) {
        error.innerHTML = "Please Paste Valid Link"
    }
    else {
        igdownload.innerHTML = "Please Wait ..."
        var url = "http://127.0.0.1:8000/insta?link=" + linkf;

        loader.style.display = "flex";
        fetch(url, { mode: 'cors', method: "GET" })
            .then((response) => response.json())
            .then((data) => {



                const videos = data.videourls;
                const images = data.imageurls;
        //         if (videos.length == 1) {
        //             loader.style.display = "none";
        //             form.style.display = "none"
        //             htdw.style.display = "none"


        //             content.innerHTML += `
        //         <div class="dcard">
        //             <div class="profilerr">


        //             <div class="colname">
        //             <span class="punun" >${data.username}</span>
                    
        //                 </div>

        //             </div>
        //             <div class="cover">
        //                 <img src="${data.videothumb}"  ></img>
        //             </div>
        //             <div class="dowlik">
        //                 <a href="${videos[0]}">Download Video</a>
        //             </div>
        //         </div>`
        //             red.style.display = "flex"
        //         }
        //         else if (images.length == 1) {
        //             loader.style.display = "none";
        //             form.style.display = "none"
        //             htdw.style.display = "none"


        //             content.innerHTML += `
        //          <div class="dcard">
        //         <div class="profilerr">

        //             <div class="colname">
        //                     <span class="punun" >${data.username}</span>
                            
        //                         </div>
        //         </div>
        //         <div class="cover">
        //             <img src="${images[0]}" alt="expired">
        //         </div>
        //         <div class="desc">
                    
        //         </div>                    
        //         <div class="dowlik">
        //             <a href="${images[0]}">Download Image</a>
        //         </div>
        //         </div> 

        //     `
        //             for (let index = 0; index < images.length; index++) {
        //                 loader.style.display = "none";
        //                 form.style.display = "none"
        //                 htdw.style.display = "none"


        //                 content.innerHTML += `
        //     <div class="dcard">
        //         <div class="profilerr">

        //             <div class="colname">
        //                 <span class="punun" >${data.username}</span>
                        
        //                     </div>
        //         </div>
        //         <div class="cover">
        //             <img src="${images[index]}" alt="expired">
        //         </div>
        //         <div class="dowlik">
        //             <a href="${images[index]}">Download Image</a>
        //         </div>
        //     </div> 

        // `
        //                 red.style.display = "flex"


        //             }

        //         }
               if (videos.length >= 1 || images.length >= 1) {

                    for (let index = 0; index < videos.length; index++) {
                        loader.style.display = "none";
                        form.style.display = "none"
                        htdw.style.display = "none"


                        content.innerHTML += `
                    <div class="dcard">
                        <div class="profilerr">


                            <div class="colname">
                            <span class="punun" >${data.username}</span>
                            
                                </div>
                            
                        </div>
                        <div class="cover">
                            <img src="${data.videothumb[index]}" controls ></img>
                        </div>
                        <div class="dowlik">
                            <a href="${videos[index]}">Download Video</a>
                        </div>
                    </div> 
`
                        red.style.display = "flex"

                    }
                    for (let index = 0; index < images.length; index++) {
                        loader.style.display = "none";
                        form.style.display = "none"
                        htdw.style.display = "none"


                        content.innerHTML += `
                    <div class="dcard">
                        <div class="profilerr">


                            <div class="colname">
                            <span class="punun" >${data.username}</span>
                            
                                </div>
                            
                        </div>
                        <div class="cover">
                            <img src="${images[index]}" controls ></img>
                        </div>
                        <div class="dowlik">
                            <a href="${images[index]}">Download Video</a>
                        </div>
                    </div> 
`
                        red.style.display = "flex"

                    }
                }


                else {
                    igdownload.innerHTML = "Download "

                    content.innerHTML = `<h1 class="err" >Check if the Account is Not PRIVATE and try again </h1>`
                    red.style.display = "flex"
                }

            })

    }
}


paste.addEventListener("click", async () => {

    try {
        const text = await navigator.clipboard.readText()
        inp.value += text;
        // igdownload.style.display="flex";
        trigger()
        paste.style.display = "none";
        clear.style.display = "block";

    } catch (error) {
        console.log('Failed to read clipboard. Using execCommand instead.');
        inp.focus();
        const result = document.execCommand('paste')
    }
})

inp.addEventListener("input", () => {
    paste.style.display = "none";
    clear.style.display = "block";
    trigger()
})
clear
function clearinp() {
    inp.value = '';
    paste.style.display = "block";
    clear.style.display = "none";
}