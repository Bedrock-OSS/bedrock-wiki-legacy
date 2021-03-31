---
layout: page
title: Discord
parent: Home
nav_exclude: true
---


## Discord

The Bedrock Wiki community features two primary Discord servers. The Bedrock Addons Discord is primarily for learning about the various aspects of Bedrock addons, including scripting, custom-entities, and block & item customization. The Bedrock OSS (Open Source Software) Discord exists to discuss, support, and collaborate on various Minecraft Bedrock projects, namely the Bedrock Wiki. Below, there is also a curated list of Discords that may be helpful to those interested in the Bedrock community.  

{::nomarkdown}

<style>
iframe {
box-shadow: -1px 3px 28px -4px rgba(0,0,0,0.76);
float: left;
width: 98%;
height: 500px;
margin-bottom: 25px;
}
</style>

<script>
function toggleWidget() {
switch(theme) {
  case "Discord Dark": widget = "dark"; break;
  case "Dark": widget = "dark"; break;
  case "Light": widget = "light"; break;
  default: widget = "dark";
}
  var server1="https://discord.com/widget?id=494194063730278411&theme=";
  var server2="https://discord.com/widget?id=523663022053392405&theme=";
  var frame1=server1+widget;
  var frame2=server2+widget;
  document.getElementsByClassName("theme-switcher")[0].setAttribute('onchange', "toggleWidget()");
  document.getElementById("iframe1").setAttribute('src', frame1);
  document.getElementById("iframe2").setAttribute('src', frame2);
}
window.onload = toggleWidget;
</script>

<div>
    <span style="float:right; width:49%; height:500">
        {% include filepath.html path="Bedrock/OSS"%}
        <iframe src="https://discord.com/widget?id=494194063730278411" id="iframe1" height="500" width="98%" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
    </span>
</div>
<div>
    <span style="float:right; width:49%; height:500">
        {% include filepath.html path="Bedrock/Addons"%}
        <iframe src="https://discord.com/widget?id=523663022053392405" id="iframe2" height="500" width="98%" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
    </span>
</div>
{:/nomarkdown}

[More Discord Servers](/knowledge/useful-links.html#discord-links){: .btn .btn-blue }