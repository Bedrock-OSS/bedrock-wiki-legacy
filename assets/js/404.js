// get current url
var currenturl = window.location.href;
// make it lowercase and replace all "_" with "-"
var redirecturl = currenturl.toLowerCase().replace(/_/g, "-");
// if the output url is different to the current url, redirect to the new url

if (currenturl !== redirecturl) {
    window.location.replace(redirecturl);
}
