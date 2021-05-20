var redirectors = {
    "/assets/guide/template_packs/README": "/guide/download-packs",
    "/knowledge/namespaces": "/concepts/namespaces"
}

// HANDLE CASE AND UNDERSCORES
// get current url
var currenturl = window.location.href;

// make it lowercase and replace all "_" with "-"
var redirecturl = currenturl.toLowerCase().replace(/_/g, "-");

// if the output url is different to the current url, redirect to the new url
if (currenturl !== redirecturl) {
    window.location.replace(redirecturl);
}

// HANDLE REDIRECTION

var path = window.location.pathname;
var newpath = redirectors[path];

if (newpath) {
    window.location.pathname = newpath;
}


