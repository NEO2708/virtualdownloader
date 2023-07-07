var title = document.getElementById("title")
var content = document.getElementById("content")
var download = document.getElementById("download")
var form = document.getElementById("form")
var red = document.getElementsByClassName("red")[0]

var error = document.getElementById("error")


var igdownload = document.getElementById("downloadButtonig")
var loader = document.getElementById("loader")

igdownload.addEventListener("click", () => {

    var linkf = document.getElementById("postUrlInputIg").value;
    ist = linkf.includes("www.instagram.com")
    if (linkf == '') {
        error.innerHTML = "Please enter The Url "
    }
    else if (ist == false) {
        error.innerHTML = "Please enter Valid  URl From Instgram App "
    }
    else {
        igdownload.innerHTML = "Please Wait ..."
        loader.style.display = "flex";
        var url = "https://virtualdownloader.vercel.app/insta?link=" + linkf;
        form.style.display="none"
        execute(url)
    }


})

function execute(url) {
    fetch(url, { mode: 'cors', method: "GET" })
        .then((response) => response.json())
        .then((data) => {



            const videos = data.videourls;
            const images = data.imageurls;
            if (videos.length == 1) {
                loader.style.display = "none";
                form.style.display = "none"


                content.innerHTML += `
                <div class="dcard">
                    <div class="profilerr">


                    <div class="colname">
                    <span class="punun" >${data.username}</span>
                    <span class="pun" >${data.name}</span>
                        </div>

                    </div>
                    <div class="cover">
                        <video src="${videos[0]}" controls ></video>
                    </div>
                    <div class="dowlik">
                        <a href="${videos[0]}">Download Video</a>
                    </div>
                </div>`
                red.style.display = "flex"
            }
            if (images.length == 1) {
                loader.style.display = "none";

                content.innerHTML += `
                 <div class="dcard">
                <div class="profilerr">

                    <div class="colname">
                            <span class="punun" >${data.username}</span>
                            <span class="pun" >${data.name}</span>
                                </div>
                </div>
                <div class="cover">
                    <img src="${images[0]}" alt="expired">
                </div>
                <div class="desc">
                    <span class="pun" >${data.caption}</span>
                </div>                    
                <div class="dowlik">
                    <a href="${images[0]}">Download Image</a>
                </div>
                </div> 

            `
            red.style.display="flex"

            }
            if (videos.length > 1) {

                for (let index = 0; index < videos.length; index++) {
                    loader.style.display = "none";

                    content.innerHTML += `
                    <div class="dcard">
                        <div class="profilerr">


                            <div class="colname">
                            <span class="punun" >${data.username}</span>
                            <span class="pun" >${data.name}</span>
                                </div>
                            
                        </div>
                        <div class="cover">
                            <video src="${videos[index]}" controls ></video>
                        </div>
                        <div class="dowlik">
                            <a href="${videos[index]}">Download Video</a>
                        </div>
                    </div> 
`
                    red.style.display = "flex"

                }
            }
            if (images.length > 1) {
                for (let index = 0; index < images.length; index++) {
                    loader.style.display = "none";

                    content.innerHTML += `
                <div class="dcard">
                    <div class="profilerr">

                        <div class="colname">
                            <span class="punun" >${data.username}</span>
                            <span class="pun" >${data.name}</span>
                                </div>
                    </div>
                    <div class="cover">
                        <img src="${images[index]}" alt="expired">
                    </div>
                    <div class="dowlik">
                        <a href="${images[index]}">Download Image</a>
                    </div>
                </div> 

            `
                    red.style.display = "flex"


                }
            }

        }

        ).catch(error =>
            igdownload.innerHTML = "Download ",

            content.innerHTML = `<h1 class="err" >Check if the Account is Not PRIVATE and try again </h1>`,
            red.style.display = "flex"

        )
}