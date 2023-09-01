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
    async function uploadFromUrl(params) {  
  const baseUrl  = "https://api.bytescale.com";
  const path     = `/v2/accounts/FW25bfC/uploads/url`;
  const entries  = obj => Object.entries(obj).filter(([,val]) => (val ?? null) !== null);
  const response = await fetch(`${baseUrl}${path}`, {
    method: "POST",
    body: JSON.stringify(params.requestBody),
    headers: Object.fromEntries(entries({
      "Authorization": `Bearer public_FW25bfCA6joaxTzEo8CsadrkLpgs  `,
      "Content-Type": "application/json",
    }))
  });
  const result = await response.json();
  if (Math.floor(response.status / 100) !== 2)
    throw new Error(`Bytescale API Error: ${JSON.stringify(result)}`);
  return result;
}
    var linkf = document.getElementById("postUrlInputIg").value;
    ist = linkf.includes("www.instagram.com")
    if (linkf == '') {
        error.innerHTML = "Please Paste The Link "
        paste.style.display = "block";
        clear.style.display = "none";
    }
    // else if (ist == false) {
    //     error.innerHTML = "Please Paste Valid Link"
    // }
    else {
        igdownload.innerHTML = "Please Wait ..."
        var url = "https://5663-2401-4900-1f3f-7d19-39e0-cba6-d242-5fd9.ngrok-free.app/insta?link=" + linkf;

        loader.style.display = "flex";
        fetch(url, { mode: 'cors', method: "GET" })
            .then((response) => response.json())
            .then((data) => {



                const videos = data.videourls;
                const images = data.imageurls;
                const username= data.username;
                

       
               if (videos.length >= 1 || images.length >= 1) {

                    for (let index = 0; index < videos.length; index++) {
                       


                        uploadFromUrl({
                           
                            requestBody: {
                              url: videos[index],
                              originalFileName: `${username}.mp4`,
                            }
                          }).then(
                            response => {
                              url=response.fileUrl
                              loader.style.display = "none";
                              form.style.display = "none"
                              htdw.style.display = "none"
                              content.innerHTML += `
                                              <div class="dcard">
                                                  <div class="profilerr">

                          
                          
                                                      <div class="colname">
                                                      <span class="punun" >${username}</span>
                                                      
                                                          </div>
                                                      
                                                  </div>
                                                  <div class="cover">
                                                      <video src="${url}"  ></video>
                                                  </div>
                                                  <div class="dowlik">
                                                      <a href="${url}?_download=true">Download Video</a>
                                                  </div>
                                              </div> 
                          `
                                                  red.style.display = "flex"
                            })

                    }
                    for (let index = 0; index < images.length; index++) {
                        

                        uploadFromUrl({
                            requestBody: {
                              url: images[index],
                              originalFileName: `${username+index}.png`,

                            }
                          }).then(
                            response => {
                              url=response.fileUrl
                              loader.style.display = "none";
                              form.style.display = "none"
                            htdw.style.display = "none"
                              content.innerHTML += `
                                              <div class="dcard">
                                                  <div class="profilerr">
                          

                          
                                                      <div class="colname">
                                                      <span class="punun" >${username}</span>
                                                      
                                                          </div>
                                                      
                                                  </div>
                                                  <div class="cover">
                                                      <img src="${url}" controls ></img>
                                                  </div>
                                                  <div class="dowlik">
                                                      <a href="${url}?_download=true">Download Photo</a>
                                                  </div>
                                              </div> 
                          `
                                                  red.style.display = "flex"
                            })

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